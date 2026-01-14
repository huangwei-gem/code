# ChromiumPage 详解

ChromiumPage 是 DrissionPage 中的核心组件之一，提供了对浏览器的完整控制能力。它基于 CDP（Chrome DevTools Protocol）实现，让你能够以编程方式控制 Chromium 内核浏览器，如 Chrome、Edge 等，实现复杂的网页自动化操作。

## ChromiumPage 概述

### 特点与优势

- **完整浏览器环境**：支持 JavaScript 渲染和动态内容
- **强大的交互能力**：可以模拟鼠标、键盘等真实用户操作
- **高度自定义**：可控制浏览器的各种设置和选项
- **调试友好**：可视化操作，便于调试和问题排查
- **统一的 API**：与 SessionPage 保持一致的接口设计

### 适用场景

- 复杂的网页自动化测试
- 需要 JavaScript 渲染的网页操作
- 模拟真实用户行为的场景
- 需要处理验证码、登录等交互的场景

## 创建 ChromiumPage 对象

### 基本创建方式

```python
from DrissionPage import ChromiumPage

# 创建默认 ChromiumPage 对象
page = ChromiumPage()
```

### 使用配置文件创建

```python
# 从指定配置文件创建
page = ChromiumPage(crx_or_path='config.ini')

# 从默认配置文件创建
page = ChromiumPage(read_file=True)
```

### 高级创建选项

```python
# 使用已有 Chrome 进程
page = ChromiumPage(address_or_pi=12345)  # 使用 PID

# 详细自定义配置
page = ChromiumPage(
    # 基本设置
    chromium_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    user_data_path=r'C:\Users\Username\AppData\Local\Google\Chrome\User Data',
    cache_path=r'D:\Temp\ChromeCache',
    
    # 浏览器窗口设置
    size=(1280, 800),
    headless=False,
    
    # 代理设置
    proxy='http://127.0.0.1:7890',
    
    # 其他选项
    timeout=20,
    browser_args=['--disable-gpu']
)
```

## 浏览器控制

### 基本浏览操作

```python
# 打开网页
page.get('https://www.example.com')

# 浏览历史操作
page.back()      # 后退
page.forward()   # 前进
page.refresh()   # 刷新

# 关闭浏览器
page.close()

# 重启浏览器（保留所有设置）
page.restart()
```

### 窗口和标签页管理

```python
# 获取窗口尺寸
size = page.rect
print(f'窗口尺寸: {size}')

# 设置窗口尺寸
page.set.window.rect((0, 0, 1280, 800))  # x, y, width, height

# 窗口状态控制
page.set.window.max()       # 最大化
page.set.window.min()       # 最小化
page.set.window.normal()    # 常规大小
page.set.window.fullscreen()  # 全屏

# 创建新标签页
new_tab = page.new_tab('https://www.example.org')

# 切换标签页
tabs = page.tabs
page.switch_to.tab(1)  # 切换到第二个标签页（索引从0开始）
page.switch_to.tab('https://www.example.org')  # 根据URL切换
page.switch_to.tab(page_id='8A3D4C6B')  # 根据页面ID切换

# 关闭当前标签页
page.close_current_tab()

# 关闭指定标签页
page.close_tabs('https://www.example.org')  # 关闭匹配URL的标签页
```

### 截图功能

```python
# 获取整个页面截图
page.screenshot('full_page.png')

# 截取可视区域
page.screenshot('viewport.png', full_page=False)

# 指定区域截图 (x, y, width, height)
page.screenshot('area.png', region=(100, 100, 500, 300))

# 调整图片质量
page.screenshot('high_quality.jpg', quality=90)
```

## 页面交互高级功能

### 等待机制

ChromiumPage 提供了多种灵活的等待方式，帮助处理异步页面加载：

```python
# 等待页面加载完成
page.wait.load_complete()

# 等待导航完成
page.wait.navigation()

# 等待元素出现
page.wait.ele_appear('#dynamic-content', timeout=10)

# 等待元素消失
page.wait.ele_disappear('.loading', timeout=10)

# 等待元素可见
page.wait.ele_display('#result')

# 等待元素包含特定文本
page.wait.text_appear('操作成功')

# 等待URL变化
page.wait.url_change()

# 等待URL包含特定文本
page.wait.url_contain('success')

# 自定义等待条件
page.wait.doc_loaded(timeout=10)  # 等待文档加载完成
```

### 鼠标操作

```python
# 移动鼠标到元素上
button = page.ele('#submit-button')
button.hover()

# 或者使用绝对坐标
page.actions.mouse.move_to(x=100, y=200)

# 鼠标点击
page.actions.mouse.click()

# 右键点击
page.actions.mouse.right_click()

# 双击
page.actions.mouse.double_click()

# 拖拽操作
source = page.ele('#drag-item')
target = page.ele('#drop-zone')
source.drag_to(target=target)

# 或者使用坐标
source.drag_to(x=500, y=300)
```

