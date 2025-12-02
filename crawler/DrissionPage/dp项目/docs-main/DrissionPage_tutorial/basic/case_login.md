# 实战案例 - 简单网站登录

在前面的章节中，我们学习了 DrissionPage 的基础知识，包括元素查找和表单操作。现在，我们将通过一个实际案例来演示如何实现网站登录功能。

本案例将展示登录过程中的常见场景，包括分析登录页面、填写表单、处理验证码以及验证登录结果。

## 案例目标

我们的目标是登录一个简化的示例网站，完成以下步骤：

1. 打开登录页面
2. 定位并填写用户名和密码
3. 处理可能出现的验证码
4. 提交表单
5. 验证登录结果

## 准备工作

首先，我们需要导入必要的模块并创建页面对象：

```python
from DrissionPage import ChromiumPage
import time
import os

# 创建浏览器页面对象
page = ChromiumPage()
```

## 分析登录页面

在编写登录脚本前，我们需要分析登录页面的结构，了解以下信息：

1. 登录表单的位置和结构
2. 用户名和密码输入框的选择器
3. 是否有验证码及其处理方式
4. 登录按钮的选择器
5. 登录成功后的特征（如URL变化、页面元素等）

通常，我们可以使用浏览器的开发者工具来获取这些信息。

## 编写登录脚本

让我们假设登录页面的URL为`https://example.com/login`，并按步骤编写登录脚本：

### 打开登录页面

```python
# 打开登录页面
page.get('https://example.com/login')

# 等待页面加载完成
page.wait.load_complete()
```

### 定位并填写登录表单

```python
# 定位用户名输入框并填写
username_input = page.ele('#username')
username_input.input('your_username', clear=True)

# 定位密码输入框并填写
password_input = page.ele('#password')
password_input.input('your_password', clear=True)

# 勾选"记住我"（如果有）
remember_me = page.ele('#remember-me')
if remember_me and not remember_me.is_selected:
    remember_me.click()
```

### 处理验证码

对于有验证码的网站，我们需要采取适当的策略。以下是一种简单的方法：

```python
# 检查是否存在验证码
captcha_img = page.ele('#captcha-img')
if captcha_img:
    # 保存验证码图片
    captcha_path = 'captcha.png'
    captcha_img.screenshot(captcha_path)
    
    # 方法1：手动输入验证码（适用于开发测试阶段）
    print(f'验证码已保存至 {os.path.abspath(captcha_path)}')
    captcha_code = input('请查看验证码图片并输入验证码: ')
    
    # 方法2：使用OCR识别验证码（适用于自动化运行）
    # 这里需要引入适当的OCR库，比如 tesseract 或在线OCR服务
    # captcha_code = recognize_captcha(captcha_path)
    
    # 填写验证码
    captcha_input = page.ele('#captcha')
    captcha_input.input(captcha_code, clear=True)
```

### 提交表单

```python
# 点击登录按钮
login_button = page.ele('button[type="submit"]')
login_button.click()

# 或者通过表单提交
# login_form = page.ele('form#login-form')
# login_form.run_js('this.submit()')
```

### 验证登录结果

登录后，我们需要验证是否登录成功：

```python
# 方法1：检查URL变化
page.wait.url_change(timeout=5)
if 'dashboard' in page.url or 'home' in page.url:
    print('登录成功！')
else:
    # 方法2：检查页面元素
    error_message = page.ele('.error-message')
    if error_message:
        print(f'登录失败: {error_message.text}')
    else:
        # 方法3：检查特定元素是否存在（如用户头像或欢迎消息）
        user_profile = page.ele('#user-profile', timeout=3)
        if user_profile:
            print('登录成功！')
        else:
            print('登录状态未知，请手动检查')
```

## 完整实例代码

下面是整合上述步骤的完整登录脚本：

```python
from DrissionPage import ChromiumPage
import time
import os

def login_example():
    # 创建浏览器页面对象
    page = ChromiumPage()
    
    try:
        # 打开登录页面
        page.get('https://example.com/login')
        page.wait.load_complete()
        
        # 填写登录表单
        page.ele('#username').input('your_username', clear=True)
        page.ele('#password').input('your_password', clear=True)
        
        # 处理记住我选项
        remember_me = page.ele('#remember-me')
        if remember_me and not remember_me.is_selected:
            remember_me.click()
        
        # 处理验证码
        captcha_img = page.ele('#captcha-img')
        if captcha_img:
            captcha_path = 'captcha.png'
            captcha_img.screenshot(captcha_path)
            
            print(f'验证码已保存至 {os.path.abspath(captcha_path)}')
            captcha_code = input('请查看验证码图片并输入验证码: ')
            
            page.ele('#captcha').input(captcha_code, clear=True)
        
        # 点击登录按钮
        page.ele('button[type="submit"]').click()
        
        # 验证登录结果
        page.wait.url_change(timeout=5)
        
        # 检查是否有错误消息
        error_message = page.ele('.error-message', timeout=2)
        if error_message:
            print(f'登录失败: {error_message.text}')
            return False
        
        # 检查是否有成功指标
        if 'dashboard' in page.url or page.ele('#user-profile', timeout=3):
            print('登录成功！')
            return True
        else:
            print('登录状态未知，请手动检查')
            return None
    
    except Exception as e:
        print(f'登录过程发生错误: {e}')
        return False
    
    finally:
        # 保持浏览器窗口打开，以便查看结果（根据需要调整）
        input('按回车键关闭浏览器...')
        page.close()

if __name__ == '__main__':
    login_example()
```

## 处理常见登录挑战

### 处理二次验证

有些网站可能需要二次验证，如手机验证码：

```python
# 检查是否需要二次验证
if page.ele('#two-factor-auth'):
    # 点击获取验证码按钮
    page.ele('#send-code').click()
    
    # 等待用户输入收到的验证码
    verification_code = input('请输入收到的验证码: ')
    
    # 填写验证码
    page.ele('#verification-code').input(verification_code)
    
    # 点击确认按钮
    page.ele('#verify-button').click()
    
    # 等待验证完成
    page.wait.url_change(timeout=10)
```

### 处理滑块验证码

对于滑块验证码，可以使用以下方法：

```python
# 检测滑块验证码
slider = page.ele('#slider')
if slider:
    # 获取滑块位置
    slider_rect = slider.rect
    
    # 获取目标位置（这通常需要图像处理技术来确定）
    target_x = slider_rect['x'] + 150  # 示例: 向右滑动150像素
    
    # 执行拖动
    slider.drag_to(x=target_x, y=slider_rect['y'])
    
    # 等待验证结果
    page.wait(2)
```

## 登录状态保存

登录成功后，我们可能希望保存登录状态以便后续使用：

```python
# 登录成功后保存cookies
if login_success:
    # 获取当前的cookies
    cookies = page.cookies
    
    # 保存cookies到文件
    page.save_cookies('login_cookies.json')
    
    print('登录状态已保存')

# 稍后使用保存的登录状态
new_page = ChromiumPage()
new_page.load_cookies('login_cookies.json')
new_page.get('https://example.com/dashboard')
```

## 小结

通过本章的实战案例，我们学习了如何使用 DrissionPage 完成网站登录功能，包括：

1. 分析登录页面结构
2. 填写用户名和密码
3. 处理验证码
4. 验证登录结果
5. 保存登录状态

这些技能适用于各种需要登录的自动化场景，如数据爬取、自动测试和日常任务自动化。通过灵活应用 DrissionPage 的功能，你可以应对各种不同的登录流程和验证机制。 