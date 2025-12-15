import requests
# from id_to_m3u8 import get_resource_id
import urllib3

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cookies = {
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
    'logintime': '1765614257',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://appryrtssf74394.h5.xet.citv.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://appryrtssf74394.h5.xet.citv.cn/p/course/ecourse/course_2eJuGzfSlwDMdhhTsS2I9heVaEn?type=2',
    'req-uuid': '20251213162418000647310',
    'retry': '1',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2219afe48405ba50-0bef8dac0676f18-26061a51-2073600-19afe48405c68c%22%7D; anony_token=6d0bda263ebdaf6d80709ecfe4977c5c; shop_version_type=4; sajssdk_2015_new_user_appryrtssf74394_h5_xet_citv_cn=1; ko_token=3c5de7cc48f862d94cb7718844e28f70; xenbyfpfUnhLsdkZbX=0; colla_login=1; newuserdays=90; olduserdays=180; regtime=1762936349; sa_jssdk_2015_appryrtssf74394_h5_xet_citv_cn=%7B%22distinct_id%22%3A%22u_6914461d4df48_sUBUDPhMTx%22%2C%22first_id%22%3A%2219b15d75cdd543-05c8dab2153f8b8-26061a51-2073600-19b15d75cdeb83%22%2C%22props%22%3A%7B%7D%7D; logintime=1765614257',
}

data = {
    'bizData[app_id]': 'appryrtssf74394',
    'bizData[resource_id]': 'v_66057ac5e4b0d84d784d2376',
    'bizData[course_id]': 'course_2eJuGzfSlwDMdhhTsS2I9heVaEn',
    'bizData[p_id]': 'chap_2eJugtSzGACCn6nIyAeQWXcFeBV',
    'bizData[order]': 'asc',
    'bizData[page]': '1',
    'bizData[page_size]': '50',
    'bizData[sub_course_id]': '',
}

response = requests.post(
    'https://appryrtssf74394.h5.xet.citv.cn/xe.course.business.avoidlogin.e_course.resource_catalog_list.get/1.0.0',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
    timeout=30  # 添加超时设置
)

def get_resource_id():
    # print(response.json())
    json_data = response.json()
    id_list = []
    for item in json_data['data']['list']:
        chapter_title = item['chapter_title']  
        resource_id = item['resource_id']
        course_id = item['course_id']
        id_list.append({'chapter_title': chapter_title, 'resource_id': resource_id, 'course_id': course_id})
    return id_list