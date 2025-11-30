import requests
import json

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cache-ts-v2': '1764483395364',
    'encryption': 'true',
    'language': 'zh',
    'origin': 'https://www.coinglass.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.coinglass.com/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

params = {
    'symbol': 'BTC',
    'timeType': '1',
}

response = requests.get('https://capi.coinglass.com/api/futures/longShortRate', params=params, headers=headers)


print(response.json())

