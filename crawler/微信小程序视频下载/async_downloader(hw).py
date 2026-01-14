import asyncio
import aiohttp
from urllib.parse import urljoin
from utils import logger, ensure_directories, merge_ts_files, get_safe_filename, parse_AES_encryption, AES_decode
from config import config


# ==================== 异步请求工具 ====================

async def async_send_request(
    url, method='get', headers=None, cookies=None, 
    data=None, json=None, params=None, verify=False, timeout=None
):
    """发送异步HTTP请求"""
    timeout = timeout or config.timeout
    headers = headers or config.common_headers
    cookies = cookies or config.cookies

    try:
        async with aiohttp.ClientSession(
            cookie_jar=aiohttp.CookieJar(unsafe=True) if cookies else None
        ) as session:
            kwargs = {
                'headers': headers,
                'timeout': aiohttp.ClientTimeout(total=timeout),
                'ssl': None if not verify else aiohttp.Fingerprint(False),
            }

            if cookies:
                kwargs['cookies'] = cookies
            if params:
                kwargs['params'] = params
            if data:
                kwargs['data'] = data
            if json:
                kwargs['json'] = json

            if method.lower() == 'get':
                async with session.get(url, **kwargs) as response:
                    response.raise_for_status()
                    logger.debug(f"异步请求成功: {url}, 状态码: {response.status}")
                    return response
            else:
                async with session.post(url, **kwargs) as response:
                    response.raise_for_status()
                    logger.debug(f"异步请求成功: {url}, 状态码: {response.status}")
                    return response
    except aiohttp.ClientError as e:
        logger.error(f"异步请求失败: {url}, 错误: {e}")
        return None

# ==================== 异步M3U8解析 ====================

async def async_parse_m3u8_data(m3u8_url):
    """异步解析M3U8数据"""
    try:
        response = await async_send_request(m3u8_url)
        if not response:
            raise Exception(f"无法获取M3U8数据: {m3u8_url}")
        
        m3u8_data = await response.text()
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
                    
                    # 使用同步的AES解码函数，因为Crypto库不支持异步
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
        logger.info(f'视频时长约为：{total_time:.2f}分钟')
        logger.info(f'找到 {len(all_ts_list)} 个视频片段')
        return all_ts_list, AES_decode_data
    except Exception as e:
        logger.error(f"异步解析M3U8数据失败: {e}")
        raise

# ==================== 异步TS下载 ====================

async def async_download_ts(i, ts_url, AES_decode_data, semaphore):
    """异步下载单个TS文件"""
    async with semaphore:
        try:
            # 确保目录存在
            ensure_directories()
            
            response = await async_send_request(ts_url)
            if response is None:
                logger.error(f'{i}.ts 下载失败！')
                return False
            
            ts_data = await response.read()
            if AES_decode_data:
                ts_data = AES_decode_data.decrypt(ts_data)
            
            with open(f'{config.save_temporary_ts_path}/{i}.ts', mode='wb+') as f:
                f.write(ts_data)
            logger.debug(f'{i}.ts 下载完成！')
            return True
        except Exception as e:
            logger.error(f'{i}.ts 下载出现异常：{e}')
            return False

# ==================== 异步下载器 ====================

async def async_download_m3u8(m3u8_url, chapter_title=None):
    """异步下载M3U8视频"""
    logger.info(f"开始异步下载视频: {chapter_title}")
    
    try:
        # 解析M3U8数据
        all_ts_list, AES_decode_data = await async_parse_m3u8_data(m3u8_url)
        
        if not all_ts_list:
            logger.error("没有找到TS文件，下载失败")
            return False
        
        # 创建信号量控制并发数
        semaphore = asyncio.Semaphore(config.max_concurrency)
        
        # 开始下载所有TS文件
        tasks = []
        for i, ts_url in enumerate(all_ts_list):
            task = async_download_ts(i, ts_url, AES_decode_data, semaphore)
            tasks.append(task)
        
        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        success_count = sum(1 for result in results if result)
        
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
        logger.error(f"异步下载视频失败: {e}")
        return False

async def async_download_video(m3u8_url, chapter_title=None):
    """异步下载视频的入口函数"""
    ensure_directories()
    return await async_download_m3u8(m3u8_url, chapter_title)

# ==================== 异步下载器类 ====================

class AsyncDownloader:
    """异步下载器类"""
    
    def __init__(self):
        self.loop = asyncio.get_event_loop()
    
    def download_video(self, m3u8_url, chapter_title=None):
        """同步接口，内部使用异步实现"""
        return self.loop.run_until_complete(async_download_video(m3u8_url, chapter_title))
    
    def close(self):
        """关闭事件循环"""
        if self.loop and not self.loop.is_closed():
            self.loop.close()
