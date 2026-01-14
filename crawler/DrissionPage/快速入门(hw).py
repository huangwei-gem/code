# 启动浏览器

from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com/')





# 爬取gitee项目标题和链接
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 爬取3页
for i in range(1, 7):
    # 访问某一页的网页
    page.get(f'https://gitee.com/explore/all?page={i}')
    # 获取所有开源库<a>元素列表
    links = page.eles('.title project-namespace-path')
    # 遍历所有<a>元素
    for link in links:
        # 打印链接信息
        print(link.text, link.link)




# 查找元素
# 根据 class 或 id 查找
page.ele('#ele_id')  # 等价于 page.ele('@id=ele_id')
page.ele('#:ele_id')  # 等价于 page.ele('@id:ele_id')
page.ele('.ele_class')  # 等价于 page.ele('@class=ele_class')
page.ele('.:ele_class')  # 等价于 page.ele('@class:ele_class')

# 根据 tag name 查找
page.ele('tag:li')  # 查找第一个 li 元素
page.eles('tag:li')  # 查找所有 li 元素

# 根据 tag name 及属性查找
page.ele('tag:div@class=div_class')  # 查找 class 为 div_class 的 div 元素




