# SessionPage 详解

SessionPage 是 DrissionPage 中的三大页面对象之一，主要基于 requests 库实现，专注于数据包收发、表单提交和数据解析功能。与浏览器模式相比，SessionPage 具有启动快、资源占用少的优势，适合批量数据采集、接口测试等场景。

## SessionPage 概述

### 特点与优势

- **轻量级**：无需启动浏览器，资源消耗小
- **高效**：收发数据包速度快，适合大规模数据获取
- **低调**：不易被网站检测为爬虫（相比浏览器）
- **简洁**：API 设计与 ChromiumPage 保持一致，易于使用

### 适用场景

- 数据爬取和采集
- API 接口测试
- 简单表单提交
- 无需渲染 JavaScript 的网页操作

## 创建 SessionPage 对象

### 基本创建方式

```python
from DrissionPage import SessionPage

# 创建默认 SessionPage 对象
page = SessionPage()
```

### 使用配置文件创建

```python
# 使用指定配置文件创建
page = SessionPage(crx_or_path='config.ini')

# 或者从默认位置读取配置
page = SessionPage(read_file=True)
```

### 自定义会话参数

```python
# 自定义创建，可设置代理等参数
page = SessionPage(proxy='http://127.0.0.1:7890', timeout=10)

# 使用更多自定义参数
page = SessionPage(
    proxy='http://127.0.0.1:7890', 
    timeout=10,
    headers={'User-Agent': 'Custom User Agent'},
    cookies={'session_id': '123456'}
)
```

## 页面请求与导航

### 打开网页

```python
# 使用 get 方法打开网页
page.get('https://www.example.com')

# 设置超时时间
page.get('https://www.example.com', timeout=10)

# 添加查询参数
page.get('https://www.example.com/search', params={'q': 'python'})
```

### 发送 POST 请求

```python
# 基本 POST 请求
page.post('https://api.example.com/submit', data={'key': 'value'})

# 发送 JSON 数据
page.post('https://api.example.com/submit', json={'key': 'value'})

# 上传文件
page.post('https://api.example.com/upload', 
          files={'file': open('example.txt', 'rb')})
```

### 其他 HTTP 方法

```python
# PUT 请求
page.put('https://api.example.com/update', data={'key': 'new_value'})

# DELETE 请求
page.delete('https://api.example.com/remove/123')

# 自定义请求
page.request('PATCH', 'https://api.example.com/patch', 
             json={'field': 'value'})
```

## 处理响应数据

### 获取页面内容

```python
# 获取 HTML 文本
html = page.html

# 获取 JSON 响应
json_data = page.json

# 获取二进制内容
binary_data = page.content
```

### 获取响应信息

```python
# 获取响应状态码
status_code = page.status_code
print(f'状态码: {status_code}')

# 获取响应头信息
headers = page.response_headers
print(f'Content-Type: {headers.get("Content-Type")}')

# 获取请求 URL
url = page.url
print(f'当前 URL: {url}')
```

## 会话管理

### Cookies 操作

```python
# 获取当前所有 cookies
cookies = page.cookies
print(cookies)

# 获取特定 cookie
session_id = page.get_cookie('session_id')
print(f'Session ID: {session_id}')

# 设置 cookie
page.set_cookies({'user_id': '12345'})

# 保存 cookies 到文件
page.save_cookies('cookies.json')

# 从文件加载 cookies
page.load_cookies('cookies.json')
```

### 请求头管理

```python
# 获取当前请求头
headers = page.headers
print(headers)

# 设置新的请求头
page.set_headers({'User-Agent': 'Mozilla/5.0 ...'})

# 添加单个请求头
page.add_headers({'Referer': 'https://www.example.com'})
```

## 元素查找与操作

SessionPage 也支持类似于浏览器模式的元素查找和操作功能，但基于静态 HTML 解析。

### 元素查找

```python
# 通过 CSS 选择器查找元素
element = page.ele('#main-content')

# 通过 XPath 查找元素
element = page.ele('xpath://div[@class="article"]')

# 通过文本查找元素
element = page.ele('@text=登录')

# 查找所有匹配元素
elements = page.eles('.item')
```

### 元素信息获取

```python
# 获取元素文本
text = element.text
print(f'元素文本: {text}')

# 获取属性值
href = element.attr('href')
print(f'链接地址: {href}')

# 获取 HTML
html = element.html
print(f'元素 HTML: {html}')
```