### 键盘操作

```python
# 按键输入
page.actions.keyboard.input('Hello DrissionPage!')

# 组合键
page.actions.keyboard.shortcuts('ctrl+a')  # 全选
page.actions.keyboard.shortcuts('ctrl+c')  # 复制

# 特殊键
page.actions.keyboard.press('Enter')
page.actions.keyboard.press('Tab')
page.actions.keyboard.press('Escape')

# 按下并释放
page.actions.keyboard.press_down('Shift')
page.actions.keyboard.input('UPPERCASE')
page.actions.keyboard.press_up('Shift')
```

### 滚动操作

```python
# 滚动到页面底部
page.scroll.to_bottom()

# 滚动到页面顶部
page.scroll.to_top()

# 滚动到特定元素
element = page.ele('#target-section')
element.scroll_into_view()

# 水平和垂直滚动
page.scroll.to_location(x=0, y=500)

# 滚动一定距离
page.scroll.down(300)  # 向下滚动300像素
page.scroll.up(200)    # 向上滚动200像素
page.scroll.right(100) # 向右滚动100像素
page.scroll.left(50)   # 向左滚动50像素
```

### 文件上传

```python
# 基本文件上传
file_input = page.ele('input[type="file"]')
file_input.input(r'C:\path\to\file.jpg')

# 多文件上传
file_input.input([r'C:\path\to\file1.jpg', r'C:\path\to\file2.jpg'])

# 处理隐藏的文件输入框
hidden_file_input = page.ele('input[type="file"]', show=True)
hidden_file_input.input(r'C:\path\to\file.jpg')
```

### 弹窗处理

```python
# 自动接受所有弹窗
page.set.auto_handle_alert(True)

# 手动处理弹窗
alert = page.get_alert()
if alert:
    print(f'弹窗文本: {alert.text}')
    alert.accept()  # 点击确定
    # 或
    alert.dismiss()  # 点击取消
    # 输入文本（如果是 prompt 类型）
    alert.input('输入内容')
```

### 执行 JavaScript

```python
# 基本JS执行
result = page.run_js('return document.title')
print(f'页面标题: {result}')

# 在元素上下文中执行
button = page.ele('#my-button')
button.run_js('this.style.backgroundColor = "red"')

# 传递参数给JS
page.run_js('console.log(arguments[0])', 'Hello from Python')

# 执行复杂脚本
js_code = """
let elements = document.querySelectorAll('.item');
let results = [];
elements.forEach(el => {
    results.push({
        text: el.textContent,
        href: el.getAttribute('href')
    });
});
return results;
"""
items = page.run_js(js_code)
for item in items:
    print(f"Text: {item['text']}, Link: {item['href']}")
```

## 网络控制与监听

### 网络请求拦截

```python
# 拦截所有图片请求
page.set.blocking_rules(['*.jpg', '*.png', '*.gif'])

# 只允许特定域名的请求
page.set.blocking_rules(['*'], ['*.example.com/*'])

# 清除拦截规则
page.set.blocking_rules([])
```

### 网络监听

```python
# 启用网络监听
page.listen.start()

# 获取最近的请求
requests = page.listen.requests
for req in requests:
    print(f"URL: {req.url}, Method: {req.method}")

# 获取最近的响应
responses = page.listen.responses
for resp in responses:
    print(f"URL: {resp.url}, Status: {resp.status}")

# 等待特定请求完成
page.listen.wait_request('api/data', timeout=10)

# 停止监听
page.listen.stop()
```

### Cookie 管理

```python
# 获取所有cookies
cookies = page.cookies
print(cookies)

# 获取特定cookie
session_id = page.get_cookie('session_id')
print(f'Session ID: {session_id}')

# 添加cookie
page.add_cookies([{
    'name': 'user_id',
    'value': '12345',
    'domain': 'example.com'
}])

# 删除cookie
page.del_cookies('session_id')

# 清除所有cookies
page.clear_cookies()

# 保存cookies到文件
page.save_cookies('cookies.json')

# 从文件加载cookies
page.load_cookies('cookies.json')
```

## 高级浏览器配置

### 浏览器参数配置

```python
# 创建时配置
page = ChromiumPage(
    browser_args=[
        '--disable-gpu',
        '--disable-extensions',
        '--no-sandbox',
        '--disable-dev-shm-usage'
    ]
)

# 通过配置文件配置
"""
# config.ini 示例
[chromium]
browser_options = --disable-gpu
                  --disable-extensions
                  --no-sandbox
"""
```

