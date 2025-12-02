# 网络监听与拦截

在网页自动化和爬虫任务中，监控和分析网络请求是非常重要的功能。DrissionPage 提供了强大的网络监听和请求拦截功能，使您能够捕获、分析和修改浏览器与服务器之间的通信。本教程将详细介绍如何使用这些功能来实现更高级的自动化任务。

## 网络监听基础

网络监听允许您捕获浏览器与服务器之间的所有通信，包括 HTTP 请求、响应、WebSocket 通信等。这对于以下场景非常有用：

1. 分析 AJAX 请求以获取数据来源
2. 监控 API 调用以了解网页运行机制
3. 调试网络问题
4. 提取隐藏在 XHR 请求中的数据

### 开启网络监听

在 ChromiumPage 中，您可以使用 `listen_requests` 方法开启网络监听：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
# 开启网络请求监听
page.listen_requests(True)
# 访问网页
page.get('https://example.com')
```

### 获取请求记录

一旦启用了网络监听，您可以使用以下方法获取捕获的请求记录：

```python
# 获取所有请求记录
all_requests = page.get_requests()

# 获取特定 URL 的请求记录
api_requests = page.get_requests(url_contains='api')

# 获取特定类型的请求记录
xhr_requests = page.get_requests(type='xhr')
```

### 过滤请求记录

`get_requests` 方法支持多种过滤条件：

```python
# 按 URL 过滤
requests = page.get_requests(url_contains='api/data')

# 按请求方法过滤
post_requests = page.get_requests(method='POST')

# 按资源类型过滤
img_requests = page.get_requests(type='image')

# 按状态码过滤
success_requests = page.get_requests(status_code=200)

# 组合过滤条件
api_post_requests = page.get_requests(url_contains='api', method='POST')
```

### 分析请求记录

每个请求记录包含丰富的信息，您可以提取这些信息进行分析：

```python
# 获取最近的 XHR 请求
requests = page.get_requests(type='xhr')
if requests:
    latest_req = requests[-1]
    
    # 请求信息
    print(f"URL: {latest_req.url}")
    print(f"方法: {latest_req.method}")
    print(f"请求头: {latest_req.request_headers}")
    print(f"请求体: {latest_req.request_body}")
    
    # 响应信息
    print(f"状态码: {latest_req.status_code}")
    print(f"响应头: {latest_req.response_headers}")
    print(f"响应体: {latest_req.response_body}")
```

### 等待特定请求完成

在某些场景中，您可能需要等待特定请求完成后再继续操作：

```python
# 等待特定 API 请求完成
page.get('https://example.com/data-page')
# 触发某个操作导致 AJAX 请求
page.ele('#load-data-button').click()
# 等待 API 请求完成
page.wait.requests_completed(url_contains='api/data')
```

## 请求拦截

请求拦截允许您修改或阻止浏览器发出的请求，这对于以下场景非常有用：

1. 阻止不必要的资源加载（如广告、图片等）以提高性能
2. 修改请求参数、头信息等以突破某些限制
3. 模拟特定的网络条件或错误情况
4. 在请求发送前注入自定义数据

### 设置请求拦截器

要使用请求拦截功能，您需要定义拦截器函数并注册到页面对象：

```python
from DrissionPage import ChromiumPage

# 定义拦截器函数
def request_interceptor(request):
    # 阻止图片加载
    if request.resource_type == 'image':
        request.abort()
    # 修改请求头
    elif 'api' in request.url:
        headers = request.headers
        headers['Custom-Header'] = 'MyValue'
        request.continue_(headers=headers)
    # 其他请求正常发送
    else:
        request.continue_()

# 创建页面对象并设置拦截器
page = ChromiumPage()
page.set_request_interceptor(request_interceptor)
# 开启请求拦截
page.enable_request_intercept(True)
```

在拦截器函数中，您可以针对每个请求执行以下操作：

- `request.continue_()`：允许请求正常发送
- `request.continue_(headers=new_headers)`：修改请求头后发送
- `request.continue_(body=new_body)`：修改请求体后发送
- `request.abort()`：阻止请求发送
- `request.respond()`：直接提供响应，不发送实际请求

### 阻止特定资源加载

以下示例展示如何阻止加载图片和广告资源：

```python
from DrissionPage import ChromiumPage

def blocker(request):
    # 阻止图片加载
    if request.resource_type == 'image':
        request.abort()
    # 阻止广告脚本
    elif 'ads' in request.url or 'analytics' in request.url:
        request.abort()
    # 允许其他请求
    else:
        request.continue_()

