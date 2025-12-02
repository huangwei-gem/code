# 性能优化

在进行网页自动化时，性能是一个关键的考量因素。本文将探讨如何优化 DrissionPage 的执行效率，减少资源消耗，提高数据读取速度，以便在处理大规模任务时获得更好的性能表现。

## 加速数据读取

### 1. 使用高效的选择器

选择器的效率对元素查找速度有显著影响：

```python
# 低效方式：使用复杂的XPath
elements = page.eles('//div[contains(@class, "item")]//span[contains(text(), "价格")]')

# 高效方式：使用CSS选择器
elements = page.eles('.item .price')
```

选择器效率从高到低的排序：
1. ID选择器（`#id`）
2. CSS选择器（`.class`）
3. 简单XPath（`//tagname[@attr='value']`）
4. 复杂XPath（包含多个条件和函数）

### 2. 优化元素查找策略

```python
# 低效方式：重复在整个页面查找元素
header = page.ele('.header')
menu = page.ele('.menu')
content = page.ele('.content')

# 高效方式：使用链式查找
header = page.ele('.header')
menu = header.next('.menu')  # 从header元素开始查找
content = menu.next('.content')  # 从menu元素开始查找
```

### 3. 批量获取数据

```python
# 低效方式：逐个获取元素并处理
items = page.eles('.item')
results = []
for item in items:
    name = item.ele('.name').text
    price = item.ele('.price').text
    results.append((name, price))

# 高效方式：使用JavaScript批量获取
results = page.run_script('''
    const items = document.querySelectorAll('.item');
    return Array.from(items).map(item => {
        const name = item.querySelector('.name').textContent;
        const price = item.querySelector('.price').textContent;
        return [name, price];
    });
''')
```

### 4. 缓存常用数据

```python
# 缓存页面元素和数据
class Scraper:
    def __init__(self):
        self.page = ChromiumPage()
        self.elements_cache = {}
        self.data_cache = {}
    
    def get_element(self, selector):
        if selector not in self.elements_cache:
            self.elements_cache[selector] = self.page.ele(selector)
        return self.elements_cache[selector]
    
    def extract_data(self, url, refresh=False):
        if url not in self.data_cache or refresh:
            self.page.get(url)
            # 提取数据
            data = {...}  # 实际数据提取逻辑
            self.data_cache[url] = data
        return self.data_cache[url]
```

### 5. 避免不必要的页面加载

```python
# 低效方式：对每个操作都加载新页面
page.get('https://example.com/page1')
data1 = page.ele('#data').text
page.get('https://example.com/page2')
data2 = page.ele('#data').text

# 高效方式：使用Ajax请求或浏览器API
page.get('https://example.com/')
data1 = page.run_script('return fetch("/api/data1").then(r => r.json())')
data2 = page.run_script('return fetch("/api/data2").then(r => r.json())')
```

## 减少资源消耗

### 1. 禁用不必要的功能

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 创建高性能配置
options = ChromiumOptions()
options.set_headless(True)  # 启用无头模式
options.set_load_images(False)  # 禁用图片加载
options.set_browser_options('disable-gpu', True)  # 禁用GPU加速
options.set_browser_options('disable-javascript', False)  # 保持JavaScript启用（根据需要）

# 设置其他性能相关选项
options.set_browser_options('disable-extensions', True)  # 禁用扩展
options.set_browser_options('disable-plugins', True)  # 禁用插件
options.set_browser_options('disable-dev-shm-usage', True)  # 避免内存问题

# 创建页面对象
page = ChromiumPage(options)
```

### 2. 关闭不需要的标签页和窗口

```python
# 打开多个标签页处理任务
page = ChromiumPage()
page.get('https://example.com')

# 打开新标签页
tab1 = page.new_tab('https://example.com/page1')
tab2 = page.new_tab('https://example.com/page2')

# 处理完一个标签页后立即关闭
data1 = tab1.ele('#data').text
tab1.close()  # 立即关闭不再需要的标签页

# 处理第二个标签页
data2 = tab2.ele('#data').text
tab2.close()
```

### 3. 垃圾回收和资源释放

```python
import gc

