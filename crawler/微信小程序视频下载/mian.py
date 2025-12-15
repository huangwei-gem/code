import requests
import os
import time
import urllib3
from gen_id import get_resource_id
from id_to_m3u8 import get_m3u8_url
from download_m3u8 import download_video


# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
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

params = {
    'sign': '65b93565164e5dc84cc6d21aa08bd535',
    't': '693da69c',
    'us': 'mchLSxJuko',
}



def main():
    id_list = get_resource_id()
    for item in id_list:
        chapter_title = item['chapter_title']
        resource_id = item['resource_id']
        course_id = item['course_id']
        m3u8_url = get_m3u8_url(resource_id)
        download_video(m3u8_url,chapter_title)
        time.sleep(5)

if __name__ == '__main__':
    main()