# 下载功能

DrissionPage 提供了强大的下载功能，可以轻松处理文件下载任务。本章将详细介绍如何使用 DrissionPage 的 DownloadKit 组件进行文件下载，包括基本下载、监控下载进度、管理下载任务等高级功能。

## DownloadKit 概述

DownloadKit 是 DrissionPage 中专门用于文件下载的模块，它提供了以下功能：

- 多线程并行下载
- 断点续传
- 限速控制
- 下载进度监控
- 文件校验
- 下载队列管理

无论是简单的单个文件下载，还是复杂的批量下载任务，DownloadKit 都能高效处理。

## 基本下载操作

### 安装和导入

DownloadKit 包含在 DrissionPage 中，无需单独安装。使用时直接导入：

```python
from DrissionPage import DownloadKit
```

### 创建下载器实例

```python
# 创建一个基本的下载器实例
downloader = DownloadKit()

# 带配置参数的下载器
downloader = DownloadKit(
    timeout=30,             # 连接超时时间
    retry=3,                # 重试次数
    chunk_size=1024*1024,   # 分块大小
    save_path='downloads',  # 默认保存路径
    download_path=None,     # 特定下载路径，优先级高于save_path
    thread_num=5,           # 默认线程数
    proxy='http://127.0.0.1:7890'  # 代理设置
)
```

### 单个文件下载

```python
# 最简单的下载方式
downloader.download('https://example.com/file.zip')

# 指定保存路径和文件名
downloader.download(
    'https://example.com/file.zip',
    save_path='D:/downloads',
    rename='myfile.zip'
)

# 使用关键字参数
downloader.download(
    url='https://example.com/file.zip',
    save_path='downloads',
    rename='myfile.zip',
    thread_num=3,           # 使用3个线程下载
    overwrite=True,         # 覆盖同名文件
    show_msg=True,          # 显示下载信息
    auto_retry=True,        # 自动重试
    retry=5                 # 重试5次
)
```

### 获取下载结果

```python
# 获取下载结果
result = downloader.download('https://example.com/file.zip')

# 判断下载是否成功
if result.success:
    print(f'下载成功: {result.path}')
else:
    print(f'下载失败: {result.error}')

# 获取下载信息
print(f'文件大小: {result.size} 字节')
print(f'文件名: {result.name}')
print(f'下载用时: {result.time_used} 秒')
print(f'平均速度: {result.speed} bytes/s')
```

## 高级下载功能

### 多线程并行下载

DownloadKit 默认使用多线程下载大文件，可以显著提高下载速度：

```python
# 设置全局默认线程数
downloader = DownloadKit(thread_num=8)

# 为单个下载任务设置线程数
downloader.download('https://example.com/large_file.zip', thread_num=10)

# 根据文件大小自动调整线程数（示例函数）
def adaptive_threads(file_size):
    """根据文件大小自动调整线程数"""
    if file_size < 1024 * 1024 * 10:  # 小于10MB
        return 1
    elif file_size < 1024 * 1024 * 100:  # 小于100MB
        return 3
    elif file_size < 1024 * 1024 * 1024:  # 小于1GB
        return 5
    else:
        return 8

# 实际使用时可以先获取文件大小，再决定线程数
file_info = downloader.get_file_info('https://example.com/some_file.zip')
thread_count = adaptive_threads(file_info.size)
downloader.download('https://example.com/some_file.zip', thread_num=thread_count)
```

### 获取文件信息

在下载前获取文件信息，可以帮助做出更智能的下载决策：

```python
# 获取远程文件信息
file_info = downloader.get_file_info('https://example.com/file.zip')

# 文件基本信息
print(f'文件名: {file_info.name}')
print(f'文件大小: {file_info.size} 字节')
print(f'内容类型: {file_info.type}')

# 文件是否支持多线程下载（支持断点续传）
if file_info.is_chunked:
    print('支持多线程下载')
else:
    print('不支持多线程下载，将使用单线程')

# 根据文件信息决定是否下载
if file_info.size > 1024 * 1024 * 1024:  # 大于1GB
    choice = input(f'文件大小: {file_info.size / (1024*1024*1024):.2f}GB，是否继续下载? (y/n): ')
    if choice.lower() != 'y':
        print('取消下载')
        exit()
        
# 获取文件实际名称后再下载
downloader.download(
    'https://example.com/file.zip',
    rename=file_info.name  # 使用服务器返回的文件名
)
```

