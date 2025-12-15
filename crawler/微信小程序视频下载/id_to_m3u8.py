import requests
import time
import urllib3

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_m3u8_url(resource_id):
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
        'logintime': '1765611847',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://appryrtssf74394.h5.xet.citv.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://appryrtssf74394.h5.xet.citv.cn/p/course/video/v_66057ac5e4b0d84d784d2376?product_id=course_2eJuGzfSlwDMdhhTsS2I9heVaEn&course_id=course_2eJuGzfSlwDMdhhTsS2I9heVaEn&sub_course_id=',
        'req-uuid': '20251213154412000663371',
        'retry': '1',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        # 'cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2219afe48405ba50-0bef8dac0676f18-26061a51-2073600-19afe48405c68c%22%7D; anony_token=6d0bda263ebdaf6d80709ecfe4977c5c; shop_version_type=4; sajssdk_2015_new_user_appryrtssf74394_h5_xet_citv_cn=1; ko_token=3c5de7cc48f862d94cb7718844e28f70; xenbyfpfUnhLsdkZbX=0; colla_login=1; newuserdays=90; olduserdays=180; regtime=1762936349; sa_jssdk_2015_appryrtssf74394_h5_xet_citv_cn=%7B%22distinct_id%22%3A%22u_6914461d4df48_sUBUDPhMTx%22%2C%22first_id%22%3A%2219b15d75cdd543-05c8dab2153f8b8-26061a51-2073600-19b15d75cdeb83%22%2C%22props%22%3A%7B%7D%7D; logintime=1765727052',
    }

    data = {
        'bizData[resource_id]': resource_id,
        'bizData[product_id]': 'course_2eJuGzfSlwDMdhhTsS2I9heVaEn',
        'bizData[opr_sys]': 'Win32',
    }

    response = requests.post(
        'https://appryrtssf74394.h5.xet.citv.cn/xe.course.business.video.detail_info.get/2.0.0',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
        timeout=30  # 添加超时设置
    )

    play_sign = response.json()['data']['video_info']['play_sign']

    cookies1 = {
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

    headers1 = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://appryrtssf74394.h5.xet.citv.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://appryrtssf74394.h5.xet.citv.cn/p/course/video/v_66057ac5e4b0d84d784d2376?product_id=course_2eJuGzfSlwDMdhhTsS2I9heVaEn&course_id=course_2eJuGzfSlwDMdhhTsS2I9heVaEn&sub_course_id=',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        # 'cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2219afe48405ba50-0bef8dac0676f18-26061a51-2073600-19afe48405c68c%22%7D; anony_token=6d0bda263ebdaf6d80709ecfe4977c5c; shop_version_type=4; sajssdk_2015_new_user_appryrtssf74394_h5_xet_citv_cn=1; ko_token=3c5de7cc48f862d94cb7718844e28f70; xenbyfpfUnhLsdkZbX=0; colla_login=1; newuserdays=90; olduserdays=180; regtime=1762936349; sa_jssdk_2015_appryrtssf74394_h5_xet_citv_cn=%7B%22distinct_id%22%3A%22u_6914461d4df48_sUBUDPhMTx%22%2C%22first_id%22%3A%2219b15d75cdd543-05c8dab2153f8b8-26061a51-2073600-19b15d75cdeb83%22%2C%22props%22%3A%7B%7D%7D; logintime=1765727052',
    }

    json_data = {
        'org_app_id': 'appryrtssf74394',
        'app_id': 'appryrtssf74394',
        'user_id': 'u_6914461d4df48_sUBUDPhMTx',
        'play_sign': [
            play_sign,
        ],
        'play_line': 'A',
        'opr_sys': 'Win32',
    }

    response = requests.post(
        'https://appryrtssf74394.h5.xet.citv.cn/xe.material-center.play/getPlayUrl',
        cookies=cookies1,
        headers=headers1,
        json=json_data,
        verify=False,
        timeout=30  # 添加超时设置
    )

    # print(response.json())
    m3u8_url = response.json()['data'][play_sign]['play_list']['720p_hls']['play_url']

    return m3u8_url