def scrape_large_dataset(urls):
    page = ChromiumPage()
    results = []
    
    for i, url in enumerate(urls):
        page.get(url)
        data = extract_data(page)
        results.append(data)
        
        # 每处理50个URL清理一次内存
        if i % 50 == 0:
            gc.collect()  # 强制垃圾回收
    
    page.quit()  # 确保浏览器实例被关闭
    return results

def extract_data(page):
    # 数据提取逻辑
    return {...}
```

### 4. 使用 SessionPage 替代 ChromiumPage

对于不需要渲染JavaScript的简单页面，使用SessionPage可以大幅减少资源消耗：

```python
from DrissionPage import SessionPage

# 对于静态页面或简单API
page = SessionPage()
page.get('https://example.com/api')
data = page.json  # 获取JSON响应

# 如果需要处理简单HTML
page.get('https://example.com/simple-page')
title = page.ele('h1').text
links = [a.link for a in page.eles('a')]
```

### 5. 内存使用优化

处理大量数据时避免一次性加载全部内容：

```python
# 使用生成器分批处理数据
def process_items(page, item_selector, batch_size=100):
    total_items = page.ele_count(item_selector)
    
    for start in range(0, total_items, batch_size):
        # 获取当前批次的元素
        script = f'''
            const items = document.querySelectorAll("{item_selector}");
            const batch = [];
            for(let i={start}; i<Math.min({start+batch_size}, items.length); i++) {{
                batch.push(items[i].textContent);
            }}
            return batch;
        '''
        batch_data = page.run_script(script)
        
        # 逐个处理当前批次
        for item in batch_data:
            yield item

# 使用示例
page = ChromiumPage()
page.get('https://example.com/large-list')

for item in process_items(page, '.item', batch_size=50):
    process_item(item)  # 处理单个项目的函数
```

## 优化执行效率

### 1. 并行处理和多线程

```python
from concurrent.futures import ThreadPoolExecutor
import time

def scrape_url(url):
    """抓取单个URL的函数"""
    page = ChromiumPage()
    try:
        page.get(url)
        # 提取数据
        title = page.ele('h1').text
        content = page.ele('#content').text
        return {'url': url, 'title': title, 'content': content}
    finally:
        page.quit()  # 确保关闭浏览器

# 并行处理多个URL
urls = ['https://example.com/page1', 'https://example.com/page2', ...]

start_time = time.time()

# 使用线程池并行处理
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(scrape_url, urls))

end_time = time.time()
print(f"并行处理耗时: {end_time - start_time:.2f}秒")
```

### 2. 使用自定义等待条件

避免固定等待时间，使用条件等待：

```python
# 低效方式：使用固定等待时间
page.ele('#submit-button').click()
time.sleep(5)  # 固定等待5秒

# 高效方式：使用条件等待
page.ele('#submit-button').click()
page.wait.load_complete()  # 等待页面加载完成

# 更高效方式：使用自定义等待条件
page.ele('#submit-button').click()
page.wait.ele_displayed('#result', timeout=10)  # 等待结果元素显示，最多10秒
```

### 3. 预加载和预处理

```python
# 预加载常用页面到缓存
def preload_pages(urls):
    """预加载页面到浏览器缓存"""
    page = ChromiumPage()
    for url in urls:
        page.get(url)
        page.wait.load_complete()
    page.quit()

# 在主程序开始前预加载
common_urls = ['https://example.com', 'https://example.com/common-page', ...]
import threading
preload_thread = threading.Thread(target=preload_pages, args=(common_urls,))
preload_thread.start()

# 继续执行主程序
# ...

# 如果需要等待预加载完成
preload_thread.join()
```

### 4. 使用异步处理

```python
import asyncio
from DrissionPage.async_browser import AsyncPage

async def scrape_page(url):
    """异步抓取单个页面"""
    page = await AsyncPage.new_page()
    try:
        await page.get(url)
        title = await page.ele('h1').text
        content = await page.ele('#content').text
        return {'url': url, 'title': title, 'content': content}
    finally:
        await page.close()