### 断点续传

DownloadKit 支持断点续传，可以恢复中断的下载：

```python
# 启用断点续传（默认启用）
downloader = DownloadKit(resumable=True)

# 单个下载任务设置
result = downloader.download('https://example.com/large_file.zip', resumable=True)

# 如果下载中断，可以继续下载
if not result.success:
    print('下载中断，尝试恢复...')
    result = downloader.download('https://example.com/large_file.zip')  
    # 如果有同名的未完成文件，会自动继续下载
```

### 下载进度监控

DownloadKit 提供了多种方式监控下载进度：

```python
# 通过回调函数监控下载进度
def progress_callback(downloaded, total, speed, percentage):
    print(f'\r下载进度: {percentage:.2f}% ({downloaded}/{total} bytes), 速度: {speed/1024:.2f} KB/s', end='')

# 使用回调函数
downloader.download(
    'https://example.com/file.zip',
    callback=progress_callback,
    interval=0.5  # 每0.5秒更新一次进度
)

# 或者使用内置的进度显示
downloader.download('https://example.com/file.zip', show_progress=True)
```

### 下载速度控制

DownloadKit 允许限制下载速度，避免占用过多带宽：

```python
# 设置全局速度限制（单位：bytes/s）
downloader = DownloadKit(max_speed=1024*1024)  # 1MB/s

# 单个下载任务设置速度限制
downloader.download(
    'https://example.com/file.zip',
    max_speed=512*1024  # 512KB/s
)
```

### 添加请求头和cookies

某些下载需要特定的请求头或cookies才能成功：

```python
# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Referer': 'https://example.com'
}

# 设置cookies
cookies = {
    'session_id': '12345',
    'user_token': 'abcdef'
}

# 带请求头和cookies的下载
downloader.download(
    'https://example.com/protected_file.zip',
    headers=headers,
    cookies=cookies
)
```

### 自定义超时和重试

```python
# 设置连接超时和读取超时
downloader.download(
    'https://example.com/file.zip',
    connect_timeout=10,
    read_timeout=60
)

# 设置重试机制
downloader.download(
    'https://example.com/file.zip',
    auto_retry=True,  # 启用自动重试
    retry=5,          # 最大重试次数
    retry_interval=3  # 重试间隔（秒）
)
```

## 批量下载

### 顺序批量下载

```python
# 准备下载链接列表
urls = [
    'https://example.com/file1.zip',
    'https://example.com/file2.pdf',
    'https://example.com/file3.jpg'
]

# 顺序下载多个文件
results = []
for url in urls:
    result = downloader.download(url, save_path='downloads')
    results.append(result)
    
# 检查下载结果
success_count = sum(1 for r in results if r.success)
print(f'成功下载: {success_count}/{len(urls)} 个文件')
```

### 并发批量下载

使用 DownloadKit 的并发功能可以同时下载多个文件：

```python
# 使用 DownloadKit 的并发下载功能
results = downloader.multithreaded_download(
    urls=['https://example.com/file1.zip', 'https://example.com/file2.pdf'],
    save_path='downloads',
    max_workers=3  # 最大并发下载数
)

# 或者使用 Python 的线程池
import concurrent.futures

def download_file(url):
    return downloader.download(url, save_path='downloads')

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_file, url) for url in urls]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]
```

### 下载队列管理

对于大量下载任务，可以实现一个简单的下载队列管理器：

