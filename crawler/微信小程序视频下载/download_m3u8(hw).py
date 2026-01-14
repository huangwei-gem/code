import os
import time
from concurrent.futures import ThreadPoolExecutor
from utils import (
    logger, ensure_directories, parse_m3u8_data, 
    send_request, merge_ts_files, get_safe_filename
)
from config import config
from async_downloader import AsyncDownloader

# ==================== 同步下载器 ====================

def download_ts(i, ts_url, AES_decode_data):
    """下载单个TS文件（同步）"""
    try:
        # 确保目录存在
        ensure_directories()
        
        response = send_request(ts_url)
        if response is None:
            logger.error(f'{i}.ts 下载失败！')
            return False
            
        ts_data = response.content
        if AES_decode_data:
            ts_data = AES_decode_data.decrypt(ts_data)
            
        with open(f'{config.save_temporary_ts_path}/{i}.ts', mode='wb+') as f:
            f.write(ts_data)
        logger.debug(f'{i}.ts 下载完成！')
        return True
    except Exception as e:
        logger.error(f'{i}.ts 下载出现异常：{e}')
        return False

def sync_download_m3u8(m3u8_url, chapter_title=None):
    """同步下载M3U8视频（多线程）"""
    logger.info(f"开始同步下载视频: {chapter_title}")
    
    try:
        # 解析M3U8数据
        all_ts_list, AES_decode_data = parse_m3u8_data(m3u8_url)
        
        if not all_ts_list:
            logger.error("没有找到TS文件，下载失败")
            return False
        
        # 使用线程池下载所有TS文件
        success_count = 0
        with ThreadPoolExecutor(max_workers=config.max_workers) as executor:
            futures = []
            for i, ts_url in enumerate(all_ts_list):
                future = executor.submit(download_ts, i, ts_url, AES_decode_data)
                futures.append(future)
            
            # 等待所有任务完成并统计成功数量
            for future in futures:
                if future.result():
                    success_count += 1
                    
        logger.info(f'视频下载结束！成功下载 {success_count}/{len(all_ts_list)} 个片段')
        
        if success_count > 0:
            # 合并TS文件
            safe_filename = get_safe_filename(chapter_title) if chapter_title else 'video'
            output_filename = f'{safe_filename}.mp4'
            if merge_ts_files(output_filename):
                logger.info(f"视频 {chapter_title} 下载完成")
                return True
            else:
                logger.error(f"视频 {chapter_title} 合并失败")
                return False
        else:
            logger.error(f"视频 {chapter_title} 下载失败，没有成功下载任何TS片段")
            return False
    except Exception as e:
        logger.error(f"同步下载视频失败: {e}")
        return False

# ==================== 通用下载接口 ====================

def download_video(m3u8_url, chapter_title, use_async=False):
    """通用视频下载接口，支持同步和异步两种模式
    
    Args:
        m3u8_url: M3U8播放地址
        chapter_title: 章节标题
        use_async: 是否使用异步模式（默认False，使用多线程）
        
    Returns:
        bool: 下载是否成功
    """
    start_time = time.time()
    
    try:
        if use_async:
            # 使用异步模式
            downloader = AsyncDownloader()
            result = downloader.download_video(m3u8_url, chapter_title)
            downloader.close()
        else:
            # 使用同步模式（多线程）
            result = sync_download_m3u8(m3u8_url, chapter_title)
        
        end_time = time.time()
        logger.info(f'视频 {chapter_title} 下载总共耗时：{end_time-start_time:.2f}秒')
        return result
    except Exception as e:
        end_time = time.time()
        logger.error(f'视频 {chapter_title} 下载异常，耗时：{end_time-start_time:.2f}秒，错误：{e}')
        return False
