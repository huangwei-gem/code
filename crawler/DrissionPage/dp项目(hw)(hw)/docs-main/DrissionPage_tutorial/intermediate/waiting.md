# 等待和超时处理

在网页自动化过程中，等待是一个非常重要的概念。由于网页加载、AJAX 请求、动画效果等因素，元素可能不会立即可用，需要适当的等待机制来确保自动化脚本的稳定性和可靠性。本章将详细介绍 DrissionPage 提供的各种等待和超时处理机制。

## 为什么需要等待

在实际的网页自动化场景中，通常会遇到以下需要等待的情况：

1. 页面加载和渲染需要时间
2. AJAX 异步加载内容
3. 动画效果导致元素暂时不可交互
4. 服务器响应延迟
5. 网络连接速度差异

不正确的等待处理可能导致以下问题：

- 元素未加载完成就尝试操作，导致失败
- 错过状态变化或动态内容
- 脚本执行太快，页面反应不及时
- 资源浪费（等待时间过长）

DrissionPage 提供了多种灵活的等待机制，帮助你在不同场景下高效地处理等待需求。

## 等待类型

DrissionPage 中的等待主要分为以下几类：

### 显式等待

明确指定等待条件和超时时间的等待方式。

```python
# 等待元素出现
element = page.wait.ele_appear('#loading-complete', timeout=10)

# 等待元素可见
page.wait.ele_display('.notification', timeout=5)
```

### 隐式等待

全局设置的默认等待时间，影响所有元素查找操作。

```python
# 设置隐式等待时间
page.set.ele_timeout(10)  # 所有元素查找默认等待10秒
```

### 固定等待

简单地暂停脚本执行一段指定的时间。

```python
# 固定等待3秒
page.wait(3)
```

## 显式等待详解

显式等待是最精确和高效的等待方式，DrissionPage 提供了丰富的显式等待方法。

### 等待页面和导航

```python
# 等待页面完全加载
page.wait.load_complete()

# 等待导航完成（URL变化后的加载）
page.wait.navigation()

# 等待页面准备就绪
page.wait.doc_loaded()

# 等待URL变化
page.wait.url_change()

# 等待URL包含特定内容
page.wait.url_contain('success')
```

### 等待元素状态

```python
# 等待元素出现在DOM中
element = page.wait.ele_appear('#result', timeout=10)

# 等待元素从DOM中消失
page.wait.ele_disappear('.loading', timeout=10)

# 等待元素变为可见
element = page.wait.ele_display('.notification')

# 等待元素变为不可见
page.wait.ele_not_display('#popup')

# 等待元素属性包含特定值
page.wait.ele_attr('#status', 'class', 'success')
```

### 等待文本和内容

```python
# 等待页面包含特定文本
page.wait.text_appear('操作成功')

# 等待页面不包含特定文本
page.wait.text_disappear('正在处理')

# 等待元素文本包含特定内容
button = page.ele('#submit-button')
button.wait.text_appear('已完成')

# 等待元素文本不包含特定内容
button.wait.text_disappear('处理中')
```

### 等待网络请求

```python
# 等待特定网络请求完成
page.listen.start()  # 开始监听网络
page.ele('#submit-button').click()
page.listen.wait_request('api/submit', timeout=10)  # 等待API请求完成

# 等待所有请求完成
page.listen.wait_requests_done()
```

### 等待下载

```python
# 等待下载开始
page.ele('#download-button').click()
page.wait.download_begin(timeout=10)

# 等待下载完成
status = page.wait.download_complete(timeout=60)
print(f'下载状态: {status}')  # 'complete', 'canceled', 'timeout'
```

### 在元素上的等待

DrissionPage 允许在已找到的元素上直接使用等待方法：

```python
# 找到元素
button = page.ele('#dynamic-button')

# 等待元素变为可点击状态
button.wait.clickable()

# 等待元素文本变化
button.wait.text_not_equal('Loading...')

# 等待元素属性变化
button.wait.attr('disabled', None)  # 等待disabled属性消失
```

## 自定义等待条件

DrissionPage 允许创建自定义等待条件，满足复杂场景需求：

