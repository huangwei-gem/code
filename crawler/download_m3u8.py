import os
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import urllib3
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import logging
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

lock = threading.Lock()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'download_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def download_segment(session, idx, ts_url, temp_dir, key, iv, total_segments):
    """
    下载单个ts片段
    
    :param session: requests会话
    :param idx: 片段索引
    :param ts_url: ts片段URL
    :param temp_dir: 临时目录
    :param key: 解密密钥
    :param iv: 初始化向量
    :param total_segments: 总片段数
    :return: (idx, ts_filename) 或 None
    """
    ts_filename = os.path.join(temp_dir, f'segment_{idx:04d}.ts')
    
    if os.path.exists(ts_filename):
        return (idx, ts_filename)
    
    max_retries = 5
    for retry in range(max_retries):
        try:
            response = session.get(ts_url, verify=False, timeout=60)
            if response.status_code == 200:
                ts_data = response.content
                
                if key and iv:
                    cipher = AES.new(key, AES.MODE_CBC, iv)
                    try:
                        decrypted_data = cipher.decrypt(ts_data)
                        decrypted_data = unpad(decrypted_data, AES.block_size)
                        with open(ts_filename, 'wb') as f:
                            f.write(decrypted_data)
                    except Exception:
                        with open(ts_filename, 'wb') as f:
                            f.write(ts_data)
                else:
                    with open(ts_filename, 'wb') as f:
                        f.write(ts_data)
                
                return (idx, ts_filename)
            else:
                logger.warning(f"[{idx}/{total_segments}] 下载失败，状态码: {response.status_code}")
        
        except requests.exceptions.Timeout:
            if retry < max_retries - 1:
                logger.warning(f"[{idx}/{total_segments}] 下载超时，重试 {retry + 1}/{max_retries}")
                import time
                time.sleep(3)
            else:
                logger.error(f"[{idx}/{total_segments}] 下载超时，已达到最大重试次数")
        except Exception as e:
            if retry < max_retries - 1:
                logger.warning(f"[{idx}/{total_segments}] 下载出错: {e}，重试 {retry + 1}/{max_retries}")
                import time
                time.sleep(2)
            else:
                logger.error(f"[{idx}/{total_segments}] 下载失败: {e}")
    
    return None


def download_m3u8_content(m3u8_file_path, output_dir='downloaded_videos', max_workers=10):
    """
    下载m3u8文件中的所有ts片段并合并成完整视频
    
    :param m3u8_file_path: m3u8文件路径
    :param output_dir: 输出目录
    :param max_workers: 线程池大小
    """
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(m3u8_file_path, 'r', encoding='utf-8') as f:
        m3u8_content = f.read()
    
    lines = m3u8_content.strip().split('\n')
    
    key_url = None
    iv = None
    ts_urls = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('#EXT-X-KEY'):
            match = re.search(r'URI="([^"]+)"', line)
            if match:
                key_url = match.group(1)
            
            iv_match = re.search(r'IV=0x([0-9a-fA-F]+)', line)
            if iv_match:
                iv = bytes.fromhex(iv_match.group(1))
        
        elif line and not line.startswith('#'):
            ts_urls.append(line)
    
    if not ts_urls:
        logger.error("未找到ts片段URL")
        return
    
    base_name = os.path.splitext(os.path.basename(m3u8_file_path))[0]
    video_output_path = os.path.join(output_dir, f'{base_name}.mp4')
    
    if os.path.exists(video_output_path):
        file_size = os.path.getsize(video_output_path)
        logger.info(f"视频已存在: {base_name}.mp4 (大小: {file_size / 1024 / 1024:.2f} MB)，跳过")
        return
    
    temp_dir = os.path.join(output_dir, f'{base_name}_temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    logger.info(f"开始下载视频: {base_name}")
    logger.info(f"总片段数: {len(ts_urls)}")
    logger.info(f"线程数: {max_workers}")
    
    key = None
    if key_url:
        logger.info(f"检测到加密，下载密钥: {key_url}")
        
        try:
            session = requests.Session()
            response = session.get(key_url, verify=False, timeout=10)
            if response.status_code == 200:
                key = response.content
                logger.info(f"密钥下载完成，长度: {len(key)} 字节")
            else:
                logger.error(f"密钥下载失败，状态码: {response.status_code}")
        except requests.exceptions.Timeout:
            logger.error("密钥下载超时")
        except Exception as e:
            logger.error(f"密钥下载失败: {e}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    downloaded_files = []
    completed = 0
    failed = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        
        for idx, ts_url in enumerate(ts_urls, 1):
            future = executor.submit(
                download_segment,
                session, idx, ts_url, temp_dir, key, iv, len(ts_urls)
            )
            futures[future] = idx
        
        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    downloaded_files.append(result)
                    completed += 1
                    with lock:
                        if completed % 10 == 0 or completed == len(ts_urls):
                            logger.info(f"进度: {completed}/{len(ts_urls)} ({completed * 100 // len(ts_urls)}%)")
                else:
                    failed += 1
            except Exception as e:
                failed += 1
                logger.error(f"下载任务出错: {e}")
    
    if failed > 0:
        logger.info(f"下载完成，成功: {completed}，失败: {failed}")
    
    downloaded_files.sort(key=lambda x: x[0])
    sorted_files = [f[1] for f in downloaded_files]
    
    logger.info(f"合并视频片段到: {video_output_path}")
    
    with open(video_output_path, 'wb') as outfile:
        for ts_file in sorted_files:
            if os.path.exists(ts_file):
                with open(ts_file, 'rb') as infile:
                    outfile.write(infile.read())
    
    file_size = os.path.getsize(video_output_path)
    logger.info(f"视频下载完成: {video_output_path} (大小: {file_size / 1024 / 1024:.2f} MB)")
    
    import shutil
    try:
        shutil.rmtree(temp_dir)
        logger.info("临时文件已清理")
    except Exception as e:
        logger.error(f"清理临时文件失败: {e}")


def download_all_m3u8(m3u8_dir='m3u8_fils', output_dir='downloaded_videos', max_workers=10):
    """
    批量下载m3u8目录下的所有m3u8文件
    
    :param m3u8_dir: m3u8文件所在目录
    :param output_dir: 输出目录
    :param max_workers: 线程池大小
    """
    m3u8_files = [f for f in os.listdir(m3u8_dir) if f.endswith('.m3u8')]
    
    if not m3u8_files:
        logger.error(f"在 {m3u8_dir} 目录下未找到m3u8文件")
        return
    
    logger.info(f"找到 {len(m3u8_files)} 个m3u8文件")
    
    for m3u8_file in m3u8_files:
        m3u8_path = os.path.join(m3u8_dir, m3u8_file)
        logger.info(f"{'='*60}")
        download_m3u8_content(m3u8_path, output_dir, max_workers)


if __name__ == "__main__":
    import sys
    
    m3u8_dir = 'm3u8_fils'
    output_dir = 'downloaded_videos'
    max_workers = 10
    
    if len(sys.argv) > 1:
        m3u8_dir = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    if len(sys.argv) > 3:
        max_workers = int(sys.argv[3])
    
    download_all_m3u8(m3u8_dir, output_dir, max_workers)
