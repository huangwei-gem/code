data = json.dumps(json_data, separators=(',', ':'))
response = requests.post('https://gw.7881.com/goods-service-api/api/goods/list', cookies=cookies, headers=headers, data=data)