```python
# 自定义等待函数
def wait_for_specific_condition(driver):
    try:
        # 检查特定条件
        progress = driver.ele('#progress').attr('value')
        return int(progress) >= 100  # 当进度达到100%时返回True
    except:
        return False  # 发生异常返回False

# 使用自定义等待条件
page.wait.until(wait_for_specific_condition, timeout=30, message='进度未达到100%')
```

## 超时处理策略

### 设置超时时间

```python
# 设置全局默认元素查找超时
page.set.ele_timeout(10)  # 10秒

# 设置全局默认页面加载超时
page.set.load_timeout(30)  # 30秒

# 为单个操作设置超时
element = page.ele('#dynamic-content', timeout=5)  # 5秒
page.wait.ele_appear('#results', timeout=15)  # 15秒
```

### 超时异常处理

```python
# 方法1：使用try-except捕获超时异常
try:
    element = page.wait.ele_appear('#nonexistent', timeout=5, raise_err=True)
    element.click()
except TimeoutError as e:
    print(f'等待超时: {e}')
    # 执行备选方案或恢复操作
    
# 方法2：检查返回结果（大多数等待方法在超时时返回False或None）
element = page.wait.ele_appear('#nonexistent', timeout=5)  # 不抛出异常
if element:
    element.click()
else:
    print('元素未出现，执行备选方案')
```

### 灵活的超时策略

根据不同场景设置合适的超时时间：

```python
# 针对不同网络环境调整超时时间
def adaptive_timeout(page, base_timeout=10):
    """根据网络状况动态调整超时时间"""
    # 测试网络响应时间
    start_time = time.time()
    page.get('https://example.com/ping')
    response_time = time.time() - start_time
    
    # 根据响应时间调整超时
    if response_time < 0.5:  # 快速网络
        return base_timeout
    elif response_time < 2:  # 一般网络
        return base_timeout * 1.5
    else:  # 慢速网络
        return base_timeout * 2.5

# 使用动态超时
timeout = adaptive_timeout(page)
element = page.wait.ele_appear('#results', timeout=timeout)
```

## 等待模式和异步处理

### 阻塞式等待与非阻塞式等待

```python
# 阻塞式等待（默认方式）
page.wait.ele_appear('#results')  # 会阻塞脚本执行直到元素出现或超时

# 非阻塞式等待（使用多线程）
import threading

def wait_for_element(page):
    result = page.wait.ele_appear('#results', timeout=30)
    if result:
        print('元素已出现')
    else:
        print('等待超时')

# 创建等待线程
wait_thread = threading.Thread(target=wait_for_element, args=(page,))
wait_thread.start()

# 主线程可以继续执行其他操作
print('主线程继续执行...')
# ... 执行其他任务 ...

# 如果需要，可以等待等待线程完成
wait_thread.join()
```

### 等待时执行操作

有时需要在等待过程中执行某些操作，例如定期检查或保持页面活动：

```python
def wait_with_activity(page, selector, timeout=30, interval=3):
    """在等待元素出现的同时执行一些操作保持页面活动"""
    end_time = time.time() + timeout
    
    while time.time() < end_time:
        # 检查元素是否出现
        element = page.ele(selector, timeout=0.5)
        if element:
            return element
            
        # 执行一些操作，防止页面超时或保持会话
        page.scroll.down(100)  # 轻微滚动页面
        page.run_js('console.log("保持活动: " + new Date())')  # 执行JS保持活动
        time.sleep(interval)
    
    return None  # 超时返回None

# 使用带活动的等待
element = wait_with_activity(page, '#lazy-loaded-content')
```

## 常见等待场景与最佳实践

### 等待页面加载

```python
# 完整页面加载流程
page.get('https://example.com')
page.wait.load_complete()  # 等待页面完全加载

# 仅等待文档就绪（DOM可用，但资源可能还在加载）
page.get('https://example.com')
page.wait.doc_loaded()
```

### 等待AJAX内容