async def main():
    urls = ['https://example.com/page1', 'https://example.com/page2', ...]
    tasks = [scrape_page(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# 运行异步任务
results = asyncio.run(main())
```

### 5. 使用连接池

对于SessionPage，可以使用连接池提高效率：

```python
from DrissionPage import SessionOptions, SessionPage

# 配置连接池
options = SessionOptions()
options.set_session_options(pool_connections=10, pool_maxsize=10)

# 创建使用连接池的SessionPage
page = SessionPage(options)

# 现在可以高效地发送多个请求
for url in urls:
    page.get(url)
    # 处理数据
```

## 实际案例：高性能爬虫

让我们结合上述技术，创建一个高性能爬虫示例：

```python
from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage
from concurrent.futures import ThreadPoolExecutor
import time
import json
import os

class HighPerformanceScraper:
    def __init__(self, max_workers=5, headless=True, disable_images=True):
        # 配置ChromiumPage
        self.chrome_options = ChromiumOptions()
        self.chrome_options.set_headless(headless)
        self.chrome_options.set_load_images(not disable_images)
        self.chrome_options.set_browser_options('disable-gpu', True)
        self.chrome_options.set_browser_options('disable-extensions', True)
        
        # 线程池
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        
        # 缓存目录
        self.cache_dir = 'data_cache'
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def scrape_urls(self, urls, force_refresh=False):
        """并行抓取多个URL"""
        start_time = time.time()
        futures = []
        
        for url in urls:
            cache_file = os.path.join(self.cache_dir, self._url_to_filename(url))
            
            # 检查缓存
            if not force_refresh and os.path.exists(cache_file):
                with open(cache_file, 'r', encoding='utf-8') as f:
                    print(f"从缓存加载: {url}")
                    continue
            
            # 提交任务到线程池
            future = self.executor.submit(self._scrape_single_url, url, cache_file)
            futures.append(future)
        
        # 获取所有结果
        results = [future.result() for future in futures]
        
        # 加载缓存中的结果
        if not force_refresh:
            for url in urls:
                cache_file = os.path.join(self.cache_dir, self._url_to_filename(url))
                if os.path.exists(cache_file) and not any(r['url'] == url for r in results):
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        results.append(json.load(f))
        
        end_time = time.time()
        print(f"抓取 {len(urls)} 个URL，耗时: {end_time - start_time:.2f}秒")
        return results
    
    def _scrape_single_url(self, url, cache_file):
        """抓取单个URL并缓存结果"""
        print(f"正在抓取: {url}")
        
        # 选择合适的页面类型
        if self._is_static_page(url):
            # 使用SessionPage处理静态页面
            page = SessionPage()
            page.get(url)
            
            # 提取数据
            data = self._extract_data_from_session(page)
        else:
            # 使用ChromiumPage处理动态页面
            page = ChromiumPage(self.chrome_options)
            page.get(url)
            page.wait.load_complete()
            
            # 提取数据
            data = self._extract_data_from_chromium(page)
            page.quit()  # 关闭浏览器实例
        
        # 保存到缓存
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return data
    
    def _url_to_filename(self, url):
        """将URL转换为合法的文件名"""
        return url.replace('https://', '').replace('http://', '').replace('/', '_') + '.json'
    
    def _is_static_page(self, url):
        """判断是否为静态页面（简化版，实际应用中可能需要更复杂的逻辑）"""
        return '.json' in url or '.xml' in url or 'api' in url
    
    def _extract_data_from_session(self, page):
        """从SessionPage提取数据"""
        url = page.url
        
        # 检查是否为JSON API
        if page.response.headers.get('Content-Type', '').startswith('application/json'):
            return {
                'url': url,
                'type': 'json',
                'data': page.json
            }
        
        # 否则提取HTML内容
        title = page.ele('title').text if page.ele_exists('title') else ''
        h1 = page.ele('h1').text if page.ele_exists('h1') else ''
        
        return {
            'url': url,
            'type': 'html',
            'title': title,
            'h1': h1,
            'links': [a.link for a in page.eles('a[href]')][:10]  # 仅获取前10个链接
        }
    
    def _extract_data_from_chromium(self, page):
        """从ChromiumPage提取数据（可以处理JS渲染的内容）"""
        url = page.url
        
        # 使用JavaScript批量提取数据
        data = page.run_script('''
            return {
                title: document.title,
                h1: document.querySelector('h1')?.textContent || '',
                metaDescription: document.querySelector('meta[name="description"]')?.content || '',
                links: Array.from(document.querySelectorAll('a[href]'))
                    .slice(0, 10)
                    .map(a => a.href)
            }
        ''')
        
        return {
            'url': url,
            'type': 'dynamic_html',
            'title': data['title'],
            'h1': data['h1'],
            'description': data['metaDescription'],
            'links': data['links']
        }
    
    def close(self):
        """关闭资源"""
        self.executor.shutdown()

# 使用示例
if __name__ == "__main__":
    urls = [
        'https://example.com',
        'https://example.com/about',
        'https://example.com/products',
        'https://example.com/api/data.json',
        # 更多URL...
    ]
    
    scraper = HighPerformanceScraper(max_workers=3)
    results = scraper.scrape_urls(urls)
    
    # 处理结果
    for result in results:
        print(f"URL: {result['url']}, 标题: {result.get('title', 'N/A')}")
    
    scraper.close()
```

## 性能测试和分析

### 1. 使用性能分析工具

```python
import cProfile
import pstats

# 使用cProfile分析性能
def profile_function(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    
    # 输出分析结果
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(20)  # 打印前20个耗时最长的函数
    
    return result

# 使用示例
profile_function(scraper.scrape_urls, urls)
```

### 2. 测量不同配置下的性能

```python
import time

def benchmark_config():
    """测试不同配置下的性能"""
    test_url = 'https://example.com'
    results = []
    
    # 测试配置1: 默认设置
    options1 = ChromiumOptions()
    page1 = ChromiumPage(options1)
    start = time.time()
    page1.get(test_url)
    page1.wait.load_complete()
    time1 = time.time() - start
    page1.quit()
    results.append(('默认设置', time1))
    
    # 测试配置2: 无头模式
    options2 = ChromiumOptions()
    options2.set_headless(True)
    page2 = ChromiumPage(options2)
    start = time.time()
    page2.get(test_url)
    page2.wait.load_complete()
    time2 = time.time() - start
    page2.quit()
    results.append(('无头模式', time2))
    
    # 测试配置3: 无头 + 禁用图片
    options3 = ChromiumOptions()
    options3.set_headless(True)
    options3.set_load_images(False)
    page3 = ChromiumPage(options3)
    start = time.time()
    page3.get(test_url)
    page3.wait.load_complete()
    time3 = time.time() - start
    page3.quit()
    results.append(('无头+禁用图片', time3))
    
    # 测试配置4: SessionPage
    page4 = SessionPage()
    start = time.time()
    page4.get(test_url)
    time4 = time.time() - start
    results.append(('SessionPage', time4))
    
    # 输出结果
    print("性能测试结果:")
    for name, time_taken in results:
        print(f"{name}: {time_taken:.4f}秒")

# 运行基准测试
benchmark_config()
```

## 优化建议小结

以下是提高 DrissionPage 性能的关键建议：

1. **选择合适的页面类型**:
   - 对于静态页面和API，使用轻量级的 SessionPage
   - 仅在需要JavaScript渲染时使用 ChromiumPage

2. **优化查找和操作**:
   - 使用高效的选择器（ID > CSS > XPath）
   - 实施链式查找减少搜索范围
   - 批量操作代替单个操作

3. **减少资源消耗**:
   - 使用无头模式
   - 禁用不必要的功能（图片、扩展等）
   - 及时关闭不再需要的页面和标签页

4. **利用缓存和预加载**:
   - 缓存经常使用的数据和元素
   - 实施数据本地缓存策略
   - 预加载常用页面

5. **并发和异步处理**:
   - 使用多线程并行处理多个任务
   - 实施连接池和请求合并
   - 使用异步处理提高效率

6. **智能等待和重试**:
   - 使用条件等待替代固定等待
   - 实施智能的重试策略
   - 根据页面加载状态动态调整行为

7. **内存管理**:
   - 分批处理大数据集
   - 定期进行垃圾回收
   - 监控和限制内存使用

通过综合应用这些技术，你可以显著提高 DrissionPage 自动化脚本的性能，使其能够高效地处理大规模任务。

## 实用工具函数

最后，这里提供一些实用的性能优化工具函数，可以直接集成到你的项目中：

```python
# performance_utils.py

import time
import functools
import gc
import os
import json
from datetime import datetime

# 函数执行计时装饰器
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

# 内存使用监控装饰器
def memory_monitor(func):
    import psutil
    process = psutil.Process(os.getpid())
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 执行前内存使用
        gc.collect()
        before = process.memory_info().rss / 1024 / 1024  # MB
        
        result = func(*args, **kwargs)
        
        # 执行后内存使用
        gc.collect()
        after = process.memory_info().rss / 1024 / 1024  # MB
        print(f"{func.__name__} 内存使用: 前 {before:.2f}MB, 后 {after:.2f}MB, 差值 {after-before:.2f}MB")
        
        return result
    return wrapper

# 简单的磁盘缓存系统
class DiskCache:
    def __init__(self, cache_dir='cache', expire_days=7):
        self.cache_dir = cache_dir
        self.expire_seconds = expire_days * 24 * 60 * 60
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_path(self, key):
        """获取缓存文件路径"""
        # 将键转换为文件名
        filename = str(hash(key)) + '.json'
        return os.path.join(self.cache_dir, filename)
    
    def get(self, key, default=None):
        """获取缓存的值"""
        path = self._get_cache_path(key)
        
        # 检查文件是否存在
        if not os.path.exists(path):
            return default
        
        # 检查是否过期
        if self.expire_seconds > 0:
            modified_time = os.path.getmtime(path)
            if time.time() - modified_time > self.expire_seconds:
                os.remove(path)  # 删除过期缓存
                return default
        
        # 读取缓存
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['value']
        except Exception:
            return default
    
    def set(self, key, value):
        """设置缓存值"""
        path = self._get_cache_path(key)
        
        # 写入缓存
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'value': value
            }, f, ensure_ascii=False)
    
    def clear(self, older_than_days=None):
        """清除所有缓存或指定天数前的缓存"""
        if older_than_days is None:
            # 清除所有缓存
            for file in os.listdir(self.cache_dir):
                os.remove(os.path.join(self.cache_dir, file))
        else:
            # 清除指定天数前的缓存
            cutoff = time.time() - older_than_days * 24 * 60 * 60
            for file in os.listdir(self.cache_dir):
                path = os.path.join(self.cache_dir, file)
                if os.path.getmtime(path) < cutoff:
                    os.remove(path)

# 批量处理器
class BatchProcessor:
    def __init__(self, batch_size=100):
        self.batch_size = batch_size
    
    def process(self, items, process_func):
        """分批处理项目"""
        results = []
        total = len(items)
        
        for i in range(0, total, self.batch_size):
            batch = items[i:i+self.batch_size]
            print(f"处理批次 {i//self.batch_size + 1}/{(total-1)//self.batch_size + 1} ({len(batch)}项)")
            
            batch_results = process_func(batch)
            results.extend(batch_results)
            
            # 每批次后进行垃圾回收
            gc.collect()
        
        return results

# 使用示例
if __name__ == "__main__":
    # 计时器示例
    @timer
    def slow_function():
        time.sleep(2)
        return "完成"
    
    result = slow_function()
    
    # 缓存示例
    cache = DiskCache('test_cache')
    
    # 使用缓存的函数
    def get_data_with_cache(url):
        # 尝试从缓存获取
        data = cache.get(url)
        if data is not None:
            print(f"从缓存获取: {url}")
            return data
        
        print(f"从网络获取: {url}")
        # 这里应该是实际的网络请求
        time.sleep(1)  # 模拟网络延迟
        data = {"url": url, "content": "示例内容"}
        
        # 存入缓存
        cache.set(url, data)
        return data
    
    # 测试缓存
    url = "https://example.com/test"
    print("第一次调用:")
    get_data_with_cache(url)
    
    print("\n第二次调用(应该从缓存获取):")
    get_data_with_cache(url)
```

这些工具函数可以帮助你在实际项目中实施性能优化策略，提高 DrissionPage 自动化脚本的运行效率。 