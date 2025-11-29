from DrissionPage import ChromiumPage
import pandas as pd

# contents列表用来存放所有爬取到的职位信息
contents = []

# 创建页面对象
page = ChromiumPage()

# 爬取30页
for i in range(1, 31):
    # 访问某一页的网页
    page.get(f'https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=python&pn={i}')
    # 查找 class 为 item__10RTO 的 div 元素
    divs = page.eles('tag:div@class=item__10RTO')
    # 提取公司、职位、薪资
    for div in divs:
        company = div.ele('.company-name__2-SjF')
        position = div.ele('#openWinPostion')
        money = div.ele('.money__3Lkgq')
        contents.append([company.text, position.text, money.text])
    print("正在爬取第", i, "页，总计获取到", len(contents), "条职位信息")

# 保存到csv文件
name = ['company', 'position', 'money']
contents_df = pd.DataFrame(columns=name, data=contents)
contents_df.to_csv("拉勾网Python职位信息.csv", index=False)