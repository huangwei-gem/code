# 异常处理与调试

在进行网页自动化的过程中，各种异常情况不可避免。DrissionPage 提供了丰富的异常处理和调试机制，帮助开发者诊断和解决问题。本文将详细介绍如何有效处理异常并进行调试，提高自动化脚本的稳定性和可维护性。

## 常见异常类型

在使用 DrissionPage 时，可能会遇到以下几类常见异常：

### 1. 页面加载异常

```python
# 捕获页面加载超时异常
try:
    page.get('https://example.com')
except TimeoutError:
    print('页面加载超时')
```

### 2. 元素查找异常

```python
# 捕获元素未找到异常
try:
    element = page.ele('#non-existent-element', timeout=3)
except ElementNotFoundError:
    print('元素未找到')
```

### 3. 操作执行异常

```python
# 捕获元素操作异常
try:
    element = page.ele('#some-element')
    element.click()
except (ElementClickError, ElementOperationError) as e:
    print(f'元素操作失败: {e}')
```

### 4. JavaScript 执行异常

```python
# 捕获 JavaScript 执行异常
try:
    result = page.run_script('return document.querySelector("#element").innerText;')
except JavaScriptErrorException as e:
    print(f'JavaScript 执行错误: {e}')
```

### 5. 网络请求异常

```python
# 捕获网络请求异常
try:
    page = SessionPage()
    page.get('https://example.com/api')
except RequestsError as e:
    print(f'网络请求错误: {e}')
```

## 异常处理最佳实践

### 1. 使用 try-except 块进行精细异常捕获

```python
from DrissionPage import ChromiumPage, ElementNotFoundError, TimeoutError

page = ChromiumPage()
try:
    page.get('https://example.com')
    element = page.ele('#login-button')
    element.click()
except TimeoutError:
    print('页面加载超时')
except ElementNotFoundError:
    print('登录按钮未找到')
except Exception as e:
    print(f'其他异常: {e}')
```

### 2. 实现重试机制

```python
def retry_operation(func, max_retries=3, delay=1):
    """实现重试机制的装饰器"""
    import time
    from functools import wraps
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"操作失败，正在重试 ({attempt+1}/{max_retries})...")
                time.sleep(delay)
    return wrapper

@retry_operation
def login(page, username, password):
    page.get('https://example.com/login')
    page.ele('#username').input(username)
    page.ele('#password').input(password)
    page.ele('#login-button').click()
```

### 3. 使用上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def safe_operation():
    try:
        yield
    except ElementNotFoundError:
        print('元素未找到')
    except TimeoutError:
        print('操作超时')
    except Exception as e:
        print(f'发生异常: {e}')

# 使用上下文管理器
with safe_operation():
    page.get('https://example.com')
    page.ele('#login-button').click()
```

### 4. 优雅地处理预期异常

```python
# 使用 ele_exists 方法避免异常
if page.ele_exists('#popup-dialog'):
    page.ele('#close-button').click()

# 使用 ele_if_exists 方法安全地获取元素
element = page.ele_if_exists('#optional-element')
if element:
    element.click()
```

## 调试技巧

### 1. 使用内置的调试方法

DrissionPage 提供了丰富的调试方法，帮助开发者诊断问题：

```python
# 打印页面源码
print(page.html)

# 获取当前 URL
print(page.url)

# 获取页面标题
print(page.title)

# 获取元素状态
element = page.ele('#some-button')
print(f'元素可见性: {element.is_displayed()}')
print(f'元素是否启用: {element.is_enabled()}')
print(f'元素是否选中: {element.is_selected()}')
```

### 2. 使用截图功能

截图是调试网页自动化脚本的有力工具，可以帮助开发者了解页面状态：

```python
# 获取页面截图
page.get_screenshot('debug_screenshot.png')

# 获取元素截图
element = page.ele('#login-form')
element.get_screenshot('element_screenshot.png')
```

### 3. 使用开发者工具

在使用 ChromiumPage 时，可以启用开发者工具进行调试：

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 配置启用开发者工具
co = ChromiumOptions()
co.set_argument('--auto-open-devtools-for-tabs')
page = ChromiumPage(co)
page.get('https://example.com')
```

### 4. 插入调试点

在关键操作前后插入调试点，便于观察页面状态：

```python
def debug_point(page, message):
    """调试点函数"""
    print(f"[DEBUG] {message}")
    print(f"当前 URL: {page.url}")
    print(f"页面标题: {page.title}")
    page.get_screenshot(f"debug_{message.replace(' ', '_').lower()}.png")
    input("按 Enter 继续...")

# 使用调试点
debug_point(page, "登录前")
page.ele('#username').input('test_user')
page.ele('#password').input('test_pass')
page.ele('#login-button').click()
debug_point(page, "登录后")
```

### 5. 使用日志记录

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("DrissionPage")

