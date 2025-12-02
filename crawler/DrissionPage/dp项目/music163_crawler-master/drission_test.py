from DrissionPage import WebPage,ChromiumOptions
import time
# import requests
#tit f-thide s-fc0
# requests.get()
def page_data(page):
    data = []
    els = page.eles('@class=tit f-thide s-fc0')
    for ele in els:
        href = ele.attr('href')
        title = ele.attr('title')
        data_str = title+' | '+href
        data.append(data_str)
    
    return data

co = ChromiumOptions()
co.headless(True)
co.auto_port()
# co.set_argument('--guest')
# co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0')
page = WebPage(chromium_options = co)
url = "https://music.163.com/#/discover/playlist"
page.get(url,retry=3,interval=2,timeout=15)
data = page_data(page)

for i in range(1,5):
    btn = page.ele('@class=zbtn znxt')
    btn.click()
    new_data = page_data(page)
    data.extend(new_data)

# for i in data:
#     print("歌单链接:::"+i)

with open('music_href','a') as f:
    for item in data:
        f.write(item+'\n')
page.quit()