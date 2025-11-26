import requests
import json
import execjs


headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pv4y-pc.youzy.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://pv4y-pc.youzy.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'agent': 'objectId:;provinceId:;provinceCode:;userPermissionId:;score:0;',
    'deviceId': 'd9e638f894bfd05cede55ce130369b82',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'u-sign': '643ff9499febb3ee34c95ffe0bb29cb0',
    'u-token': '',
}

json_data = {
    'keyword': '',
    'provinceNames': [],
    'natureTypes': [],
    'eduLevel': '',
    'categories': [],
    'features': [],
    'pageIndex': 1,
    'pageSize': 20,
    'sort': 11,
}


# 这是调用js的测试代码
with open('webpack.js', encoding='utf-8') as f:
    code = f.read()
ctll = execjs.compile(code)

# 调用JavaScript中的c函数，注意第二个参数应该是对象而不是字符串
obj = ctll.call("c", '/youzy.dms.basiclib.api.v1.label.get', json_data)

print(obj)
headers['u-sign'] = obj

# 发送请求前才将数据转换为JSON字符串
data = json.dumps(json_data, separators=(',', ':'))
response = requests.post('https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query', headers=headers, data=data)

print(response.text)