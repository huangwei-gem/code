# WebPage 详解

WebPage 是 DrissionPage 中的一个特殊页面对象，它结合了 SessionPage 和 ChromiumPage 的功能，允许在两种模式之间无缝切换。这种设计提供了极大的灵活性，让你能够在同一个脚本中，根据需要选择最合适的模式处理不同的任务。

## WebPage 概述

### 特点与优势

- **双模式支持**：同时支持会话模式（s模式）和浏览器模式（d模式）
- **无缝切换**：可在两种模式间随时切换，保持状态同步
- **统一接口**：无论使用哪种模式，API 保持一致
- **场景适应**：可根据不同场景选择最高效的模式
- **资源优化**：仅在需要浏览器功能时才启动浏览器

### 模式说明

- **s模式（会话模式）**：基于 requests 库，相当于 SessionPage，适合数据获取、接口测试等轻量级任务
- **d模式（浏览器模式）**：基于 CDP 协议，相当于 ChromiumPage，适合复杂交互、JavaScript 渲染等场景

## 创建 WebPage 对象

### 基本创建方式

```python
from DrissionPage import WebPage

# 创建默认 WebPage 对象（默认为d模式）
page = WebPage()

# 指定初始模式为s模式
page = WebPage(mode='s')
```

### 使用配置文件创建

```python
# 从指定配置文件创建
page = WebPage(crx_or_path='config.ini')

# 从默认配置文件创建
page = WebPage(read_file=True)
```

### 高级创建选项

```python
# 指定浏览器和会话参数
page = WebPage(
    # 浏览器设置
    chromium_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    user_data_path=r'C:\Users\Username\AppData\Local\Google\Chrome\User Data',
    headless=False,
    
    # 会话设置
    proxy='http://127.0.0.1:7890',
    timeout=10,
    
    # 初始模式
    mode='d'
)
```

## 模式切换

### 基本模式切换

```python
# 从d模式切换到s模式
page.change_mode()  # 默认切换到另一个模式
# 或者明确指定
page.change_mode('s')

# 从s模式切换到d模式
page.change_mode('d')

# 查看当前模式
current_mode = page.mode
print(f'当前模式: {current_mode}')  # 'd' 或 's'
```

### 模式切换时的同步

WebPage 在模式切换时会自动同步以下状态：

- 当前URL
- Cookies
- 本地存储（LocalStorage）
- 会话存储（SessionStorage）

这确保了在不同模式间切换时，用户登录状态和网站配置能够得到保留。

```python
# 示例：在不同模式下保持登录状态
# 使用s模式登录（速度快）
page = WebPage(mode='s')
page.get('https://example.com/login')

# 提交登录表单
page.ele('#username').input('user123')
page.ele('#password').input('password123')
page.ele('button[type="submit"]').click()

# 切换到d模式处理需要JavaScript的操作
page.change_mode('d')  # 自动同步cookies，保持登录状态

# 执行需要JavaScript的操作
page.run_js('console.log("已登录")')
```

### 使用上下文管理器临时切换模式

```python
# 在d模式下临时切换到s模式
page = WebPage(mode='d')
page.get('https://example.com')

with page.session_context() as session_page:
    # 这里是s模式
    data = session_page.get('https://api.example.com/data').json
    print(f'获取数据: {data}')

# 返回到d模式
print(f'当前模式: {page.mode}')  # 'd'

# 在s模式下临时切换到d模式
page = WebPage(mode='s')
page.get('https://example.com')

with page.browser_context() as browser_page:
    # 这里是d模式
    browser_page.run_js('alert("Hello!")')
    browser_page.get_alert().accept()

# 返回到s模式
print(f'当前模式: {page.mode}')  # 's'
```

## 模式选择策略

### 何时使用s模式（会话模式）

- 获取静态内容或简单HTML
- 访问API接口
- 表单提交（不需要JavaScript）
- 大量数据爬取（更高效）
- 对资源消耗敏感的场景

```python
# s模式示例：爬取文章列表
page = WebPage(mode='s')
page.get('https://example.com/articles')

# 提取所有文章链接
article_links = []
for article in page.eles('.article-item'):
    title = article.ele('.title').text
    link = article.ele('a').attr('href')
    article_links.append((title, link))

print(f'找到{len(article_links)}篇文章')
```

### 何时使用d模式（浏览器模式）

- 页面需要JavaScript渲染
- 需要模拟用户交互（点击、拖拽等）
- 处理动态加载内容
- 需要执行JavaScript代码
- 处理复杂的验证码或登录流程

```python
# d模式示例：处理动态加载内容
page = WebPage(mode='d')
page.get('https://example.com/infinite-scroll')

# 滚动加载更多内容
for _ in range(5):
    page.scroll.down(800)  # 向下滚动
    page.wait(1)  # 等待内容加载

# 获取所有加载的项目
items = page.eles('.item')
print(f'加载了{len(items)}个项目')
```

