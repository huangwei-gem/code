from utils import send_request, logger
from config import config

def get_m3u8_url(resource_id):
    """通过资源ID获取M3U8播放URL"""
    try:
        # 第一步：获取视频详情和play_sign
        video_detail_data = {
            'bizData[resource_id]': resource_id,
            'bizData[product_id]': 'course_2eJuGzfSlwDMdhhTsS2I9heVaEn',
            'bizData[opr_sys]': 'Win32',
        }
        
        response = send_request(
            url=config.api_urls['VIDEO_DETAIL'],
            method='post',
            data=video_detail_data
        )
        
        if not response:
            logger.error(f"无法获取视频详情: {resource_id}")
            return None
        
        play_sign = response.json()['data']['video_info']['play_sign']
        logger.debug(f"成功获取play_sign: {play_sign}")
        
        # 第二步：获取播放URL
        play_url_data = {
            'org_app_id': 'appryrtssf74394',
            'app_id': 'appryrtssf74394',
            'user_id': 'u_6914461d4df48_sUBUDPhMTx',
            'play_sign': [play_sign],
            'play_line': 'A',
            'opr_sys': 'Win32',
        }
        
        response = send_request(
            url=config.api_urls['PLAY_URL'],
            method='post',
            json=play_url_data
        )
        
        if not response:
            logger.error(f"无法获取播放URL: {resource_id}")
            return None
        
        m3u8_url = response.json()['data'][play_sign]['play_list']['720p_hls']['play_url']
        logger.info(f"成功获取M3U8 URL: {m3u8_url}")
        
        return m3u8_url
    except Exception as e:
        logger.error(f"获取M3U8 URL失败: {resource_id}, 错误: {e}")
        return None
