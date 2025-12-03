import requests
import json
import re
# 从demo模块导入字体映射函数
from demo import UniversalFontRecognition

cookies = {
    '_lxsdk_cuid': '19adef88ddac8-04464c569ebf78-15313374-fa000-19adef88ddac8',
    '_lxsdk': '19adef88ddac8-04464c569ebf78-15313374-fa000-19adef88ddac8',
    '_lxsdk_s': '19adef88dda-522-cf5-6a2%7C%7C1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': '_lxsdk_cuid=19adef88ddac8-04464c569ebf78-15313374-fa000-19adef88ddac8; _lxsdk=19adef88ddac8-04464c569ebf78-15313374-fa000-19adef88ddac8; _lxsdk_s=19adef88dda-522-cf5-6a2%7C%7C1',
    'Referer': 'https://piaofang.maoyan.com/dashboard/movie',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36',
    'X-FOR-WITH': 'sgyMmX8CzJU60nSgyN0dNxeZwJ6o87OvVLDDFZmfef72IWTgppmhXXSAOSfBpmvpOtcGxaGCT9zYuiXAC/PMLHUL5PWdlg7aAyCM96AsTb7ghHyX37+L3ttvLHwC0SNSDugK/AWQ/MvPGbMOBkMU2O5jtFBg7JkhVlYHbnN47Za7zNsmVK0BhLzR5iZHASQ9NvGBLbEP0TeNqxEJQE1FFg==',
    'mygsig': '{"m1":"0.0.3","m2":0,"m3":"0.0.67_tool","ms1":"11a4460b9f8e350468e13fe6cdc14ba4","ts":1764677428384,"ts1":1764677421695}',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'orderType': '0',
    'uuid': 'a02f0cce-965f-4528-ab17-1c31f374c21e',
    'timeStamp': '1764677424921',
    'User-Agent': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjYyNjEuOTUgU2FmYXJpLzUzNy4zNg==',
    'index': '976',
    'channelId': '40009',
    'sVersion': '2',
    'signKey': 'db78ea487abbe8f677cb9e84b84ae71c',
    'WuKongReady': 'h5',
}

response = requests.get('https://piaofang.maoyan.com/dashboard-ajax/movie', params=params, cookies=cookies, headers=headers)

json_data = response.json()
# print(json_data)

# 获取字体文件地址
font_url = 'https://' + re.findall(r'//(.*?)\"\)',json_data['fontStyle'])[-1]
print(font_url)
font_content = requests.get(font_url, cookies=cookies, headers=headers).content
with open('font.woff', 'wb') as f:
    f.write(font_content)



result = []
# 预先加载字体识别器，避免重复加载
u_f_r = UniversalFontRecognition(r"font.woff")
recognition_result = u_f_r.crack()

for item in json_data['movieList']['list']:
    # 解密总票房
    test_text = item['boxSplitUnit']['num']+item['boxSplitUnit']['unit']
    
    # 使用正则表达式找到所有的HTML实体并替换
    import re
    html_entities = re.findall(r'&#x([0-9a-fA-F]+);?', test_text)
    
    decrypted_text = test_text
    for entity in html_entities:
        try:
            unicode_code = int(entity, 16)
            map_text = recognition_result.get(unicode_code, '.')
            decrypted_text = decrypted_text.replace(f'&#x{entity};', map_text)
        except ValueError:
            continue
    
    print(f"原始: {test_text}")
    print(f"解密: {decrypted_text}")
    decrypted_box_office = decrypted_text


    result.append({
        '电影名字': item['movieInfo']['movieName'],
        '上座率': item['avgSeatView'],
        '场均人次': item['avgShowView'],
        '票房占比': item['splitBoxRate'],
        '上映时间': item['movieInfo']['releaseInfo'],
        '总票房': decrypted_box_office,
        '排片占比': item['showCountRate'],
        '排片场次': item['showCount'],
    })

# 输出最终结果
print("\n解密后的票房数据:")
print(result)