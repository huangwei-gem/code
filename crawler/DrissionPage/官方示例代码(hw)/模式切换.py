from DrissionPage import Chromium

# 连接浏览器并获取一个MixTab对象
tab = Chromium().latest_tab
# 访问网址
tab.get('https://gitee.com/explore/all')
# 切换到收发数据包模式
tab.change_mode()
# 获取所有行元素
items = tab.ele('.ui relaxed divided items explore-repo__list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('t:h3').text)
    print(item('.project-desc mb-1').text)
    print()