### 组合使用两种模式

WebPage 的强大之处在于可以组合使用两种模式，充分利用各自的优势：

```python
# 组合使用示例：登录后爬取数据
page = WebPage()

# 使用d模式处理登录（支持JavaScript）
page.get('https://example.com/login')
page.ele('#username').input('user123')
page.ele('#password').input('password123')
page.ele('#login-button').click()

# 等待登录成功
page.wait.ele_appear('#user-dashboard', timeout=10)
print('登录成功')

# 切换到s模式爬取数据（更高效）
page.change_mode('s')

# 爬取多个页面的数据
results = []
for i in range(1, 11):
    # 获取列表页
    page.get(f'https://example.com/data?page={i}')
    
    # 提取数据
    for item in page.eles('.data-item'):
        item_data = {
            'title': item.ele('.title').text,
            'price': item.ele('.price').text,
            'desc': item.ele('.description').text
        }
        results.append(item_data)
    
    print(f'已爬取第{i}页数据')

print(f'总共爬取{len(results)}条数据')
```

## 数据共享与同步

### Cookies 同步

```python
# 在两种模式间同步 Cookies
page = WebPage(mode='d')
page.get('https://example.com')

# 在浏览器中设置 Cookie
page.run_js('document.cookie = "test_cookie=value123; path=/"')

# 切换到s模式，Cookie会自动同步
page.change_mode('s')

# 验证Cookie已同步
cookie_value = page.get_cookie('test_cookie')
print(f'Cookie值: {cookie_value}')  # 'value123'

# 在s模式下修改Cookie
page.set_cookies({'new_cookie': 'new_value'})

# 切换回d模式，新Cookie也会同步
page.change_mode('d')
cookie_value = page.get_cookie('new_cookie')
print(f'新Cookie值: {cookie_value}')  # 'new_value'
```

### LocalStorage 和 SessionStorage 同步

```python
# 仅在d模式下可以操作存储，但会在切换时同步
page = WebPage(mode='d')
page.get('https://example.com')

# 设置本地存储
page.run_js('localStorage.setItem("userPreference", "darkMode")')

# 切换到s模式（存储信息会保留）
page.change_mode('s')

# 执行一些s模式操作
page.get('https://example.com/api/settings')

# 切换回d模式，验证存储是否保留
page.change_mode('d')
storage_value = page.run_js('return localStorage.getItem("userPreference")')
print(f'存储值: {storage_value}')  # 'darkMode'
```

## 高级用法

### 自定义模式切换逻辑

```python
def smart_mode_switch(page, url):
    """根据URL自动选择合适的模式"""
    # API接口使用s模式
    if '/api/' in url or '/data/' in url:
        if page.mode != 's':
            page.change_mode('s')
    # 交互页面使用d模式
    elif '/dashboard/' in url or '/interactive/' in url:
        if page.mode != 'd':
            page.change_mode('d')
    
    # 访问URL
    page.get(url)
    return page

# 使用
page = WebPage()
smart_mode_switch(page, 'https://example.com/api/data')  # s模式
smart_mode_switch(page, 'https://example.com/dashboard')  # d模式
```

### 处理需要验证码的场景

```python
# 组合使用：s模式提交表单，d模式处理验证码
page = WebPage(mode='s')

# 使用s模式获取登录页面（更快）
page.get('https://example.com/login')

# 检查是否有验证码
if page.ele('#captcha-img'):
    # 切换到d模式处理验证码
    page.change_mode('d')
    
    # 重新加载页面（确保验证码正确显示）
    page.refresh()
    
    # 截取验证码图片
    captcha = page.ele('#captcha-img')
    captcha.screenshot('captcha.png')
    
    # 手动输入验证码
    code = input('请输入验证码: ')
    
    # 填写表单并提交
    page.ele('#username').input('user123')
    page.ele('#password').input('password123')
    page.ele('#captcha-input').input(code)
    page.ele('#login-button').click()
else:
    # 没有验证码，使用s模式直接提交表单
    form_data = {
        'username': 'user123',
        'password': 'password123'
    }
    page.post('https://example.com/login', data=form_data)

# 验证登录结果
if 'welcome' in page.html or page.ele('#user-profile'):
    print('登录成功')
else:
    print('登录失败')
```

### 处理动态页面内容提取

```python
def extract_data(page, url, is_dynamic=False):
    """根据页面是否动态选择合适的模式提取数据"""
    # 根据是否需要动态渲染选择模式
    if is_dynamic and page.mode != 'd':
        page.change_mode('d')
    elif not is_dynamic and page.mode != 's':
        page.change_mode('s')
    
    # 访问页面
    page.get(url)
    
    # 如果是动态页面，等待内容加载
    if is_dynamic:
        page.wait.load_complete()
        # 等待特定内容出现
        page.wait.ele_appear('.content-loaded', timeout=10)
    
    # 提取数据
    data = []
    for item in page.eles('.item'):
        item_data = {
            'title': item.ele('.title').text,
            'content': item.ele('.content').text
        }
        data.append(item_data)
    
    return data

# 使用示例
page = WebPage()
# 静态页面使用s模式提取
static_data = extract_data(page, 'https://example.com/static-page', is_dynamic=False)
# 动态页面使用d模式提取
dynamic_data = extract_data(page, 'https://example.com/dynamic-page', is_dynamic=True)
```

