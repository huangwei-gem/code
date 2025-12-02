# 网络请求监听

在网页自动化和爬虫开发中，监听和分析网络请求是一项重要能力。DrissionPage 提供了强大的网络监听功能，可以捕获、分析和操作页面产生的各种网络请求。本章将介绍如何使用 DrissionPage 的网络监听功能来处理各种网络请求场景。

## 网络监听基础

### 网络监听的用途

网络监听在自动化中有多种重要用途：

1. **提取数据源** - 直接获取 API 数据，绕过复杂的页面解析
2. **监控网络活动** - 跟踪页面加载过程中的网络请求
3. **性能分析** - 分析请求响应时间和资源加载顺序
4. **拦截和修改** - 修改请求或响应内容
5. **自动化调试** - 识别和解决网络相关问题

### 开启网络监听

```python
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 开启网络监听
page.listen.start()

# 访问目标网页
page.get('https://example.com')

# 执行可能触发网络请求的操作
page.ele('#search-button').click()

# 停止监听
page.listen.stop()

# 查看捕获的请求
requests = page.listen.requests
for req in requests:
    print(f"URL: {req.url}")
    print(f"方法: {req.method}")
    print(f"类型: {req.type}")
    print('-' * 50)
```

### 基本监听配置

```python
# 在开启监听时配置过滤条件
page.listen.start(
    types=['XHR', 'Fetch'],  # 只监听XHR和Fetch请求
    urls=['api', '.json'],    # 只监听URL包含api或.json的请求
    exclude=['image', 'font']  # 排除URL中包含image或font的请求
)

# 也可以单独设置监听选项
page.listen.types = ['XHR']  # 只监听XHR请求
page.listen.urls = ['api/data']  # 只监听包含api/data的URL
page.listen.exclude = ['thumbnail']  # 排除包含thumbnail的URL
```

## 请求分析与处理

### 获取请求信息

```python
# 开启监听并访问页面
page.listen.start()
page.get('https://example.com/data-page')

# 获取所有捕获的请求
all_requests = page.listen.requests

# 获取最后一个请求
last_request = page.listen.latest

# 按URL查找特定请求
api_requests = page.listen.find('api/products')

# 按请求类型筛选
xhr_requests = [req for req in all_requests if req.type == 'XHR']

# 获取请求详细信息
for req in xhr_requests[:3]:  # 只查看前3个XHR请求
    print(f"URL: {req.url}")
    print(f"方法: {req.method}")
    print(f"请求头: {req.req_headers}")
    
    if req.method == 'POST':
        print(f"请求体: {req.req_data}")
    
    print(f"状态码: {req.status_code}")
    print(f"响应头: {req.resp_headers}")
    print(f"响应体: {req.response[:100]}...")  # 只打印前100个字符
    print('-' * 50)
```

### 等待特定请求

```python
# 开启监听
page.listen.start()

# 点击触发请求的按钮
page.ele('#load-data-btn').click()

# 等待特定请求完成
api_req = page.listen.wait('/api/data', timeout=10)

if api_req:
    print(f"API请求已完成，状态码: {api_req.status_code}")
    data = api_req.json  # 如果响应是JSON格式
    print(f"获取到的数据: {data}")
else:
    print("等待超时，未捕获到目标请求")
```

### 提取JSON数据

许多现代网站通过 API 返回 JSON 数据，可以直接提取这些数据：

```python
# 开启监听
page.listen.start(types=['XHR'])  # 只监听XHR请求

# 触发数据加载
page.ele('#fetch-data').click()

# 等待数据API请求
data_req = page.listen.wait('api/data')

# 解析JSON响应
if data_req and data_req.status_code == 200:
    json_data = data_req.json  # 自动解析JSON
    
    # 处理数据
    if 'items' in json_data:
        for item in json_data['items']:
            print(f"ID: {item['id']}, 名称: {item['name']}")
```

### 处理分页请求

对于分页数据，可以监听并收集多个请求的响应：

```python
from DrissionPage import ChromiumPage
import time
import json

def collect_paginated_data(url, max_pages=5):
    page = ChromiumPage()
    combined_data = []
    
    # 访问页面
    page.get(url)
    
    # 开启监听
    page.listen.start(types=['XHR'], urls=['api/items'])
    
    # 处理每一页
    for i in range(max_pages):
        print(f"处理第 {i+1} 页...")
        
        # 如果不是第一页，点击下一页按钮
        if i > 0:
            next_btn = page.ele('#next-page')
            if not next_btn or not next_btn.is_enabled():
                print("没有更多页面")
                break
            next_btn.click()
        
        # 等待API请求
        data_req = page.listen.wait('api/items', timeout=10)
        
        if not data_req or data_req.status_code != 200:
            print(f"第 {i+1} 页请求失败")
            continue
        
        # 提取数据
        try:
            page_data = data_req.json
            items = page_data.get('items', [])
            combined_data.extend(items)
            print(f"已提取 {len(items)} 条数据")
            
            # 检查是否是最后一页
            if page_data.get('isLastPage', False):
                print("已到达最后一页")
                break
                
            # 轻微延迟，避免请求过于频繁
            time.sleep(1)
            
        except Exception as e:
            print(f"解析数据出错: {str(e)}")
    
    page.close()
    print(f"总共收集了 {len(combined_data)} 条数据")
    return combined_data

# 使用函数收集分页数据
all_data = collect_paginated_data('https://example.com/paginated-data')

# 将收集的数据保存到文件
with open('collected_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
```