# 使用日志记录操作
try:
    page.get('https://example.com')
    logger.info("页面加载成功")
    
    element = page.ele('#login-button')
    logger.debug(f"找到登录按钮: {element}")
    
    element.click()
    logger.info("点击登录按钮")
except Exception as e:
    logger.error(f"发生错误: {e}", exc_info=True)
```

## 高级调试技术

### 1. 网络流量监控

监控网络请求对于调试复杂应用尤为重要：

```python
# 启用网络监听
page = ChromiumPage()
page.get('https://example.com')

# 开始记录网络请求
page.listen.start()

# 执行操作
page.ele('#search-button').click()

# 获取网络请求数据
requests = page.listen.requests
for req in requests:
    if 'api' in req.url:
        print(f"请求 URL: {req.url}")
        print(f"请求方法: {req.method}")
        print(f"请求头: {req.headers}")
        if req.body:
            print(f"请求体: {req.body}")
        
        if req.response:
            print(f"响应状态: {req.response.status}")
            print(f"响应体: {req.response.body}")
```

### 2. 性能分析

```python
import time

# 简单的性能计时器
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def search_product(page, keyword):
    page.ele('#search-input').input(keyword)
    page.ele('#search-button').click()
    page.wait.load_complete()
    return page.eles('.product-item')
```

### 3. 使用执行跟踪

```python
def trace_execution(func):
    """执行跟踪装饰器"""
    def wrapper(*args, **kwargs):
        print(f"开始执行 {func.__name__}")
        print(f"参数: {args}, {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} 执行成功")
            return result
        except Exception as e:
            print(f"{func.__name__} 执行失败: {e}")
            raise
    return wrapper

@trace_execution
def login(page, username, password):
    page.ele('#username').input(username)
    page.ele('#password').input(password)
    page.ele('#login-button').click()
```

## 日志管理

### 1. 配置日志系统

```python
import logging
import os
from datetime import datetime

# 创建日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 配置日志格式和输出
def setup_logger(name, level=logging.INFO):
    log_file = os.path.join(log_dir, f"{name}_{datetime.now().strftime('%Y%m%d')}.log")
    
    # 创建 logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 文件处理器
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # 格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 使用示例
logger = setup_logger("web_automation")
logger.info("自动化脚本启动")
```

### 2. 分级日志记录

```python
# 请求日志记录器
request_logger = setup_logger("requests", logging.DEBUG)

# 业务逻辑日志记录器
business_logger = setup_logger("business", logging.INFO)

# 错误日志记录器
error_logger = setup_logger("errors", logging.ERROR)

try:
    # 记录请求日志
    request_logger.debug(f"请求 URL: {page.url}")
    
    # 记录业务逻辑
    business_logger.info("开始登录流程")
    
    # 执行操作
    page.ele('#username').input('test_user')
    page.ele('#password').input('test_pass')
    page.ele('#login-button').click()
    
    business_logger.info("登录成功")
except Exception as e:
    # 记录错误
    error_logger.error(f"登录过程中发生错误", exc_info=True)
    raise
```

### 3. 日志轮转

对于长时间运行的自动化脚本，建议使用日志轮转功能：

```python
import logging
from logging.handlers import RotatingFileHandler

# 配置轮转日志
def setup_rotating_logger(name, level=logging.INFO):
    log_file = f"logs/{name}.log"
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 设置轮转文件处理器，最大 10MB，保留 5 个备份
    handler = RotatingFileHandler(
        log_file, maxBytes=10*1024*1024, backupCount=5
    )
    handler.setLevel(level)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# 使用轮转日志
logger = setup_rotating_logger("automation")
```

## 调试工具整合

DrissionPage 可以与多种调试工具整合，提升调试效率：

### 1. 与 pdb 集成

```python
import pdb

page = ChromiumPage()
page.get('https://example.com')

# 在关键点插入断点
element = page.ele('#login-form')
if not element:
    pdb.set_trace()  # 进入交互式调试
```

### 2. 与 ipdb 集成（增强版 pdb）

```python
# 安装: pip install ipdb
import ipdb

# 在关键点插入断点
try:
    element = page.ele('#login-button')
    element.click()
except Exception:
    ipdb.post_mortem()  # 异常发生时进入调试
```

### 3. 与 VS Code 调试器集成

在 VS Code 中，可以设置断点并使用内置调试器进行调试：

```python
# 在 VS Code 中设置断点
page = ChromiumPage()
page.get('https://example.com')  # 可以在这里设置断点