### 表单操作

虽然 SessionPage 不能像浏览器一样实时交互，但可以通过解析和构建表单数据实现表单提交。

```python
# 找到表单元素
form = page.ele('form#login')

# 获取表单字段
form_data = {}
for input_ele in form.eles('input'):
    name = input_ele.attr('name')
    if name:
        form_data[name] = input_ele.attr('value') or ''

# 更新表单数据
form_data['username'] = 'user123'
form_data['password'] = 'pass123'

# 获取表单提交地址
action = form.attr('action') or page.url
method = form.attr('method') or 'post'

# 提交表单
if method.lower() == 'post':
    page.post(action, data=form_data)
else:
    page.get(action, params=form_data)
```

## 高级功能

### 会话克隆与共享

```python
# 克隆当前会话创建新页面
new_page = page.clone()

# 使用相同会话创建新页面（共享cookies等状态）
same_session_page = SessionPage(session=page.session)
```

### 设置代理

```python
# 设置 HTTP 代理
page.set.proxy('http://127.0.0.1:7890')

# 设置 SOCKS 代理
page.set.proxy('socks5://127.0.0.1:1080')

# 移除代理
page.set.proxy(None)
```

### 处理重定向

```python
# 允许自动重定向（默认）
page.get('https://example.com/redirect', allow_redirects=True)

# 禁止自动重定向
page.get('https://example.com/redirect', allow_redirects=False)

# 获取重定向历史
history = page.history
for resp in history:
    print(f'重定向: {resp.url} -> {resp.status_code}')
```

### 会话重连

```python
# 重新创建会话（保留cookies等信息）
page.reconnect()

# 完全重置会话（包括cookies）
page.reset()
```

## SessionPage vs. ChromiumPage

两种模式有各自的优缺点，下面是简单对比：

| 特性 | SessionPage | ChromiumPage |
|------|-------------|--------------|
| 启动速度 | 快 | 慢 |
| 资源占用 | 低 | 高 |
| JavaScript执行 | 不支持 | 支持 |
| 元素交互 | 基础支持 | 完全支持 |
| 反爬能力 | 较弱 | 较强 |
| 数据处理速度 | 快 | 慢 |
| 适用场景 | 数据抓取、接口测试 | 复杂网页交互、自动化测试 |

## 实用技巧

### 处理 AJAX 数据

对于需要 JavaScript 加载的数据，可以直接请求接口：

```python
# 先访问页面
page.get('https://example.com/products')

# 分析后找到 AJAX 接口地址
api_url = 'https://example.com/api/products'

# 构建请求参数
params = {
    'page': 1,
    'size': 20,
    'sort': 'popular'
}

# 提取必要的认证信息（如果有）
token = page.ele('meta[name="csrf-token"]').attr('content')

# 设置必要的头信息
page.add_headers({
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': page.url,
    'X-CSRF-Token': token
})

# 发送 API 请求获取数据
page.get(api_url, params=params)
data = page.json
print(f'获取到{len(data["items"])}个产品')
```

### 处理防盗链

处理图片等资源的防盗链保护：

```python
# 访问页面
page.get('https://example.com/gallery')

# 设置 Referer 头以通过防盗链检查
img_url = 'https://example.com/images/protected.jpg'
page.add_headers({'Referer': 'https://example.com/gallery'})

# 下载图片
page.get(img_url)
with open('image.jpg', 'wb') as f:
    f.write(page.content)
```

### 批量并行请求

使用多个 SessionPage 实例可以实现并行请求：

```python
import concurrent.futures

urls = [f'https://api.example.com/items/{i}' for i in range(1, 101)]
results = []

def fetch_url(url):
    page = SessionPage()
    page.get(url)
    return page.json

# 使用线程池并行请求
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_url, urls))

print(f'获取了 {len(results)} 条数据')
```

## 小结

SessionPage 提供了高效、轻量级的网页操作方式，特别适合批量数据采集和接口测试场景。它与 ChromiumPage 共享相似的 API 设计，使得在两种模式之间切换变得简单。通过合理利用 SessionPage 的特性，可以显著提升自动化脚本的性能和效率。

在下一章中，我们将详细介绍 ChromiumPage 的高级功能，展示如何在需要完整浏览器环境的场景下进行自动化操作。 