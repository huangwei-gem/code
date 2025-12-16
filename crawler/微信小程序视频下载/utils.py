import os
import logging
import requests
from urllib.parse import urljoin
from config import config

# 尝试导入加密库，兼容不同的安装方式
try:
    from Crypto.Cipher import AES
except ImportError:
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        # 定义兼容的AES类
        class AES:
            def __init__(self, key, mode, iv=None):
                self.key = key
                self.mode = mode
                self.iv = iv
                self.backend = default_backend()
            
            def decrypt(self, data):
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=self.backend)
                decryptor = cipher.decryptor()
                return decryptor.update(data) + decryptor.finalize()
                
        AES.MODE_CBC = 'cbc'
    except ImportError:
        # 如果都导入失败，在使用时会报错
        AES = None



# ==================== 日志工具 ====================

def setup_logger(name=__name__, level=None):
    """设置日志配置"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        # 设置日志级别
        log_level = level or getattr(logging, config.log_level.upper(), logging.INFO)
        logger.setLevel(log_level)
        
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        
        # 创建文件处理器
        os.makedirs(os.path.dirname(config.log_file), exist_ok=True)
        file_handler = logging.FileHandler(config.log_file, encoding='utf-8')
        file_handler.setLevel(log_level)
        
        # 定义日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        # 添加处理器
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger

# 创建全局日志实例
logger = setup_logger()

# ==================== 目录管理 ====================

def ensure_directories():
    """确保所有必需的目录都存在"""
    os.makedirs(config.video_download_path, exist_ok=True)
    os.makedirs(config.save_mp4_path, exist_ok=True)
    os.makedirs(config.save_temporary_ts_path, exist_ok=True)
    logger.info("所有目录已创建或存在")

def clear_temporary_files():
    """清理临时文件"""
    ts_dir = config.save_temporary_ts_path
    if os.path.exists(ts_dir):
        for file in os.listdir(ts_dir):
            file_path = os.path.join(ts_dir, file)
            try:
                os.remove(file_path)
                logger.debug(f"已删除临时文件: {file_path}")
            except Exception as e:
                logger.error(f"删除临时文件失败: {file_path}, 错误: {e}")

# ==================== 请求工具 ====================

def send_request(url, method='get', headers=None, cookies=None, data=None, json=None, params=None, verify=False, timeout=None):
    """发送HTTP请求（同步版本）"""
    timeout = timeout or config.timeout
    headers = headers or config.common_headers
    cookies = cookies or config.cookies
    
    try:
        if method.lower() == 'get':
            response = requests.get(
                url=url, 
                headers=headers, 
                cookies=cookies, 
                params=params,
                verify=verify, 
                timeout=timeout
            )
        else:
            response = requests.post(
                url=url, 
                headers=headers, 
                cookies=cookies, 
                data=data, 
                json=json,
                params=params,
                verify=verify, 
                timeout=timeout
            )
        
        response.raise_for_status()
        logger.debug(f"请求成功: {url}, 状态码: {response.status_code}")
        return response
    except requests.RequestException as e:
        logger.error(f"请求失败: {url}, 错误: {e}")
        return None

# ==================== 加密解密工具 ====================

def parse_AES_encryption(key_content):
    """解析AES加密信息"""
    try:
        if 'IV' in key_content or 'iv' in key_content:
            parse_result = key_content.split('=')
            # 获取加密方法
            encryption_method = parse_result[1].split(',')[0]
            parts = key_content.split(',')
            # 获取密钥链接
            uri_part = [part for part in parts if 'URI=' in part][0]
            key_url = uri_part.split('"')[1]
            # 获取 IV 值
            iv_part = [part for part in parts if 'IV=' in part]
            iv_hex = iv_part[0].split('=')[1]  # 获取 IV 的十六进制值
            # 移除 "0x" 前缀
            iv_value = iv_hex[2:] if iv_hex.startswith('0x') else iv_hex
        else:
            parse_result = key_content.split('=')
            encryption_method = parse_result[1].split(',')[0]
            key_url = parse_result[2].split('"')[1]
            iv_value = None
        
        logger.debug(f"解析AES加密信息成功，加密方法: {encryption_method}")
        return encryption_method, key_url, iv_value
    except Exception as e:
        logger.error(f"解析AES加密信息失败: {e}")
        raise

def AES_decode(key_url, iv):
    """获取AES解密器"""
    try:
        response = send_request(key_url)
        if response is None:
            raise Exception(f"无法获取解密密钥: {key_url}")
        
        key = response.content
        # 处理 IV
        if iv:
            # 如果 IV 是十六进制字符串，转换为字节
            if isinstance(iv, str):
                # 移除可能的 "0x" 前缀
                if iv.startswith('0x'):
                    iv = iv[2:]
                # 将十六进制字符串转换为字节
                iv_bytes = bytes.fromhex(iv)
            else:
                iv_bytes = iv
            AES_decode_data = AES.new(key, AES.MODE_CBC, iv_bytes)
        else:
            # 默认 IV 设置为16个字节的零
            AES_decode_data = AES.new(key, AES.MODE_CBC, bytes(16))
        
        logger.debug(f"AES解密器创建成功")
        return AES_decode_data
    except Exception as e:
        logger.error(f"AES解密器创建失败: {e}")
        raise

# ==================== M3U8解析工具 ====================

def parse_m3u8_data(m3u8_url):
    """解析M3U8数据，获取TS链接列表和加密信息"""
    try:
        response = send_request(m3u8_url)
        if response is None:
            raise Exception(f"无法获取M3U8数据: {m3u8_url}")
        
        m3u8_data = response.text
        each_line_list = m3u8_data.strip('\n').split('\n')
        all_ts_list = []
        video_time = []
        AES_decode_data = None
        base_url = '/'.join(m3u8_url.split('/')[:-1]) + '/'
        
        if '#EXTM3U' in m3u8_data:
            for i in range(len(each_line_list)):
                line = each_line_list[i]
                if '#EXT-X-KEY' in line:  # 判断是否加密
                    encryption_method, key_url, iv = parse_AES_encryption(line)
                    logger.info(f'检测到加密，加密方法：{encryption_method}')
                    # 处理相对路径和绝对路径
                    if not key_url.startswith('http'):
                        key_url = urljoin(base_url, key_url)
                    AES_decode_data = AES_decode(key_url, iv)
                # 检查是否是.ts片段行
                if not line.startswith('#') and (line.endswith('.ts') or '.ts?' in line):
                    # 处理相对路径和绝对路径
                    if line.startswith('http'):
                        each_ts_url = line
                    else:
                        each_ts_url = urljoin(base_url, line)
                    all_ts_list.append(each_ts_url)
                if line.startswith('#EXTINF'):
                    time_ = float(line.strip().split(':')[1][:-1])
                    video_time.append(time_)
        
        total_time = sum(video_time) / 60 if video_time else 0
        logger.info('视频时长约为：%.2f分钟' % total_time)
        logger.info('找到 %d 个视频片段' % len(all_ts_list))
        return all_ts_list, AES_decode_data
    except Exception as e:
        logger.error(f"解析M3U8数据失败: {e}")
        raise

# ==================== 文件操作工具 ====================

def get_safe_filename(filename):
    """获取安全的文件名，去除非法字符"""
    import re
    # 保留字母、数字、空格、下划线、连字符
    safe_filename = re.sub(r'[^a-zA-Z0-9\s_-]', '', filename)
    # 去除首尾空格
    safe_filename = safe_filename.strip()
    # 确保文件名不为空
    if not safe_filename:
        safe_filename = 'video'
    return safe_filename

def merge_ts_files(output_filename, ts_dir=None):
    """合并TS文件为MP4"""
    ts_dir = ts_dir or config.save_temporary_ts_path
    output_path = os.path.join(config.save_mp4_path, output_filename)
    
    try:
        if not os.path.exists(ts_dir):
            logger.error(f"临时目录不存在: {ts_dir}")
            return False
        
        ts_file_list = os.listdir(ts_dir)
        if not ts_file_list:
            logger.error(f"没有找到任何TS文件")
            return False
        
        # 按数字顺序排序
        ts_file_list.sort(key=lambda x: int(x.split('.')[0]))
        
        logger.info(f"开始合并 {len(ts_file_list)} 个TS文件到 {output_filename}")
        
        with open(output_path, 'wb+') as fw:
            for i, ts_file in enumerate(ts_file_list):
                ts_path = os.path.join(ts_dir, ts_file)
                if os.path.exists(ts_path):
                    with open(ts_path, 'rb') as fr:
                        fw.write(fr.read())
                    logger.debug(f"已合并 {i+1}/{len(ts_file_list)}: {ts_file}")
        
        logger.info(f"视频合并完成！已保存为 {output_filename}")
        return True
    except Exception as e:
        logger.error(f"合并TS文件失败: {e}")
        return False
