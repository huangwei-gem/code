from utils import send_request, logger
from config import config

def get_resource_id():
    """获取资源ID列表"""
    try:
        response = send_request(
            url=config.api_urls['RESOURCE_CATALOG'],
            method='post',
            data=config.resource_catalog_data
        )
        
        if response:
            json_data = response.json()
            id_list = []
            for item in json_data['data']['list']:
                chapter_title = item['chapter_title']  
                resource_id = item['resource_id']
                course_id = item['course_id']
                id_list.append({
                    'chapter_title': chapter_title, 
                    'resource_id': resource_id, 
                    'course_id': course_id
                })
            logger.info(f"成功获取 {len(id_list)} 个资源ID")
            return id_list
        else:
            logger.error("无法获取资源ID列表")
            return []
    except Exception as e:
        logger.error(f"获取资源ID列表失败: {e}")
        return []