```python
# 方法1：等待特定元素出现
page.ele('#load-data-button').click()
page.wait.ele_appear('.data-item', timeout=10)

# 方法2：等待网络请求完成
page.listen.start()  # 开始监听网络
page.ele('#load-data-button').click()
page.listen.wait_request('api/data', timeout=10)
```

### 等待动画完成

```python
# 等待CSS动画完成
page.ele('#animate-button').click()
page.wait(0.5)  # 给动画开始的时间
page.wait.ele_attr('#animated-element', 'class', 'animation-complete')

# 或者等待元素达到最终状态
def animation_complete(driver):
    element = driver.ele('#animated-element')
    rect = element.rect
    return rect['x'] > 500  # 检查元素是否移动到目标位置

page.wait.until(animation_complete, timeout=5)
```

### 处理登录和表单提交

```python
# 登录流程的等待处理
def login(page, username, password):
    page.get('https://example.com/login')
    page.wait.load_complete()
    
    # 填写表单
    page.ele('#username').input(username)
    page.ele('#password').input(password)
    
    # 提交表单并等待结果
    page.ele('#login-button').click()
    
    # 等待可能的多种结果
    success = page.wait.ele_appear('#dashboard', timeout=5)
    if success:
        return True  # 登录成功
        
    error = page.ele('.error-message')
    if error:
        print(f'登录失败: {error.text}')
        return False
        
    # 检查是否需要二次验证
    if page.ele('#two-factor'):
        print('需要二次验证')
        # 处理二次验证...
        
    return False
```

### 长时间运行任务的等待

```python
# 等待长时间运行的后台任务
def wait_for_task_completion(page, task_id, max_wait=300):
    """等待后台任务完成，定期检查任务状态"""
    start_time = time.time()
    check_interval = 5  # 每5秒检查一次
    
    while time.time() - start_time < max_wait:
        # 检查任务状态
        page.get(f'https://example.com/tasks/{task_id}/status')
        status = page.run_js('return document.body.textContent')
        status_json = json.loads(status)
        
        if status_json['status'] == 'completed':
            return True
        elif status_json['status'] == 'failed':
            print(f"任务失败: {status_json.get('error', '未知错误')}")
            return False
            
        # 计算下一次检查前的等待时间
        elapsed = time.time() - start_time
        progress = status_json.get('progress', 0)
        
        # 根据进度调整检查频率
        if progress > 80:
            check_interval = 2  # 接近完成时检查更频繁
        elif progress > 50:
            check_interval = 3
        
        print(f"任务进度: {progress}%, 已用时间: {int(elapsed)}秒")
        time.sleep(check_interval)
    
    print(f"等待超过最大时间: {max_wait}秒")
    return False

# 使用
page.ele('#start-task').click()
task_id = page.wait.ele_appear('#task-id').text
success = wait_for_task_completion(page, task_id)
```

## 高级等待技巧

### 智能等待策略

```python
# 综合多个条件的智能等待
def smart_wait_for_page_ready(page, timeout=30):
    """综合多种条件判断页面是否真正准备就绪"""
    start_time = time.time()
    
    # 首先等待基本加载
    page.wait.doc_loaded(timeout=timeout)
    
    # 定义检查函数
    def is_truly_ready():
        # 1. 检查是否有加载指示器
        if page.ele('.loading-spinner', displayed=True):
            return False
            
        # 2. 检查网络活动是否完成
        if hasattr(page, 'listen') and page.listen.is_active:
            active_requests = len([r for r in page.listen.requests if r.status is None])
            if active_requests > 0:
                return False
        
        # 3. 检查主要内容区域是否已加载
        main_content = page.ele('#main-content')
        if not main_content or not main_content.eles('*'):
            return False
            
        # 4. 执行自定义JS检查
        js_ready = page.run_js('''
            return {
                ajaxActive: (window.jQuery ? jQuery.active : 0) === 0,
                animationsComplete: !document.querySelector('.animating'),
                lazyImagesLoaded: Array.from(
                    document.querySelectorAll('img[data-src]')
                ).every(img => img.complete && img.currentSrc !== '')
            }
        ''')
        
        if not all(js_ready.values()):
            return False
            
        return True  # 所有条件满足，页面真正准备就绪
    
    # 等待直到真正就绪或超时
    while time.time() - start_time < timeout:
        if is_truly_ready():
            return True
        time.sleep(0.5)
    
    return False  # 超时

# 使用智能等待
page.get('https://example.com/complex-page')
if smart_wait_for_page_ready(page):
    print('页面已完全准备就绪')
else:
    print('页面可能未完全加载')
```