## 请求拦截与修改

### 拦截和修改请求

DrissionPage 允许拦截和修改请求，这对于模拟特定行为或绕过某些限制非常有用：

```python
from DrissionPage import ChromiumPage

# 创建页面
page = ChromiumPage()

# 设置请求拦截器
@page.listen.interceptor
def modify_request(request):
    # 只修改特定API请求
    if 'api/user' in request.url:
        # 修改请求头
        request.req_headers['X-Custom-Header'] = 'Modified'
        
        # 如果是POST请求，可以修改请求体
        if request.method == 'POST':
            data = request.req_json  # 获取JSON格式的请求体
            if data:
                # 修改数据
                data['customField'] = 'custom_value'
                # 更新请求体
                request.req_json = data
    
    # 继续请求
    request.continue_()

# 访问页面
page.get('https://example.com')

# 执行可能触发请求的操作
page.ele('#user-action').click()
```

### 模拟响应

有时需要拦截请求并返回自定义响应，特别是在测试场景中：

```python
@page.listen.interceptor
def mock_response(request):
    # 拦截特定API请求并返回模拟数据
    if 'api/products' in request.url:
        # 创建模拟响应数据
        mock_data = {
            'products': [
                {'id': 1, 'name': '模拟产品1', 'price': 99.99},
                {'id': 2, 'name': '模拟产品2', 'price': 199.99}
            ],
            'total': 2,
            'page': 1,
            'pageSize': 10
        }
        
        # 返回模拟响应
        request.respond(
            status_code=200,
            headers={'Content-Type': 'application/json'},
            body=json.dumps(mock_data)
        )
    else:
        # 对其他请求正常处理
        request.continue_()
```

### 阻止特定请求

可以选择性地阻止某些请求，例如阻止广告或追踪请求：

```python
@page.listen.interceptor
def block_ads(request):
    # 广告和追踪相关URL的关键词列表
    ad_keywords = ['ads', 'analytics', 'tracker', 'pixel', 'banner']
    
    # 检查请求URL是否包含广告关键词
    if any(keyword in request.url.lower() for keyword in ad_keywords):
        print(f"已阻止请求: {request.url}")
        request.abort()  # 中止请求
    else:
        request.continue_()  # 继续正常请求
```

## 实际应用案例

### 案例1：API数据提取

监听网络请求是获取网站API数据的便捷方式，无需解析复杂的HTML：

```python
from DrissionPage import ChromiumPage
import json
import os

def extract_api_data(url, api_pattern, output_file):
    page = ChromiumPage()
    
    # 开启监听
    page.listen.start(types=['XHR', 'Fetch'])
    
    # 访问页面
    page.get(url)
    print("页面已加载")
    
    # 等待页面完全加载
    page.wait.load_complete()
    
    # 等待特定API请求
    print("等待API数据...")
    api_req = page.listen.wait(api_pattern, timeout=10)
    
    if not api_req:
        print("未找到匹配的API请求")
        page.close()
        return None
        
    print(f"找到API请求: {api_req.url}")
    
    # 获取JSON数据
    try:
        data = api_req.json
        
        # 保存到文件
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"数据已保存至: {output_file}")
        
        page.close()
        return data
        
    except Exception as e:
        print(f"处理数据时出错: {str(e)}")
        page.close()
        return None

# 使用函数提取特定网站的API数据
data = extract_api_data(
    'https://example.com/products', 
    'api/product-list',
    'data/products.json'
)
```

### 案例2：监控页面加载性能

分析页面加载过程中的网络请求，评估性能指标：

```python
from DrissionPage import ChromiumPage
import time
from collections import defaultdict

def analyze_page_loading(url):
    page = ChromiumPage()
    
    # 开启全面监听
    page.listen.start()
    
    # 记录开始时间
    start_time = time.time()
    
    # 访问页面
    page.get(url)
    
    # 等待页面完全加载
    page.wait.load_complete()
    
    # 记录加载完成时间
    load_complete_time = time.time()
    
    # 停止监听
    page.listen.stop()
    
    # 获取所有请求
    requests = page.listen.requests
    
    # 分析数据
    total_requests = len(requests)
    total_size = sum(len(req.response or b'') for req in requests)
    load_time = load_complete_time - start_time
    
    # 按资源类型分类
    resource_types = defaultdict(list)
    for req in requests:
        resource_types[req.type].append(req)
    
    # 打印基本信息
    print(f"页面加载时间: {load_time:.2f} 秒")
    print(f"总请求数: {total_requests}")
    print(f"总数据量: {total_size / 1024 / 1024:.2f} MB")
    
    # 打印各类型资源统计
    print("\n资源类型分布:")
    for type_name, reqs in resource_types.items():
        type_size = sum(len(req.response or b'') for req in reqs)
        print(f"  {type_name}: {len(reqs)} 个请求, {type_size / 1024:.2f} KB")
    
    # 找出最慢的请求
    if requests:
        slowest_reqs = sorted(requests, key=lambda r: r.duration or 0, reverse=True)[:5]
        print("\n加载最慢的5个请求:")
        for i, req in enumerate(slowest_reqs):
            print(f"  {i+1}. {req.url[:100]}... - {req.duration:.2f} 秒")
    
    page.close()
    return {
        'load_time': load_time,
        'total_requests': total_requests,
        'total_size': total_size,
        'resource_types': {k: len(v) for k, v in resource_types.items()}
    }

# 分析页面加载性能
performance_data = analyze_page_loading('https://example.com')
```

