import requests

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


print(response.text)