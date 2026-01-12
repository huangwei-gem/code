# 快速入门

本章将通过简单的例子，帮助您快速上手 DrissionPage，了解其基本用法和核心功能。

## 创建页面对象

DrissionPage 提供了三种主要的页面对象类型，您可以根据需求选择使用。每种类型的页面对象创建方式如下：

### 1. ChromiumPage（浏览器控制）

```python
from DrissionPage import ChromiumPage

# 创建浏览器页面对象
page = ChromiumPage()

# 打开网页
page.get('https://www.baidu.com')

# 关闭浏览器
page.quit()
```

### 2. SessionPage（数据包收发）

```python
from DrissionPage import SessionPage

# 创建会话页面对象
page = SessionPage()

# 打开网页
page.get('https://www.baidu.com')

# 获取响应状态码
print(page.status_code)
```

### 3. WebPage（混合模式）

```python
from DrissionPage import WebPage

# 创建网页对象（同时支持浏览器控制和数据包收发）
page = WebPage()

# 打开网页（默认使用 d 模式，即浏览器模式）
page.get('https://www.baidu.com')

# 切换到 s 模式（数据包模式）
page.change_mode('s')

# 再次请求页面（使用数据包方式）
page.get('https://www.baidu.com')

# 切回 d 模式
page.change_mode('d')

# 关闭浏览器
page.quit()
```

## 简单的页面操作

以下是一些常用的页面操作示例。

### 打开和导航网页

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()

# 打开网页
page.get('https://www.baidu.com')

# 刷新页面
page.refresh()

# 获取当前 URL
current_url = page.url
print(f'当前 URL: {current_url}')

# 获取页面标题
title = page.title
print(f'页面标题: {title}')

# 前进和后退
page.get('https://www.bing.com')
page.back()  # 返回百度
page.forward()  # 前进到必应
```

### 窗口操作

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 调整窗口大小
page.set_window_size(800, 600)

# 最大化窗口
page.max_window()

# 最小化窗口
page.min_window()

# 截取整个页面
page.get_screenshot('full_page.png')

# 截取可见区域
page.get_screenshot('visible_area.png', full_page=False)
```

### 执行 JavaScript

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 执行简单的 JavaScript
result = page.run_script('return document.title')
print(f'通过 JavaScript 获取的标题: {result}')

# 滚动到页面底部
page.run_script('window.scrollTo(0, document.body.scrollHeight)')

# 修改页面内容
page.run_script('document.getElementById("kw").value = "DrissionPage"')
```

## 查找和操作元素

DrissionPage 提供了强大且简洁的元素查找和操作功能。

### 元素查找方法

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 使用 CSS 选择器查找元素
search_box = page.ele('#kw')  # 百度搜索框

# 使用 XPath 查找元素
search_button = page.ele('xpath://input[@id="su"]')  # 百度搜索按钮

# 使用文本内容查找
news_link = page.ele('text:新闻')  # 查找文本为"新闻"的元素

# 使用元素属性查找
submit_button = page.ele('@value=百度一下')  # 查找属性 value="百度一下" 的元素
```

### 元素基本操作

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 输入文本
search_box = page.ele('#kw')
search_box.input('DrissionPage 自动化工具')

# 点击元素
search_button = page.ele('#su')
search_button.click()

# 获取元素文本内容
result_stats = page.ele('.nums')
if result_stats:
    print(f'搜索结果: {result_stats.text}')

# 获取元素属性
logo = page.ele('#lg img')
if logo:
    print(f'Logo 图片链接: {logo.attr("src")}')

# 获取元素HTML
result_item = page.ele('#content_left .result')
if result_item:
    print(f'第一个搜索结果的 HTML: {result_item.html}')
```

### 等待元素出现

DrissionPage 内置了智能等待功能，可以等待元素出现或满足特定条件。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 输入搜索内容并点击搜索
page.ele('#kw').input('DrissionPage')
page.ele('#su').click()

# 等待搜索结果出现（最多等待 10 秒）
result = page.ele('#content_left', timeout=10)

# 如果找到结果，打印第一个结果的标题
if result:
    first_title = result.ele('h3')
    if first_title:
        print(f'第一个搜索结果的标题: {first_title.text}')
```

### 查找多个元素

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://news.baidu.com')

# 查找所有新闻标题
news_titles = page.eles('.title-hot')

# 打印前 5 个新闻标题
for i, title in enumerate(news_titles[:5], 1):
    print(f'新闻 {i}: {title.text}')
```

## 简单的表单操作示例

以下是一个完整的表单填写和提交示例：

```python
from DrissionPage import ChromiumPage
from time import sleep

# 创建浏览器页面对象
page = ChromiumPage()

# 打开 GitHub 登录页面
page.get('https://github.com/login')

# 填写用户名和密码（请替换为自己的用户名和密码）
page.ele('#login_field').input('your_username')
page.ele('#password').input('your_password')

# 点击登录按钮
page.ele('input[name="commit"]').click()

# 等待页面加载完成
sleep(3)

# 检查是否登录成功
if page.ele('.avatar'):
    print('登录成功！')
else:
    print('登录失败！')

# 关闭浏览器
page.quit()
```

## 保存 Cookie

DrissionPage 可以方便地保存和加载 Cookie，实现免登录访问。

```python
from DrissionPage import ChromiumPage
import json

page = ChromiumPage()

# 打开网站并登录
page.get('https://example.com/login')
# ... 执行登录操作 ...

# 获取当前页面的 Cookie
cookies = page.get_cookies()

# 保存 Cookie 到文件
with open('cookies.json', 'w') as f:
    json.dump(cookies, f)

print('Cookie 已保存！')

# 关闭浏览器
page.quit()

# 下次使用 Cookie 访问
page = ChromiumPage()
# 加载 Cookie
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# 设置 Cookie
page.set_cookies(cookies)

# 访问需要登录的页面
page.get('https://example.com/user/profile')
# 此时无需登录即可访问
```

## 接下来

现在您已经了解了 DrissionPage 的基础用法，可以开始编写简单的自动化脚本了。在下一章中，我们将深入介绍 DrissionPage 的基础概念，帮助您更好地理解其工作原理。

查看 [基础概念](./concepts.md) 继续学习。 