### 条件退避等待

对于可能需要长时间等待的场景，使用指数退避策略可以减少不必要的检查：

```python
def exponential_backoff_wait(page, condition_func, max_wait=300, initial_interval=1):
    """使用指数退避策略的等待
    
    Args:
        page: 页面对象
        condition_func: 返回布尔值的条件检查函数
        max_wait: 最大等待时间（秒）
        initial_interval: 初始检查间隔（秒）
    """
    start_time = time.time()
    interval = initial_interval
    
    while time.time() - start_time < max_wait:
        if condition_func(page):
            return True
            
        # 使用指数退避，但设置上限
        wait_time = min(interval, 30)  # 最长间隔30秒
        time.sleep(wait_time)
        interval *= 2  # 每次将间隔时间翻倍
    
    return False

# 使用示例：等待电子邮件送达
def check_email_received(page):
    page.refresh()  # 刷新收件箱
    return bool(page.ele('@text*=您的订单确认'))

page.get('https://example.com/email')
if exponential_backoff_wait(page, check_email_received, max_wait=600):
    print('收到邮件')
else:
    print('未在指定时间内收到邮件')
```

### 并行等待多个条件

在某些场景下，可能需要等待多个可能的结果中的任意一个：

```python
import concurrent.futures

def wait_for_any_condition(page, conditions, timeout=30):
    """等待多个条件中的任意一个满足
    
    Args:
        page: 页面对象
        conditions: 字典，键为条件名称，值为等待函数
        timeout: 总超时时间
    
    Returns:
        满足的条件名称，或者超时返回None
    """
    def check_condition(name, func):
        try:
            result = func()
            if result:
                return name
        except:
            pass
        return None
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(conditions)) as executor:
        futures = {
            executor.submit(check_condition, name, lambda: func(page)): name 
            for name, func in conditions.items()
        }
        
        try:
            completed, _ = concurrent.futures.wait(
                futures, 
                timeout=timeout,
                return_when=concurrent.futures.FIRST_COMPLETED
            )
            
            for future in completed:
                result = future.result()
                if result:
                    return result
        except:
            pass
        
    return None

# 使用示例
def wait_for_login_result(page):
    conditions = {
        'success': lambda p: p.ele('#dashboard', timeout=0.5),
        'wrong_password': lambda p: p.ele('@text=密码错误', timeout=0.5),
        'account_locked': lambda p: p.ele('@text*=账号已锁定', timeout=0.5),
        'captcha_needed': lambda p: p.ele('#captcha-input', timeout=0.5)
    }
    
    # 提交登录表单
    page.ele('#login-button').click()
    
    # 等待任意一种结果
    result = wait_for_any_condition(page, conditions, timeout=15)
    
    if result == 'success':
        print('登录成功')
        return True
    elif result:
        print(f'登录失败: {result}')
        # 根据不同的失败原因采取不同的处理...
    else:
        print('等待登录结果超时')
    
    return False
```

## 小结

本章详细介绍了 DrissionPage 中的等待和超时处理机制，包括：

1. **显式等待**：针对特定条件的精确等待
2. **隐式等待**：全局等待设置，影响所有元素查找
3. **超时处理**：设置合适的超时时间和处理超时情况
4. **等待策略**：根据不同场景选择合适的等待方法
5. **高级技巧**：智能等待、条件退避、并行等待等

掌握这些等待机制和技巧，能够有效提高自动化脚本的稳定性和可靠性，减少因为时序问题导致的错误。合理的等待策略不仅可以确保脚本正确执行，还能优化执行效率，避免不必要的时间浪费。

在下一章中，我们将学习如何使用 DrissionPage 的下载功能，处理文件下载和上传的相关操作。 