page = ChromiumPage()
page.set_request_interceptor(blocker)
page.enable_request_intercept(True)
page.get('https://example.com')
```

### 修改请求头和请求参数

以下示例展示如何修改请求头和查询参数：

```python
from DrissionPage import ChromiumPage
import json
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def modifier(request):
    # 修改 API 请求的头信息和参数
    if 'api' in request.url:
        # 修改请求头
        headers = request.headers
        headers['User-Agent'] = 'Custom User Agent'
        headers['Authorization'] = 'Bearer my-token'
        
        # 修改 URL 查询参数
        parsed_url = urlparse(request.url)
        query_params = parse_qs(parsed_url.query)
        
        # 添加或修改参数
        query_params['limit'] = ['50']
        query_params['custom_param'] = ['custom_value']
        
        # 重建 URL
        new_query = urlencode(query_params, doseq=True)
        new_url = urlunparse(
            (parsed_url.scheme, parsed_url.netloc, parsed_url.path, 
             parsed_url.params, new_query, parsed_url.fragment)
        )
        
        # 修改 POST 请求的请求体
        if request.method == 'POST' and request.post_data:
            try:
                body = json.loads(request.post_data)
                body['additional_field'] = 'value'
                new_body = json.dumps(body)
                request.continue_(url=new_url, headers=headers, body=new_body)
                return
            except:
                pass
        
        # 对于其他请求，只修改 URL 和头信息
        request.continue_(url=new_url, headers=headers)
    else:
        request.continue_()

page = ChromiumPage()
page.set_request_interceptor(modifier)
page.enable_request_intercept(True)
page.get('https://example.com')
```

### 模拟响应

在某些情况下，您可能希望直接提供响应而不是发送实际请求，这可以用于测试或绕过某些限制：

```python
from DrissionPage import ChromiumPage

def mock_response(request):
    # 模拟 API 响应
    if '/api/data' in request.url:
        # 创建模拟响应内容
        mock_data = {
            'status': 'success',
            'data': [
                {'id': 1, 'name': 'Item 1'},
                {'id': 2, 'name': 'Item 2'},
                {'id': 3, 'name': 'Item 3'}
            ]
        }
        
        # 设置响应头
        response_headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        
        # 提供模拟响应
        request.respond(
            status=200,
            headers=response_headers,
            body=json.dumps(mock_data)
        )
    else:
        # 其他请求正常发送
        request.continue_()

page = ChromiumPage()
page.set_request_interceptor(mock_response)
page.enable_request_intercept(True)
page.get('https://example.com')
```

## 高级应用场景

### 提取 API 数据

监听网络请求是一种提取数据的有效方法，特别是对于使用 AJAX 加载数据的网站：

```python
from DrissionPage import ChromiumPage
import json
import time

# 创建页面对象
page = ChromiumPage()
# 开启请求监听
page.listen_requests(True)

# 访问目标页面
page.get('https://example.com/data-page')

# 点击加载数据按钮
page.ele('#load-data-button').click()

# 等待数据加载完成
time.sleep(2)  # 简单等待，也可以使用 wait.requests_completed

# 获取 API 请求
api_requests = page.get_requests(url_contains='/api/data')

# 从响应中提取数据
data_list = []
for req in api_requests:
    if req.status_code == 200 and req.response_body:
        try:
            response_data = json.loads(req.response_body)
            if 'data' in response_data:
                data_list.extend(response_data['data'])
        except:
            pass

# 使用提取的数据
for item in data_list:
    print(f"Item: {item}")
```

### 监控 WebSocket 通信

DrissionPage 也支持监听 WebSocket 通信，这对于分析实时更新的网站非常有用：

```python
from DrissionPage import ChromiumPage
import time
import json

page = ChromiumPage()
# 开启 WebSocket 监听
page.listen_websockets(True)

# 访问使用 WebSocket 的页面
page.get('https://example.com/realtime-page')

# 等待一段时间收集消息
time.sleep(10)

# 获取 WebSocket 消息
ws_messages = page.get_websocket_messages()
for msg in ws_messages:
    print(f"方向: {'发送' if msg.is_sent else '接收'}")
    try:
        data = json.loads(msg.data)
        print(f"消息内容: {data}")
    except:
        print(f"原始消息: {msg.data}")
```

### 分析页面性能

网络监听也可以用于分析页面性能，帮助识别加载缓慢的资源：

```python
from DrissionPage import ChromiumPage
import time

page = ChromiumPage()
page.listen_requests(True)

# 记录加载开始时间
start_time = time.time()

# 加载页面
page.get('https://example.com')

# 获取所有请求
all_requests = page.get_requests()

# 计算总加载时间
total_load_time = time.time() - start_time
print(f"总加载时间: {total_load_time:.2f} 秒")
print(f"请求总数: {len(all_requests)}")

# 按资源类型统计
resource_types = {}
for req in all_requests:
    res_type = req.resource_type
    if res_type not in resource_types:
        resource_types[res_type] = 0
    resource_types[res_type] += 1

for res_type, count in resource_types.items():
    print(f"{res_type}: {count} 个请求")

# 找出耗时最长的请求
slowest_requests = sorted(
    all_requests, 
    key=lambda x: (x.response_received_time or 0) - (x.sent_time or 0),
    reverse=True
)