### 案例3：自动获取动态加载的数据

许多网站使用无限滚动加载更多数据，可以通过监听请求自动获取：

```python
from DrissionPage import ChromiumPage
import time
import json

def scrape_infinite_scroll(url, api_pattern, max_scrolls=10):
    page = ChromiumPage()
    
    # 访问页面
    page.get(url)
    
    # 开启监听
    page.listen.start(types=['XHR'], urls=[api_pattern])
    
    # 保存所有API返回的数据
    all_items = []
    seen_urls = set()  # 用于避免重复处理相同的请求
    
    # 模拟滚动和数据收集
    for scroll in range(max_scrolls):
        print(f"执行第 {scroll+1} 次滚动...")
        
        # 滚动到页面底部
        page.run_js('window.scrollTo(0, document.body.scrollHeight);')
        
        # 等待新数据加载 (监听新的API请求)
        time.sleep(2)  # 等待请求发出和响应
        
        # 检查新的请求
        new_items_found = False
        requests = page.listen.requests
        
        for req in requests:
            if api_pattern in req.url and req.url not in seen_urls:
                seen_urls.add(req.url)
                
                if req.status_code == 200:
                    try:
                        data = req.json
                        if 'items' in data:
                            # 添加新项目到结果集
                            items = data['items']
                            all_items.extend(items)
                            print(f"  从API获取到 {len(items)} 个新项目")
                            new_items_found = True
                    except Exception as e:
                        print(f"  解析响应出错: {str(e)}")
        
        # 如果没有找到新项目，可能已到达底部
        if not new_items_found:
            print("未检测到新数据，可能已到达页面底部")
            break
    
    print(f"总共收集了 {len(all_items)} 个项目")
    page.close()
    
    # 返回收集的所有数据
    return all_items

# 使用函数收集无限滚动页面的数据
items = scrape_infinite_scroll(
    'https://example.com/infinite-scroll-page',
    'api/items',
    max_scrolls=15
)

# 保存结果
with open('infinite_scroll_data.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
```

## 高级技巧

### 优化网络性能

通过拦截器可以优化网络性能，例如阻止不必要的请求：

```python
# 阻止不必要的资源加载，提高性能
@page.listen.interceptor
def optimize_resources(request):
    # 要阻止的资源类型
    block_types = ['Image', 'Media', 'Font', 'Other']
    
    # 要阻止的URL关键词
    block_keywords = ['analytics', 'tracker', 'ads', 'banner']
    
    # 判断是否阻止
    should_block = (
        request.type in block_types or
        any(keyword in request.url.lower() for keyword in block_keywords)
    )
    
    if should_block:
        request.abort()
    else:
        request.continue_()
```

### 在特定条件下等待请求完成

有时需要等待多个相关请求完成，可以使用自定义等待条件：

```python
def wait_for_data_complete(page, timeout=30):
    """等待所有数据加载请求完成"""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        # 获取所有API请求
        api_requests = page.listen.find('api/data')
        
        # 检查是否所有请求都已完成
        all_completed = all(req.status_code is not None for req in api_requests)
        
        # 检查是否有请求正在进行中
        pending_requests = page.run_js('''
            return performance.getEntriesByType('resource')
                .filter(r => r.name.includes('api/data') && !r.responseEnd)
                .length;
        ''')
        
        if all_completed and not pending_requests:
            print("所有数据请求已完成")
            return True
            
        time.sleep(0.5)
    
    print("等待数据加载超时")
    return False
```

## 小结

网络监听功能为 DrissionPage 提供了强大的能力，使其不仅可以操作页面元素，还能直接与网络层交互。通过网络监听，可以：

1. **直接获取 API 数据**，无需复杂的页面解析
2. **分析网络性能**，找出潜在的性能瓶颈
3. **拦截和修改请求**，实现更高级的自动化场景
4. **模拟网络响应**，便于测试和开发

在实际应用中，网络监听通常与页面操作结合使用，既可以模拟用户交互，又可以直接从网络层获取数据，大大提高了自动化脚本的效率和功能。

在下一章中，我们将探讨 DrissionPage 的 JavaScript 执行能力，学习如何在自动化脚本中使用 JavaScript 来实现更复杂的功能。 