# from mmap import ACCESS_COPY
# import requests

# headers = {
#     'sec-ch-ua-platform': '"Windows"',
#     'Referer': '',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'accept': '*/*, application/vnd.t1c.int-4174',
#     'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
#     'sec-ch-ua-mobile': '?0',
# }

# response = requests.get(
#     'https://6s77bgvf.18s8yd05.cc/putanginamo/m3u8/p/bcbec63e3f1fc295d01096bf01221874.m3u8',
#     headers=headers,
# )   
'https://6s77bgvf.18s8yd05.cc/putanginamo/m3u8/p/48de4dc62a7407e3675d5b307c0e4b9c.m3u8'




import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


import requests

headers = {
    'Host': 'api.82d0616f.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '216',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="140", "Edge";v="140"',
    'sec-ch-ua-mobile': '?1',
    'DeviceType': 'h5',
    'Time': '2026-01-20 14:38:10',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36 EdgA/140.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'text/plain',
    'Version': '3.0',
    'Origin': 'https://api.82d0616f.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

data = 'MAi8cl4TIwQ5Obfu8Eeq7oXZYszQy2qzpouiBAvJZ4hPQVGJ5rtxWOVKYsk43YLMgIPb3bz6LnnpuMF3cMVmRjM1q9eiEJukY/bPnlRKP9fVJSc5SCw0p/wZKOwRopwAr8HLnJe70laOySGvcevUSaq0SkPz+oApH6Ns9n2ySJY95z2dJELNW+db75nxlXzo7O4xDRKdMfnEoJ89M6djow=='

response = requests.post('https://api.82d0616f.com/putanginamo/movie/favorite', headers=headers, data=data,verify=False)
print(response.text)






decrypt_key='464c73336f41337032613339476e736d'
encrypt_key='5a7439576a45366350624c6b51325668'



url ='https://1help18.cwqvgj.com/m-eighth/m3u8/enc.key?sign=1768880918-a73a13f7f8cbe925f9b30835e2804d09-0-5b4eb418265b52276aaaf0c6ee5b313f'


AES = 'AES-128'
key_hex = '977b00697985feed47748f721010f568'
key_base64 = 'l3sAaXmF/u1HdI9yEBD1aA=='
iv_hex = '0x64cf692cebc516e4a86ac6081aae50ce'
