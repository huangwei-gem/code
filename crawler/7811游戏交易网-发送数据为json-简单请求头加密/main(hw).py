

import requests
import execjs
import json
cookies = {
    'SERVERID': '216',
    'home_page_yxb': '%7B%22gameid%22%3A%22G10%22%2C%22gamename%22%3A%22%E5%9C%B0%E4%B8%8B%E5%9F%8E%E4%B8%8E%E5%8B%87%E5%A3%AB%22%2C%22groupid%22%3A%22G10P001%22%2C%22serverid%22%3A%22G10P001001%22%2C%22groupserver%22%3A%22%E5%B9%BF%E4%B8%9C%E5%8C%BA%2F%E5%B9%BF%E4%B8%9C1%E5%8C%BA%22%2C%22tradeplace%22%3A%22%22%2C%22tradeplacename%22%3A%22%E4%BA%A4%E6%98%93%E6%96%B9%E5%BC%8F%22%2C%22camp%22%3A%22%22%2C%22refresh%22%3A%221%22%7D',
    'Hm_lvt_6fb35abaf76325a4316e33e23c984e73': '1763815971',
    'HMACCOUNT': '5F929BD1A22E6A3F',
    'home_page_search': '%7B%22gameid%22%3A%22A2705%22%2C%22goodschannel%22%3A%22100003%22%2C%22camp%22%3Anull%7D',
    'Hm_lpvt_6fb35abaf76325a4316e33e23c984e73': '1763819899',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://search.7881.com',
    'Referer': 'https://search.7881.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'lb-sign': '97d8887bb19cb97eb0b6c2e1ef192a89',
    'lb-timestamp': '1763819898795',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'SERVERID=216; home_page_yxb=%7B%22gameid%22%3A%22G10%22%2C%22gamename%22%3A%22%E5%9C%B0%E4%B8%8B%E5%9F%8E%E4%B8%8E%E5%8B%87%E5%A3%AB%22%2C%22groupid%22%3A%22G10P001%22%2C%22serverid%22%3A%22G10P001001%22%2C%22groupserver%22%3A%22%E5%B9%BF%E4%B8%9C%E5%8C%BA%2F%E5%B9%BF%E4%B8%9C1%E5%8C%BA%22%2C%22tradeplace%22%3A%22%22%2C%22tradeplacename%22%3A%22%E4%BA%A4%E6%98%93%E6%96%B9%E5%BC%8F%22%2C%22camp%22%3A%22%22%2C%22refresh%22%3A%221%22%7D; Hm_lvt_6fb35abaf76325a4316e33e23c984e73=1763815971; HMACCOUNT=5F929BD1A22E6A3F; home_page_search=%7B%22gameid%22%3A%22A2705%22%2C%22goodschannel%22%3A%22100003%22%2C%22camp%22%3Anull%7D; Hm_lpvt_6fb35abaf76325a4316e33e23c984e73=1763819899',
}

json_data = {
    'marketRequestSource': 'search',
    'sellerType': 'C',
    'gameId': 'A2705',
    'gtid': '100003',
    'tradePlace': '0',
    'goodsSortType': '1',
    'extendAttrList': [],
    'pageNum': 1,
    'pageSize': 20,
}

with open('test.js', encoding='utf-8') as f:
    code = f.read()
ctll = execjs.compile(code)
obj = ctll.call("sign", json_data)
print(obj)
headers['lb-sign'] = obj['lb-sign']
headers['lb-timestamp'] = str(obj['lb-timestamp'])

data = json.dumps(json_data, separators=(',', ':'))
response = requests.post('https://gw.7881.com/goods-service-api/api/goods/list', cookies=cookies, headers=headers, data=data)
print(response.text)