```python
from DrissionPage import DownloadKit
import queue
import threading
import time

class DownloadManager:
    def __init__(self, concurrent=3, save_path='downloads'):
        self.downloader = DownloadKit(save_path=save_path)
        self.download_queue = queue.Queue()
        self.concurrent = concurrent
        self.active_downloads = 0
        self.results = []
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        
    def add_task(self, url, **kwargs):
        """添加下载任务到队列"""
        self.download_queue.put((url, kwargs))
        
    def worker(self):
        """工作线程，从队列获取任务并下载"""
        while not self.stop_event.is_set():
            try:
                # 获取任务，设置超时以便检查是否需要停止
                url, kwargs = self.download_queue.get(timeout=1)
            except queue.Empty:
                continue
                
            try:
                with self.lock:
                    self.active_downloads += 1
                
                # 执行下载
                result = self.downloader.download(url, **kwargs)
                
                with self.lock:
                    self.results.append(result)
                    
                if result.success:
                    print(f'下载成功: {result.name}')
                else:
                    print(f'下载失败: {url}, 错误: {result.error}')
                    
            except Exception as e:
                print(f'下载出错: {url}, 异常: {str(e)}')
                
            finally:
                with self.lock:
                    self.active_downloads -= 1
                self.download_queue.task_done()
                
    def start(self):
        """启动下载管理器"""
        self.stop_event.clear()
        self.workers = []
        for _ in range(self.concurrent):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            self.workers.append(t)
            
    def stop(self):
        """停止下载管理器"""
        self.stop_event.set()
        for worker in self.workers:
            worker.join(timeout=2)
            
    def wait_completion(self):
        """等待所有任务完成"""
        self.download_queue.join()
        
    def get_status(self):
        """获取当前状态"""
        with self.lock:
            return {
                'queue_size': self.download_queue.qsize(),
                'active_downloads': self.active_downloads,
                'completed': len(self.results),
                'success': sum(1 for r in self.results if r.success)
            }

# 使用下载管理器
manager = DownloadManager(concurrent=3, save_path='downloads')
manager.start()

# 添加下载任务
for i in range(10):
    url = f'https://example.com/file{i}.zip'
    manager.add_task(url, show_progress=True)
    
# 监控下载进度
try:
    while True:
        status = manager.get_status()
        print(f'\r队列: {status["queue_size"]}, 活动: {status["active_downloads"]}, 完成: {status["completed"]}, 成功: {status["success"]}', end='')
        
        if status['queue_size'] == 0 and status['active_downloads'] == 0:
            break
            
        time.sleep(1)
        
    print('\n所有下载任务已完成')
    
except KeyboardInterrupt:
    print('\n用户中断，正在停止下载...')
    manager.stop()
```

## 与页面对象结合使用

DrissionPage 的下载功能可以与页面对象结合使用，自动处理登录状态、cookies等：

### 从网页获取下载链接

```python
from DrissionPage import ChromiumPage, DownloadKit

# 创建页面对象和下载器
page = ChromiumPage()
downloader = DownloadKit()

# 访问网页获取下载链接
page.get('https://example.com/download-page')

# 登录（如果需要）
page.ele('#username').input('user123')
page.ele('#password').input('pass456')
page.ele('#login-button').click()
page.wait.ele_appear('#download-section')

# 提取所有下载链接
download_links = []
link_elements = page.eles('a[href$=".pdf"]')  # 查找所有PDF链接
for ele in link_elements:
    href = ele.attr('href')
    if href:
        download_links.append(href)
        
print(f'找到 {len(download_links)} 个下载链接')

# 使用页面的cookies进行下载
cookies = page.cookies
for url in download_links:
    downloader.download(url, cookies=cookies, save_path='downloads')
```

### 处理需要登录的下载

