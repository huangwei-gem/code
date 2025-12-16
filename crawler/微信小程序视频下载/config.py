import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent

# ==================== 下载配置 ====================
# 下载路径配置
VIDEO_DOWNLOAD_PATH = os.getenv('VIDEO_DOWNLOAD_PATH', str(BASE_DIR / 'm3u8Download'))
SAVE_MP4_PATH = os.getenv('SAVE_MP4_PATH', str(BASE_DIR / 'm3u8Download' / 'testVideo'))
SAVE_TEMPORARY_TS_PATH = os.getenv('SAVE_TEMPORARY_TS_PATH', str(BASE_DIR / 'm3u8Download' / 'temporary_ts'))

# 线程数配置
MAX_WORKERS = int(os.getenv('MAX_WORKERS', '10'))

# 异步协程并发数
MAX_CONCURRENCY = int(os.getenv('MAX_CONCURRENCY', '10'))

# 超时设置（秒）
TIMEOUT = int(os.getenv('TIMEOUT', '30'))

# ==================== 请求配置 ====================
# 通用Headers
COMMON_HEADERS = {
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://appryrtssf74394.h5.xet.citv.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://appryrtssf74394.h5.xet.citv.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'accept': '*/*, application/vnd.t1c.int-18393',
    'accept-language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# Cookies配置
COOKIES = {
    'sensorsdata2015jssdkcross': '%7B%22%24device_id%22%3A%2219afe48405ba50-0bef8dac0676f18-26061a51-2073600-19afe48405c68c%22%7D',
    'anony_token': '6d0bda263ebdaf6d80709ecfe4977c5c',
    'shop_version_type': '4',
    'sajssdk_2015_new_user_appryrtssf74394_h5_xet_citv_cn': '1',
    'ko_token': '3c5de7cc48f862d94cb7718844e28f70',
    'xenbyfpfUnhLsdkZbX': '0',
    'colla_login': '1',
    'newuserdays': '90',
    'olduserdays': '180',
    'regtime': '1762936349',
    'sa_jssdk_2015_appryrtssf74394_h5_xet_citv_cn': '%7B%22distinct_id%22%3A%22u_6914461d4df48_sUBUDPhMTx%22%2C%22first_id%22%3A%2219b15d75cdd543-05c8dab2153f8b8-26061a51-2073600-19b15d75cdeb83%22%2C%22props%22%3A%7B%7D%7D',
    'logintime': '1765727052',
}

# API URL配置
API_URLS = {
    'RESOURCE_CATALOG': 'https://appryrtssf74394.h5.xet.citv.cn/xe.course.business.avoidlogin.e_course.resource_catalog_list.get/1.0.0',
    'VIDEO_DETAIL': 'https://appryrtssf74394.h5.xet.citv.cn/xe.course.business.video.detail_info.get/2.0.0',
    'PLAY_URL': 'https://appryrtssf74394.h5.xet.citv.cn/xe.material-center.play/getPlayUrl',
}

# 请求参数配置
REQUEST_PARAMS = {
    'sign': '65b93565164e5dc84cc6d21aa08bd535',
    't': '693da69c',
    'us': 'mchLSxJuko',
}

# 资源目录请求数据
RESOURCE_CATALOG_DATA = {
    'bizData[app_id]': 'appryrtssf74394',
    'bizData[resource_id]': 'v_66057ac5e4b0d84d784d2376',
    'bizData[course_id]': 'course_2eJuGzfSlwDMdhhTsS2I9heVaEn',
    'bizData[p_id]': 'chap_2eJugtSzGACCn6nIyAeQWXcFeBV',
    'bizData[order]': 'asc',
    'bizData[page]': '1',
    'bizData[page_size]': '50',
    'bizData[sub_course_id]': '',
}

# 视频详情请求数据模板
VIDEO_DETAIL_DATA_TEMPLATE = {
    'bizData[resource_id]': '{resource_id}',
    'bizData[product_id]': 'course_2eJuGzfSlwDMdhhTsS2I9heVaEn',
    'bizData[opr_sys]': 'Win32',
}

# 获取播放URL请求数据模板
PLAY_URL_DATA_TEMPLATE = {
    'org_app_id': 'appryrtssf74394',
    'app_id': 'appryrtssf74394',
    'user_id': 'u_6914461d4df48_sUBUDPhMTx',
    'play_sign': ['{play_sign}'],
    'play_line': 'A',
    'opr_sys': 'Win32',
}

# ==================== 日志配置 ====================
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', str(BASE_DIR / 'logs' / 'download.log'))

# ==================== 其他配置 ====================
# 重试次数
RETRY_TIMES = int(os.getenv('RETRY_TIMES', '3'))

# 是否使用异步模式（默认使用多线程）
USE_ASYNC = os.getenv('USE_ASYNC', 'False').lower() in ['true', '1', 'yes']

# ==================== 配置类 ====================
class Config:
    """配置类，方便在代码中使用"""
    def __init__(self):
        self.base_dir = BASE_DIR
        self.video_download_path = VIDEO_DOWNLOAD_PATH
        self.save_mp4_path = SAVE_MP4_PATH
        self.save_temporary_ts_path = SAVE_TEMPORARY_TS_PATH
        self.max_workers = MAX_WORKERS
        self.max_concurrency = MAX_CONCURRENCY
        self.timeout = TIMEOUT
        self.common_headers = COMMON_HEADERS
        self.cookies = COOKIES
        self.api_urls = API_URLS
        self.request_params = REQUEST_PARAMS
        self.resource_catalog_data = RESOURCE_CATALOG_DATA
        self.video_detail_data_template = VIDEO_DETAIL_DATA_TEMPLATE
        self.play_url_data_template = PLAY_URL_DATA_TEMPLATE
        self.log_level = LOG_LEVEL
        self.log_file = LOG_FILE
        self.retry_times = RETRY_TIMES
        self.use_async = USE_ASYNC

# 创建全局配置实例
config = Config()