## 实用案例

### 登录后数据爬取

```python
from DrissionPage import WebPage
import csv
import time

def login_and_scrape(username, password, pages=5):
    """登录网站并爬取多页数据"""
    page = WebPage()
    
    try:
        # 1. 使用d模式处理登录
        page.get('https://example.com/login')
        
        # 填写登录表单
        page.ele('#username').input(username)
        page.ele('#password').input(password)
        page.ele('#login-button').click()
        
        # 等待登录成功
        page.wait.ele_appear('#dashboard', timeout=10)
        print('登录成功')
        
        # 2. 切换到s模式加速数据爬取
        page.change_mode('s')
        
        # 准备保存数据
        with open('data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['标题', '价格', '评分', '链接'])
            
            # 爬取多页数据
            for i in range(1, pages + 1):
                print(f'正在爬取第{i}页...')
                page.get(f'https://example.com/products?page={i}')
                
                # 提取产品数据
                products = page.eles('.product-item')
                for product in products:
                    title = product.ele('.title').text
                    price = product.ele('.price').text
                    rating = product.ele('.rating').attr('data-score')
                    link = product.ele('a.details').attr('href')
                    
                    writer.writerow([title, price, rating, link])
                
                print(f'第{i}页爬取完成')
                
                # 适当延迟，避免请求过快
                time.sleep(1)
        
        print(f'爬取完成，数据已保存到 data.csv')
        
    except Exception as e:
        print(f'爬取过程中发生错误: {e}')
    
    finally:
        page.close()

# 使用示例
login_and_scrape('user123', 'password123', pages=10)
```

### 处理既有API又有复杂交互的网站

```python
from DrissionPage import WebPage

def process_website():
    """处理既有API又有复杂交互的网站"""
    page = WebPage()
    
    # 1. 使用d模式登录
    page.get('https://example.com/login')
    page.ele('#username').input('user123')
    page.ele('#password').input('password123')
    page.ele('#login-button').click()
    
    # 等待登录成功
    page.wait.ele_appear('#dashboard', timeout=10)
    
    # 2. 使用s模式获取API数据
    page.change_mode('s')
    
    # 获取用户配置
    user_config = page.get('https://example.com/api/user/config').json
    print(f"用户配置: {user_config['preferences']}")
    
    # 获取产品列表
    products = page.get('https://example.com/api/products').json
    product_ids = [product['id'] for product in products['items']]
    
    # 3. 切换回d模式进行复杂交互
    page.change_mode('d')
    
    # 打开产品编辑页面
    page.get('https://example.com/products/manage')
    
    # 对每个产品进行操作
    for product_id in product_ids[:5]:  # 处理前5个产品
        # 打开编辑界面
        page.ele(f'#edit-{product_id}').click()
        
        # 等待编辑表单加载
        page.wait.ele_appear('#product-form', timeout=5)
        
        # 修改产品信息
        page.ele('#product-price').input('99.99', clear=True)
        page.ele('#product-stock').input('100', clear=True)
        
        # 保存更改
        page.ele('#save-button').click()
        
        # 等待保存成功
        page.wait.text_appear('保存成功', timeout=5)
        
        # 返回产品列表
        page.ele('#back-button').click()
        page.wait.ele_appear('#products-table', timeout=5)
    
    print('产品更新完成')
    
    # 4. 再次使用s模式验证API更改结果
    page.change_mode('s')
    updated_products = page.get('https://example.com/api/products').json
    
    # 打印更新后的价格
    for product in updated_products['items'][:5]:
        print(f"产品 {product['id']} - 更新后价格: {product['price']}")
    
    page.close()

# 使用
process_website()
```

## 小结

WebPage 通过结合 SessionPage 和 ChromiumPage 的功能，提供了极大的灵活性，使你能够在同一个自动化流程中根据需要选择最合适的模式。主要优势包括：

1. **最佳性能**：可以在轻量级任务中使用s模式节省资源，在需要复杂交互时切换到d模式
2. **数据同步**：两种模式间自动同步cookies、本地存储等状态
3. **统一API**：无论使用哪种模式，API保持一致，降低学习成本
4. **场景适应**：可以根据不同的自动化场景选择最合适的工作模式

合理利用 WebPage 的双模式特性，可以开发出既高效又功能强大的网页自动化脚本，满足从简单数据爬取到复杂交互模拟的各种需求。

在下一章中，我们将深入探讨高级元素查找技术，学习如何在复杂的网页结构中精确定位所需元素。 