```python
from DrissionPage import SessionPage, DownloadKit
import os

def download_protected_files():
    # 创建会话页面
    session_page = SessionPage()
    
    # 登录
    session_page.get('https://example.com/login')
    session_page.ele('#username').input('user123')
    session_page.ele('#password').input('pass456')
    session_page.ele('#login-button').click()
    
    # 验证登录成功
    if 'welcome' not in session_page.html.lower():
        print('登录失败')
        return
        
    # 进入下载页面
    session_page.get('https://example.com/files')
    
    # 提取文件列表
    file_links = []
    for tr in session_page.eles('tr.file-row'):
        name_ele = tr.ele('.file-name')
        link_ele = tr.ele('a.download-link')
        
        if name_ele and link_ele:
            file_links.append({
                'name': name_ele.text,
                'url': link_ele.attr('href')
            })
    
    print(f'找到 {len(file_links)} 个文件')
    
    # 创建下载器，使用会话页面的cookies和headers
    downloader = DownloadKit(
        cookies=session_page.cookies,
        headers=session_page.headers
    )
    
    # 创建下载目录
    os.makedirs('protected_files', exist_ok=True)
    
    # 下载所有文件
    for file_info in file_links:
        print(f'正在下载: {file_info["name"]}')
        result = downloader.download(
            file_info['url'],
            save_path='protected_files',
            rename=file_info['name'],
            show_progress=True
        )
        
        if result.success:
            print(f'下载成功: {result.path}')
        else:
            print(f'下载失败: {result.error}')
    
    print('所有文件下载完成')

# 运行下载函数
download_protected_files()
```

### 处理页面中的文件下载按钮

```python
from DrissionPage import WebPage, DownloadKit
import time

def download_from_button_click():
    page = WebPage()
    downloader = DownloadKit(save_path='button_downloads')
    
    # 打开页面
    page.get('https://example.com/download-page')
    
    # 找到所有下载按钮
    download_buttons = page.eles('button.download-btn')
    print(f'找到 {len(download_buttons)} 个下载按钮')
    
    for i, button in enumerate(download_buttons):
        print(f'处理第 {i+1} 个下载按钮')
        
        # 获取按钮上的文件名或描述
        file_desc = button.text
        
        # 监听网络请求以获取下载URL
        page.listen.start()
        
        # 点击下载按钮
        button.click()
        
        # 等待下载请求发出
        time.sleep(2)
        
        # 查找下载请求
        download_url = None
        for req in page.listen.requests:
            if req.url.endswith(('.zip', '.pdf', '.doc', '.xls')):
                download_url = req.url
                break
                
        page.listen.stop()
        
        if download_url:
            print(f'找到下载URL: {download_url}')
            # 使用DownloadKit下载文件
            result = downloader.download(
                download_url,
                cookies=page.cookies,
                headers={'Referer': page.url},
                rename=f"{file_desc.replace(' ', '_')}.{download_url.split('.')[-1]}",
                show_progress=True
            )
            
            if result.success:
                print(f'下载成功: {result.path}')
            else:
                print(f'下载失败: {result.error}')
        else:
            print('未找到下载URL，可能需要其他方式处理')
        
        # 等待一段时间再处理下一个按钮
        time.sleep(2)
    
    page.close()
    print('所有按钮处理完成')

# 运行函数
download_from_button_click()
```

## 实用技巧与最佳实践

### 文件完整性校验

```python
import hashlib

def calculate_md5(file_path):
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 下载并验证文件
def download_and_verify(url, expected_md5):
    downloader = DownloadKit()
    result = downloader.download(url)
    
    if not result.success:
        print(f'下载失败: {result.error}')
        return False
        
    file_md5 = calculate_md5(result.path)
    if file_md5 == expected_md5:
        print(f'文件验证成功: {result.path}')
        return True
    else:
        print(f'文件验证失败，MD5不匹配: {file_md5} != {expected_md5}')
        return False
```

### 智能重命名