# 执行操作
element = page.ele('#username')
element.input('test_user')  # 可以在这里设置断点
```

## 故障排除清单

在遇到问题时，可以按照以下清单进行检查：

1. **页面加载问题**
   - 检查网络连接
   - 确认 URL 是否正确
   - 检查页面加载超时设置

2. **元素查找问题**
   - 确认选择器是否正确
   - 检查元素是否在 iframe 中
   - 检查元素是否在 Shadow DOM 中
   - 检查页面是否完全加载
   - 检查元素是否是动态生成的

3. **元素操作问题**
   - 确认元素是否可见
   - 确认元素是否可交互
   - 检查元素是否被覆盖

4. **JavaScript 执行问题**
   - 检查 JavaScript 语法
   - 确认所需的变量和函数是否存在

5. **浏览器控制问题**
   - 检查浏览器路径配置
   - 确认启动参数是否正确
   - 检查浏览器版本兼容性

## 调试案例分析

### 案例一：登录失败调试

```python
from DrissionPage import ChromiumPage, ElementNotFoundError

# 创建调试日志
logger = setup_logger("login_debug", logging.DEBUG)

def debug_login(username, password):
    page = ChromiumPage()
    try:
        # 记录开始
        logger.debug("开始登录调试")
        
        # 打开登录页面
        page.get('https://example.com/login')
        logger.debug(f"当前 URL: {page.url}")
        page.get_screenshot("login_page.png")
        
        # 尝试查找用户名输入框
        try:
            username_input = page.ele('#username', timeout=5)
            logger.debug("找到用户名输入框")
        except ElementNotFoundError:
            logger.error("未找到用户名输入框")
            logger.debug(f"页面源码: {page.html}")
            raise
        
        # 输入用户名
        username_input.input(username)
        logger.debug(f"输入用户名: {username}")
        
        # 尝试查找密码输入框
        try:
            password_input = page.ele('#password', timeout=5)
            logger.debug("找到密码输入框")
        except ElementNotFoundError:
            logger.error("未找到密码输入框")
            raise
        
        # 输入密码
        password_input.input(password)
        logger.debug("输入密码")
        
        # 尝试查找登录按钮
        try:
            login_button = page.ele('#login-button', timeout=5)
            logger.debug("找到登录按钮")
        except ElementNotFoundError:
            logger.error("未找到登录按钮")
            raise
        
        # 点击登录按钮
        login_button.click()
        logger.debug("点击登录按钮")
        
        # 等待登录结果
        page.wait.load_complete()
        logger.debug(f"登录后 URL: {page.url}")
        page.get_screenshot("after_login.png")
        
        # 检查登录结果
        if page.ele_exists('.error-message'):
            error_msg = page.ele('.error-message').text
            logger.error(f"登录失败，错误信息: {error_msg}")
            return False
        
        if page.ele_exists('.user-profile'):
            logger.debug("登录成功")
            return True
        
        logger.warning("无法确定登录状态")
        return None
    
    except Exception as e:
        logger.error(f"登录过程中发生异常: {e}", exc_info=True)
        raise
    finally:
        # 确保记录页面最终状态
        logger.debug(f"最终 URL: {page.url}")
        logger.debug(f"页面标题: {page.title}")
        page.get_screenshot("final_state.png")

# 使用调试函数
result = debug_login('test_user', 'test_password')
```

### 案例二：网络请求调试

```python
from DrissionPage import ChromiumPage

def debug_api_request():
    page = ChromiumPage()
    page.get('https://example.com')
    
    # 开始记录网络请求
    page.listen.start()
    
    print("触发 API 请求...")
    page.ele('#data-button').click()
    
    # 等待请求完成
    page.wait.load_complete()
    
    # 分析网络请求
    for req in page.listen.requests:
        if 'api/data' in req.url:
            print(f"\n找到目标请求: {req.url}")
            print(f"请求方法: {req.method}")
            print(f"请求头:")
            for key, value in req.headers.items():
                print(f"  {key}: {value}")
            
            if req.body:
                print(f"请求体: {req.body}")
            
            if req.response:
                print(f"响应状态: {req.response.status}")
                print(f"响应头:")
                for key, value in req.response.headers.items():
                    print(f"  {key}: {value}")
                
                print(f"响应体: {req.response.body}")
            
            # 复制请求到 curl 命令
            headers_str = ' '.join([f'-H "{k}: {v}"' for k, v in req.headers.items()])
            body_str = f"-d '{req.body}'" if req.body else ""
            curl_cmd = f"curl -X {req.method} {headers_str} {body_str} '{req.url}'"
            print(f"\n调试用 curl 命令:\n{curl_cmd}")
            
            return

    print("未找到目标 API 请求")

# 执行调试
debug_api_request()
```

## 小结

有效的异常处理和调试技巧是成功进行网页自动化的关键。通过本文介绍的方法，你可以：

1. 识别和处理常见异常类型
2. 使用最佳实践进行异常处理
3. 掌握各种调试技巧和工具
4. 实现高效的日志管理
5. 与第三方调试工具整合
6. 系统地排除故障

随着经验的积累，你将能够更快地识别问题并找到解决方案，使自动化脚本更加稳定和可靠。 