### User Agent 设置

```python
# 设置User Agent
page.set.user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
```

### 代理设置

```python
# 设置代理
page.set.proxy('http://127.0.0.1:7890')

# 使用带认证的代理
page.set.proxy('http://username:password@127.0.0.1:7890')

# 移除代理
page.set.proxy(None)
```

### 设备模拟

```python
# 模拟移动设备
page.set.device('iPhone X')

# 自定义设备参数
page.set.device({
    'width': 375,
    'height': 812,
    'device_scale_factor': 3,
    'mobile': True,
    'user_agent': 'Custom iPhone User Agent'
})

# 恢复为桌面模式
page.set.device(None)
```

## 调试技巧

### 开发者工具

```python
# 打开开发者工具
page.set.activate_developer_tools()
```

### 日志记录

```python
# 启用控制台日志记录
page.set.log_level('info')  # 可选: 'debug', 'info', 'warning', 'error'

# 获取控制台日志
logs = page.get_console_log()
for log in logs:
    print(f"[{log['level']}] {log['text']}")
```

### 保存页面

```python
# 保存当前页面HTML到文件
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(page.html)

# 保存页面为PDF
page.save_as_pdf('page.pdf')

# 保存页面为MHTML (包含图片等资源)
page.save_as_mhtml('page.mhtml')
```

## 实用案例

### 处理复杂登录

```python
# 完整登录流程示例
from DrissionPage import ChromiumPage

def login_with_verification():
    page = ChromiumPage()
    page.get('https://example.com/login')
    
    # 填写登录表单
    page.ele('#username').input('user123')
    page.ele('#password').input('password123')
    
    # 点击登录按钮
    page.ele('#login-button').click()
    
    # 处理可能出现的验证码
    captcha = page.ele('#captcha-img', timeout=3)
    if captcha:
        # 保存验证码图片
        captcha.screenshot('captcha.png')
        
        # 手动输入验证码（示例）
        code = input('请输入验证码: ')
        page.ele('#captcha-input').input(code)
        page.ele('#verify-button').click()
    
    # 处理可能的二次验证
    two_factor = page.ele('#two-factor-auth', timeout=3)
    if two_factor:
        # 等待短信验证码
        sms_code = input('请输入短信验证码: ')
        page.ele('#sms-code').input(sms_code)
        page.ele('#verify-sms').click()
    
    # 等待登录成功
    page.wait.ele_appear('#user-profile', timeout=10)
    print('登录成功!')
    
    # 保存登录状态
    page.save_cookies('login_cookies.json')
    
    return page

# 使用保存的登录状态
def use_saved_login():
    page = ChromiumPage()
    page.load_cookies('login_cookies.json')
    page.get('https://example.com/dashboard')
    
    # 验证登录状态
    if page.ele('#user-profile'):
        print('成功使用保存的登录状态!')
    else:
        print('登录状态已失效，需要重新登录')
        page = login_with_verification()
    
    return page
```

### 无头模式下的文件下载

```python
from DrissionPage import ChromiumPage
import time
import os

def download_file():
    # 配置下载路径
    download_path = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_path, exist_ok=True)
    
    # 创建页面对象，设置下载路径
    page = ChromiumPage(download_path=download_path)
    
    # 打开下载页面
    page.get('https://example.com/download')
    
    # 查找并点击下载按钮
    download_button = page.ele('#download-button')
    download_button.click()
    
    # 等待下载开始
    page.wait.download_begin(timeout=10)
    
    # 等待下载完成
    status = page.wait.download_complete(timeout=60)
    
    if status == 'complete':
        print('文件下载成功!')
        # 获取最后下载的文件名
        files = os.listdir(download_path)
        if files:
            latest_file = max([os.path.join(download_path, f) for f in files], key=os.path.getctime)
            print(f'下载文件: {latest_file}')
            return latest_file
    else:
        print(f'下载失败，状态: {status}')
        return None
```

## 小结

ChromiumPage 提供了丰富的浏览器控制能力，可以满足从简单网页访问到复杂自动化测试的各种需求。其主要优势包括：

1. 完整支持 JavaScript 和动态内容
2. 真实的用户交互模拟（鼠标、键盘操作）
3. 强大的网络监控和控制能力
4. 灵活的等待机制，适应各种异步加载情况
5. 与 SessionPage 共享一致的 API 设计

尽管 ChromiumPage 在资源消耗上比 SessionPage 更重，但在处理复杂网页交互、模拟真实用户操作和自动化测试等场景时，它的优势是不可替代的。

在下一章中，我们将介绍 WebPage 对象，它集成了 SessionPage 和 ChromiumPage 的功能，提供了两种模式间无缝切换的能力。 