```python
import os
import re
from urllib.parse import unquote

def smart_rename(url, original_name=None):
    """智能提取更友好的文件名"""
    if original_name:
        # 使用服务器提供的名称，但清理不安全字符
        filename = re.sub(r'[\\/*?:"<>|]', '_', original_name)
    else:
        # 从URL中提取文件名
        url_filename = os.path.basename(unquote(url.split('?')[0]))
        
        # 如果URL没有明确的文件名部分，使用参数或生成一个
        if not url_filename or '.' not in url_filename:
            # 尝试从URL参数中查找文件名
            if 'filename=' in url:
                param_name = re.search(r'filename=([^&]+)', url)
                if param_name:
                    url_filename = unquote(param_name.group(1))
            
            # 如果仍然没有文件名，生成一个带时间戳的名称
            if not url_filename or '.' not in url_filename:
                import time
                timestamp = int(time.time())
                url_filename = f'download_{timestamp}'
                
                # 尝试从Content-Type猜测扩展名
                content_type_map = {
                    'application/pdf': '.pdf',
                    'application/zip': '.zip',
                    'application/x-rar-compressed': '.rar',
                    'application/msword': '.doc',
                    'application/vnd.ms-excel': '.xls',
                    'image/jpeg': '.jpg',
                    'image/png': '.png'
                }
                
                # 获取文件信息
                downloader = DownloadKit()
                file_info = downloader.get_file_info(url)
                
                # 根据Content-Type添加扩展名
                if file_info.type in content_type_map:
                    url_filename += content_type_map[file_info.type]
        
        filename = re.sub(r'[\\/*?:"<>|]', '_', url_filename)
    
    return filename

# 使用智能重命名
downloader = DownloadKit()
url = 'https://example.com/download?file_id=12345&filename=report.pdf'
file_info = downloader.get_file_info(url)
filename = smart_rename(url, file_info.name)
result = downloader.download(url, rename=filename)
```

### 保存下载历史

```python
import json
import datetime
import os

class DownloadHistory:
    def __init__(self, history_file='download_history.json'):
        self.history_file = history_file
        self.history = self._load_history()
        
    def _load_history(self):
        """加载历史记录"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f'加载历史记录失败: {e}')
                return []
        return []
        
    def _save_history(self):
        """保存历史记录"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f'保存历史记录失败: {e}')
            
    def add_entry(self, download_result):
        """添加下载记录"""
        entry = {
            'url': download_result.url,
            'path': download_result.path,
            'name': download_result.name,
            'size': download_result.size,
            'time_used': download_result.time_used,
            'success': download_result.success,
            'timestamp': datetime.datetime.now().isoformat(),
        }
        
        if not download_result.success:
            entry['error'] = download_result.error
            
        self.history.append(entry)
        self._save_history()
        
    def get_history(self):
        """获取所有历史记录"""
        return self.history
        
    def search_by_name(self, name_pattern):
        """按文件名搜索历史记录"""
        return [entry for entry in self.history 
                if name_pattern.lower() in entry['name'].lower()]
                
    def get_statistics(self):
        """获取下载统计信息"""
        total = len(self.history)
        successful = sum(1 for entry in self.history if entry['success'])
        total_size = sum(entry['size'] for entry in self.history if entry['success'])
        
        return {
            'total_downloads': total,
            'successful_downloads': successful,
            'failed_downloads': total - successful,
            'success_rate': successful / total if total > 0 else 0,
            'total_downloaded_size': total_size,
            'average_size': total_size / successful if successful > 0 else 0
        }

# 使用下载历史管理
downloader = DownloadKit()
history = DownloadHistory()

# 下载并记录
result = downloader.download('https://example.com/file.zip')
history.add_entry(result)

# 显示统计信息
stats = history.get_statistics()
print(f"总下载: {stats['total_downloads']}, 成功率: {stats['success_rate']*100:.2f}%")
print(f"总下载大小: {stats['total_downloaded_size']/1024/1024:.2f} MB")
```

## 小结

本章详细介绍了 DrissionPage 的下载功能，包括：

1. **基本下载操作**：使用 DownloadKit 下载单个文件
2. **高级下载功能**：多线程并行、断点续传、进度监控等
3. **批量下载**：顺序和并发下载多个文件
4. **与页面对象结合**：结合网页操作实现复杂下载流程
5. **实用技巧**：文件校验、智能重命名、下载历史管理等

掌握这些下载技能，可以帮助你实现各种复杂的文件下载需求，无论是简单的单个文件下载，还是需要登录验证的批量下载任务。

在下一章中，我们将学习如何处理 iframe 元素，解决网页中常见的嵌套页面操作问题。 