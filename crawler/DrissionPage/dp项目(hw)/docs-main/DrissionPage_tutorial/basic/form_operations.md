# 表单操作

表单操作是网页自动化中最常见的任务之一，包括填写文本框、选择下拉菜单、勾选复选框、上传文件等。本章将详细介绍如何使用 DrissionPage 处理各种表单操作。

## 文本输入框操作

### 基本输入操作

```python
# 找到输入框元素
username_input = page.ele('#username')
password_input = page.ele('#password')

# 输入文本
username_input.input('user123')
password_input.input('password123')
```

### 清空输入框

```python
# 清空输入框后再输入
username_input.clear()
username_input.input('new_user')

# 或者使用input方法的clear参数
password_input.input('new_password', clear=True)
```

### 特殊输入情况

```python
# 模拟人类输入（字符之间有随机延迟）
username_input.input('slow_typing_user', interval=0.1)

# 输入后按回车键
search_input = page.ele('#search-box')
search_input.input('search keyword', enter=True)

# 处理有掩码的密码框
password_input.input('password123', clear=True)
```

## 单选框和复选框操作

### 复选框操作

```python
# 找到复选框
remember_me = page.ele('#remember')

# 获取复选框状态
if not remember_me.is_selected:
    # 如果未选中，则点击选中
    remember_me.click()

# 取消选中
if remember_me.is_selected:
    remember_me.click()
```

### 单选框操作

```python
# 找到单选框组
gender_male = page.ele('#gender-male')
gender_female = page.ele('#gender-female')

# 选择"男性"选项
gender_male.click()

# 检查是否选中
is_selected = gender_male.is_selected
print(f'男性选项是否选中: {is_selected}')
```

## 下拉菜单操作

### 基本下拉菜单选择

```python
# 找到下拉菜单
country_select = page.ele('#country')

# 方法1：直接选择选项（某些页面对象支持）
country_select.select('中国')  # 通过可见文本选择

# 方法2：找到选项并点击
china_option = page.ele('#country > option[value="CN"]')
china_option.click()

# 方法3：使用JavaScript选择
page.run_js('document.querySelector("#country").value = "CN"')
```

### 处理高级下拉菜单（非原生select元素）

```python
# 点击下拉菜单触发显示选项
dropdown = page.ele('.custom-select')
dropdown.click()

# 等待选项显示
page.wait.ele_display('.dropdown-options')

# 点击特定选项
option = page.ele('.dropdown-options > .option@text=中国')
option.click()
```

## 文件上传

### 基本文件上传

```python
# 找到文件上传输入框
file_input = page.ele('input[type="file"]')

# 上传文件（指定文件路径）
file_input.input(r'C:\path\to\file.jpg')

# 上传多个文件
file_input.input([r'C:\path\to\file1.jpg', r'C:\path\to\file2.jpg'])
```

### 处理隐藏的文件上传输入框

```python
# 如果文件输入框被隐藏（常见于美化的上传界面）
hidden_file_input = page.ele('input[type="file"]', timeout=2)
if hidden_file_input:
    # 使文件输入框可见
    page.run_js('document.querySelector("input[type=\\"file\\"]").style.opacity = "1"')
    page.run_js('document.querySelector("input[type=\\"file\\"]").style.display = "block"')
    
    # 然后上传文件
    hidden_file_input.input(r'C:\path\to\file.jpg')
```

### 处理拖放上传界面

```python
# 找到拖放区域
drop_zone = page.ele('#dropzone')

# 使用 JavaScript 模拟文件拖放（这是一种可能的方法，具体取决于网站实现）
js_code = """
var dt = new DataTransfer();
var file = new File(['file content'], 'example.txt', {type: 'text/plain'});
dt.items.add(file);

var event = new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dt});
arguments[0].dispatchEvent(event);
"""
drop_zone.run_js(js_code)
```

## 表单提交

### 点击提交按钮

```python
# 找到提交按钮
submit_button = page.ele('button[type="submit"]')
# 或者
submit_button = page.ele('input[type="submit"]')

# 点击提交
submit_button.click()
```

### 通过回车键提交

```python
# 在最后一个输入框中按回车提交表单
last_input = page.ele('input:last-of-type')
last_input.input('some text', enter=True)
```

### 通过JavaScript提交表单

```python
# 找到表单
form = page.ele('form#login-form')

# 使用JavaScript提交
form.run_js('this.submit()')

# 或者在页面级别执行
page.run_js('document.querySelector("form#login-form").submit()')
```

## 处理动态表单和验证

### 处理表单验证错误

```python
# 提交表单
submit_button.click()

# 等待并检查错误消息
error_msg = page.ele('.error-message', timeout=3)
if error_msg:
    print(f'表单验证错误: {error_msg.text}')
    # 修正错误并重新提交
```

### 处理动态变化的表单

```python
# 选择某个选项后会动态显示其他字段
option = page.ele('input[value="other"]')
option.click()

# 等待新字段出现
page.wait.ele_display('#other-field')

# 在新显示的字段中输入
other_field = page.ele('#other-field')
other_field.input('Custom value')
```

## 处理验证码

### 简单验证码处理（适用于固定验证码或测试环境）

```python
# 找到验证码图片
captcha_img = page.ele('#captcha-img')

# 获取验证码图片并保存
captcha_img.screenshot('captcha.png')

# 手动或使用OCR识别验证码
# ...

# 输入验证码
captcha_input = page.ele('#captcha')
captcha_input.input('识别出的验证码')
```

### 刷新验证码

```python
# 点击刷新验证码按钮
refresh_btn = page.ele('#refresh-captcha')
refresh_btn.click()

# 等待新验证码加载
page.wait(1)  # 简单等待1秒
```

## 完整表单操作示例

下面是一个完整的表单填写示例：

```python
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 打开登录页面
page.get('https://example.com/login')

# 填写用户名和密码
page.ele('#username').input('user123', clear=True)
page.ele('#password').input('password123', clear=True)

# 勾选"记住我"
remember_me = page.ele('#remember')
if not remember_me.is_selected:
    remember_me.click()

# 选择用户类型
page.ele('#user-type').select('企业用户')

# 处理验证码（如果有）
captcha_img = page.ele('#captcha-img')
if captcha_img:
    # 保存验证码图片
    captcha_img.screenshot('captcha.png')
    # 假设我们已经识别出验证码为"A1B2"
    page.ele('#captcha').input('A1B2')

# 提交表单
page.ele('button[type="submit"]').click()

# 等待登录成功
page.wait.title_contains('首页', timeout=10)
print('登录成功！')
```

## 小结

本章介绍了使用 DrissionPage 进行表单操作的各种方法，包括：

- 文本输入框操作
- 单选框和复选框操作
- 下拉菜单选择
- 文件上传处理
- 表单提交
- 处理动态表单和验证
- 验证码处理

通过这些基础操作，你可以处理大多数网站的表单交互需求。下一章我们将通过一个完整的案例，演示如何实现网站登录功能。 