print("\n耗时最长的5个请求:")
for i, req in enumerate(slowest_requests[:5]):
    if req.sent_time and req.response_received_time:
        duration = req.response_received_time - req.sent_time
        print(f"{i+1}. {req.url} - {duration:.2f}秒")
```

### 自动化测试中的网络监控

在自动化测试中，监控网络请求可以帮助验证应用程序的行为：

```python
from DrissionPage import ChromiumPage

def test_api_calls():
    page = ChromiumPage()
    page.listen_requests(True)
    
    # 执行测试场景
    page.get('https://example.com/app')
    page.ele('#login-button').click()
    
    # 验证登录 API 被调用
    login_requests = page.get_requests(url_contains='/api/login')
    assert len(login_requests) > 0, "登录 API 未被调用"
    assert login_requests[-1].status_code == 200, "登录 API 返回错误状态码"
    
    # 验证用户数据 API 被调用
    user_data_requests = page.get_requests(url_contains='/api/user-data')
    assert len(user_data_requests) > 0, "用户数据 API 未被调用"
    
    # 验证没有错误请求
    error_requests = page.get_requests(status_code_gte=400)
    assert len(error_requests) == 0, f"发现 {len(error_requests)} 个错误请求"
    
    print("所有网络请求测试通过!")

# 运行测试
test_api_calls()
```

## 实战案例：监控和拦截商品价格 API

以下是一个完整的实战案例，展示如何监控商品价格 API 并提取产品信息：

```python
from DrissionPage import ChromiumPage
import json
import csv
import time

# 创建页面对象
page = ChromiumPage()

# 定义请求拦截器，添加自定义请求头以绕过反爬措施
def add_custom_headers(request):
    if 'api/products' in request.url:
        headers = request.headers
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        headers['Referer'] = 'https://example.com/products'
        request.continue_(headers=headers)
    else:
        request.continue_()

# 设置拦截器并开启网络监听
page.set_request_interceptor(add_custom_headers)
page.enable_request_intercept(True)
page.listen_requests(True)

# 访问产品页面
page.get('https://example.com/products')

# 模拟用户行为：筛选产品
page.ele('#category-dropdown').click()
page.ele('text=Electronics').click()
page.ele('#apply-filter').click()

# 等待 API 请求完成
page.wait.requests_completed(url_contains='api/products')

# 提取产品数据
product_requests = page.get_requests(url_contains='api/products')
products = []

for req in product_requests:
    if req.status_code == 200 and req.response_body:
        try:
            response_data = json.loads(req.response_body)
            if 'products' in response_data:
                for product in response_data['products']:
                    products.append({
                        'id': product.get('id'),
                        'name': product.get('name'),
                        'price': product.get('price'),
                        'currency': product.get('currency'),
                        'availability': product.get('in_stock', False),
                        'rating': product.get('rating', 0),
                        'url': product.get('url')
                    })
        except Exception as e:
            print(f"解析产品数据时出错: {e}")

# 保存产品数据到 CSV 文件
if products:
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)
    print(f"已保存 {len(products)} 个产品信息到 products.csv")
else:
    print("未找到产品信息")

# 检查价格变化（模拟）
def check_price_changes():
    page.get('https://example.com/products/1')
    
    # 清除之前的请求记录
    page.clear_requests()
    
    # 模拟刷新价格
    page.ele('#refresh-price').click()
    
    # 等待价格 API 请求完成
    page.wait.requests_completed(url_contains='api/price')
    
    # 获取价格请求
    price_requests = page.get_requests(url_contains='api/price')
    if price_requests:
        latest_req = price_requests[-1]
        if latest_req.status_code == 200 and latest_req.response_body:
            try:
                price_data = json.loads(latest_req.response_body)
                print(f"当前价格: {price_data.get('current_price')} {price_data.get('currency')}")
                print(f"原价: {price_data.get('original_price')} {price_data.get('currency')}")
                print(f"折扣: {price_data.get('discount_percentage')}%")
            except Exception as e:
                print(f"解析价格数据时出错: {e}")

# 检查价格变化
check_price_changes()

# 关闭浏览器
page.quit()
```

## 总结

DrissionPage 的网络监听和拦截功能为网页自动化和爬虫任务提供了强大的工具。通过这些功能，您可以：

1. **监听网络请求**：捕获并分析浏览器与服务器之间的通信，提取 API 数据。
2. **过滤请求记录**：根据 URL、方法、资源类型等条件筛选请求。
3. **拦截并修改请求**：修改请求头、参数，甚至直接提供模拟响应。
4. **阻止不必要的资源**：提高页面加载速度和减少资源消耗。
5. **监控页面性能**：分析请求耗时，找出性能瓶颈。

这些功能在数据提取、自动化测试、性能分析等场景中非常有用。通过合理利用这些功能，您可以实现更高效、更智能的网页自动化任务。 