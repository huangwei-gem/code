# 高级交互操作

在网页自动化中，除了基本的点击和输入操作外，有时我们需要模拟更复杂的用户交互行为，如拖拽、悬停、键盘组合键等。DrissionPage 提供了丰富的高级交互功能，让您能够精确模拟各种复杂的用户行为。本教程将详细介绍这些高级交互操作的使用方法。

## 鼠标操作

### 鼠标悬停

悬停操作是指将鼠标移动到元素上方但不点击，常用于触发下拉菜单、工具提示等交互效果：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://example.com')

# 鼠标悬停在元素上
menu_item = page.ele('#dropdown-menu')
menu_item.hover()

# 等待子菜单显示后点击子菜单项
page.wait.ele_display('.submenu-item')
page.ele('.submenu-item').click()
```

### 鼠标拖拽

拖拽操作可以用于各种场景，如滑块控件、拖放上传、排序等：

```python
# 基本拖拽：将一个元素拖到另一个元素位置
source = page.ele('#drag-source')
target = page.ele('#drop-target')
source.drag_to(target)

# 带偏移量的拖拽：将元素拖动指定的距离
slider = page.ele('#slider')
# 水平拖动100像素，垂直不变
slider.drag_to(slider, offset_x=100, offset_y=0)

# 自定义拖拽路径
source = page.ele('#drag-source')
# 先向右移动，再向下移动，最后到达目标位置
source.drag_to(
    target,
    steps=10,  # 分10步完成
    path='curved'  # 使用曲线路径
)
```

### 精确点击

有时需要点击元素的特定位置，而不是默认的中心点：

```python
# 点击元素左上角
button = page.ele('#button')
button.click(inner_offset_x=-button.rect.width/2 + 5, inner_offset_y=-button.rect.height/2 + 5)

# 点击元素右下角
button.click(inner_offset_x=button.rect.width/2 - 5, inner_offset_y=button.rect.height/2 - 5)

# 相对于页面坐标点击
page.click_at(x=100, y=200)
```

### 多次点击

双击或连续多次点击：

```python
# 双击元素
element = page.ele('#double-click-target')
element.click(2)  # 点击2次

# 三击全选文本
text_element = page.ele('#text-field')
text_element.click(3)  # 点击3次，通常用于全选文本
```

## 键盘操作

### 键盘按键

模拟键盘按键可以触发各种快捷键和操作：

```python
# 按下单个键
page.press_key('F5')  # 刷新页面

# 按下组合键
page.press_key('Ctrl+A')  # 全选
page.press_key('Ctrl+C')  # 复制
page.press_key('Ctrl+V')  # 粘贴

# 常用组合键
page.press_key('Alt+Tab')  # 切换窗口
page.press_key('Ctrl+Shift+I')  # 打开开发者工具
page.press_key('Ctrl+Shift+N')  # 打开隐身窗口
```

### 在元素上使用键盘操作

针对特定元素执行键盘操作：

```python
input_field = page.ele('#search-input')

# 聚焦元素后按键
input_field.focus()
page.press_key('Hello World')  # 输入文本
page.press_key('Enter')  # 按回车确认

# 使用键盘修改输入
input_field.input('Hello ')
page.press_key('World')
page.press_key('Ctrl+A')  # 全选文本
page.press_key('Backspace')  # 删除所选内容
```

### 模拟输入法和特殊字符

对于中文等需要使用输入法的场景或特殊字符：

```python
# 中文输入
input_field = page.ele('#name-input')
input_field.input('张三', by_js=False)  # 使用by_js=False可以支持输入法

# 输入特殊字符
message_field = page.ele('#message')
message_field.input('Hello 世界！✨🎉 Special chars: ©®™')
```

## 高级表单操作

### 文件上传

处理文件上传有多种方式：

```python
# 方法1：直接使用上传方法（推荐）
file_input = page.ele('input[type=file]')
file_input.upload('C:/path/to/file.jpg')

# 方法2：多文件上传
file_input = page.ele('input[multiple][type=file]')
file_input.upload(['C:/path/to/file1.jpg', 'C:/path/to/file2.jpg'])

# 方法3：如果上传按钮被隐藏或样式改变
# 先找到真正的input元素
file_input = page.ele('input[type=file]', timeout=0.1)
if not file_input:
    # 如果找不到，可能是隐藏的，使用JavaScript修改其可见性
    page.run_js('''
    var input = document.querySelector('input[type=file]');
    input.style.opacity = 1;
    input.style.display = 'block';
    input.style.visibility = 'visible';
    ''')
    file_input = page.ele('input[type=file]')
file_input.upload('C:/path/to/file.jpg')
```

### 操作富文本编辑器

许多网站使用富文本编辑器，如TinyMCE、CKEditor等：

```python
# 方法1：通过iframe访问编辑器（如果在iframe中）
editor_frame = page.get_frame('#editor-iframe')
editor_body = editor_frame.ele('body')
editor_body.input('Hello, this is rich text content.')

# 方法2：使用JavaScript设置内容
page.run_js('''
document.querySelector('.rich-editor').innerHTML = 'Hello, <b>bold text</b> and <i>italic text</i>.';
''')

# 方法3：操作可编辑div
editor_div = page.ele('[contenteditable=true]')
editor_div.input('Hello World')
# 添加格式化文本
editor_div.run_js('''
this.innerHTML += '<br><b>This is bold</b> and <i>this is italic</i>';
''')
```

### 处理复杂下拉菜单

现代网站中的下拉菜单通常不是标准的`<select>`元素，而是自定义实现：

```python
# 自定义下拉菜单操作
# 1. 点击打开下拉菜单
dropdown = page.ele('.custom-dropdown')
dropdown.click()

# 2. 等待下拉选项显示
page.wait.ele_display('.dropdown-options')

# 3. 点击特定选项
page.ele('.dropdown-options .option[data-value="option2"]').click()

# 或通过文本选择
page.ele('text=选项2', base_ele=page.ele('.dropdown-options')).click()
```

## 滚动操作

### 页面滚动

控制页面滚动对于加载延迟内容或操作特定区域的元素很重要：

```python
# 基本滚动
page.scroll.down(300)  # 向下滚动300像素
page.scroll.up(200)    # 向上滚动200像素

# 滚动到页面特定位置
page.scroll.to_top()     # 滚动到顶部
page.scroll.to_bottom()  # 滚动到底部
page.scroll.to(x=0, y=500)  # 滚动到指定坐标

# 平滑滚动（模拟真实用户）
page.scroll.to_bottom(smooth=True)
```

### 元素滚动

有些元素有自己的滚动条，需要单独控制：

```python
# 滚动元素使其可见
target = page.ele('#deep-content')
target.scroll.to_see()  # 滚动到元素可见

# 操作有滚动条的元素
scroll_container = page.ele('.scrollable-container')
# 在容器内滚动
scroll_container.scroll.down(200)
scroll_container.scroll.to_bottom()

# 水平滚动
scroll_container.scroll.right(100)
scroll_container.scroll.left(50)
```

### 滚动并等待加载

针对无限滚动加载的页面：

```python
# 滚动到底部并等待新内容加载
def scroll_and_wait():
    # 记录当前元素数量
    initial_count = len(page.eles('.item'))
    
    # 滚动到底部
    page.scroll.to_bottom()
    
    # 等待新元素加载
    def check_new_content():
        new_count = len(page.eles('.item'))
        return new_count > initial_count
        
    # 等待条件满足或超时
    try:
        page.wait.until(check_new_content, timeout=5)
        return True
    except:
        return False

# 连续滚动加载多页内容
items = []
for _ in range(5):  # 尝试加载5页
    # 获取当前页面的items
    items.extend([item.text for item in page.eles('.item')])
    
    # 滚动并检查是否有新内容
    if not scroll_and_wait():
        print("没有更多内容了")
        break
        
print(f"共加载了 {len(items)} 个项目")
```

## 复杂交互场景

### 拖拽排序

实现列表元素拖拽排序：

```python
from DrissionPage import ChromiumPage
import time

page = ChromiumPage()
page.get('https://example.com/sortable-list')

# 获取所有可排序的项目
items = page.eles('.sortable-item')

# 将第一项拖到最后一项之后
first_item = items[0]
last_item = items[-1]
first_item.drag_to(last_item, offset_y=10)  # 稍微偏下以确保放到后面

# 将第三项向上移动一位
items = page.eles('.sortable-item')  # 重新获取排序后的项目
items[2].drag_to(items[1], offset_y=-5)  # 稍微偏上以确保放到前面

# 验证排序结果
items = page.eles('.sortable-item')
item_texts = [item.text for item in items]
print("排序后的顺序:", item_texts)
```

### 滑块控件操作

操作滑块控件调整值：

```python
# 获取滑块元素
slider = page.ele('.slider-handle')

# 获取滑块初始位置和轨道宽度
track = page.ele('.slider-track')
track_width = track.rect.width

# 拖动到50%位置
slider.drag_to(slider, offset_x=track_width/2 - slider.rect.width/2, offset_y=0)

# 精确拖动到特定值
def move_slider_to_value(value, min_val=0, max_val=100):
    slider = page.ele('.slider-handle')
    track = page.ele('.slider-track')
    
    # 计算需要移动的距离
    track_width = track.rect.width
    value_range = max_val - min_val
    position = (value - min_val) / value_range * track_width
    
    # 计算当前位置
    current_position = slider.rect.x - track.rect.x
    
    # 计算需要拖动的距离
    offset = position - current_position
    
    # 执行拖动
    slider.drag_to(slider, offset_x=offset, offset_y=0)

# 将滑块移动到75%的位置
move_slider_to_value(75)
```

### 颜色选择器操作

操作网页中的颜色选择器：

```python
# 点击颜色选择器打开面板
color_picker = page.ele('#color-picker')
color_picker.click()

# 等待颜色面板出现
page.wait.ele_display('.color-panel')

# 方法1：点击预设颜色
page.ele('.color-swatch[data-color="#FF5733"]').click()

# 方法2：操作HSL颜色选择器
hue_slider = page.ele('.hue-slider')
# 将色相调到中间位置
hue_slider.drag_to(hue_slider, offset_x=hue_slider.rect.width/2, offset_y=0)

# 在色板上选择饱和度和亮度
color_area = page.ele('.color-area')
# 选择右上角（高饱和度，高亮度）
color_area.click(inner_offset_x=color_area.rect.width/2 - 10, inner_offset_y=-color_area.rect.height/2 + 10)

# 方法3：直接输入RGB或HEX值
hex_input = page.ele('input[data-format="hex"]')
hex_input.input('#3366FF')
```

### 复杂拖拽上传

处理需要拖拽文件到特定区域的上传功能：

```python
from DrissionPage import ChromiumPage
import os

page = ChromiumPage()
page.get('https://example.com/upload')

# 方法1：如果有隐藏的文件输入框，直接使用它
try:
    file_input = page.ele('input[type=file]', timeout=1)
    file_input.upload('C:/path/to/file.jpg')
    print("使用常规上传方法成功")
except:
    print("找不到标准文件输入框，尝试模拟拖拽...")
    
    # 方法2：使用JavaScript模拟拖拽事件
    file_path = os.path.abspath('C:/path/to/file.jpg')
    
    # 获取拖拽区域
    drop_zone = page.ele('#drop-zone')
    
    # 执行JavaScript模拟文件拖拽
    page.run_js('''
    function simulateFileDrop(dropTarget, filePath) {
        // 创建DataTransfer对象
        const dt = new DataTransfer();
        
        // 创建File对象
        const file = new File(['file content'], 'filename.jpg', {type: 'image/jpeg'});
        dt.items.add(file);
        
        // 创建拖拽事件
        const dragEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dt
        });
        
        // 分发事件
        dropTarget.dispatchEvent(dragEvent);
    }
    
    // 获取目标元素并执行拖拽
    const dropZone = document.querySelector('#drop-zone');
    simulateFileDrop(dropZone, arguments[0]);
    ''', file_path)
```

## 执行连续操作

有时需要执行一系列连续操作，模拟真实用户行为：

```python
from DrissionPage import ChromiumPage
import time
import random

def simulate_human_behavior(page):
    """模拟人类用户浏览页面的行为"""
    
    # 随机滚动
    scroll_distance = random.randint(300, 800)
    page.scroll.down(scroll_distance, smooth=True)
    time.sleep(random.uniform(1, 3))
    
    # 随机点击一个链接
    links = page.eles('tag:a')
    if links:
        random_link = random.choice(links)
        if random_link.is_displayed():
            random_link.scroll.to_see()
            time.sleep(random.uniform(0.5, 1.5))
            random_link.click()
            page.wait.load_complete()
    
    # 随机移动鼠标到某个元素上
    elements = page.eles('.hoverable')
    if elements:
        random_element = random.choice(elements)
        if random_element.is_displayed():
            random_element.scroll.to_see()
            random_element.hover()
            time.sleep(random.uniform(1, 2))
    
    # 随机查看图片
    images = page.eles('tag:img')
    if images:
        random_image = random.choice(images)
        if random_image.is_displayed():
            random_image.scroll.to_see()
            time.sleep(random.uniform(1, 3))
    
    # 回到顶部
    page.scroll.to_top(smooth=True)
    time.sleep(random.uniform(1, 2))

# 创建页面并执行模拟行为
page = ChromiumPage()
page.get('https://example.com')

# 执行多次模拟行为
for _ in range(3):
    simulate_human_behavior(page)
```

## 处理验证码

自动化过程中，经常会遇到验证码挑战：

### 处理文本验证码

```python
from DrissionPage import ChromiumPage
import pytesseract
from PIL import Image
import io
import time

page = ChromiumPage()
page.get('https://example.com/login')

# 填写登录信息
page.ele('#username').input('user123')
page.ele('#password').input('password123')

# 处理文本验证码
captcha_img = page.ele('#captcha-img')

# 方法1：手动处理
# captcha_img.save('captcha.png')
# code = input("请查看captcha.png并输入验证码: ")

# 方法2：使用OCR自动识别
img_bytes = captcha_img.get_screenshot_as_bytes()
img = Image.open(io.BytesIO(img_bytes))

# 使用pytesseract进行OCR识别
captcha_text = pytesseract.image_to_string(img, config='--psm 7')
captcha_text = ''.join(c for c in captcha_text if c.isalnum())  # 清理文本

print(f"识别到的验证码: {captcha_text}")

# 输入验证码
page.ele('#captcha-input').input(captcha_text)

# 提交表单
page.ele('#login-button').click()

# 检查登录结果
time.sleep(2)
if '验证码错误' in page.html:
    print("验证码识别错误，尝试刷新验证码重试")
    # 刷新验证码
    page.ele('#refresh-captcha').click()
    # ... 重试逻辑 ...
else:
    print("登录成功！")
```

### 处理滑块验证码

```python
from DrissionPage import ChromiumPage
import time
import random

page = ChromiumPage()
page.get('https://example.com/with-slider-captcha')

# 通用滑块验证码破解方法
def solve_slider_captcha():
    # 获取滑块和轨道
    slider = page.ele('.slider-button')
    track = page.ele('.slider-track')
    
    # 获取轨道宽度
    track_width = track.rect.width
    slider_width = slider.rect.width
    
    # 计算需要滑动的距离（通常是轨道宽度减去滑块宽度）
    distance = track_width - slider_width
    
    # 生成人类般的移动轨迹
    # 先加速，后减速，加点随机性
    tracks = []
    current = 0
    mid = distance * 4 / 5  # 前4/5加速，后1/5减速
    t = 0.2  # 时间因子
    v = 0  # 初速度
    
    while current < distance:
        if current < mid:
            a = random.uniform(2, 5)  # 加速度
        else:
            a = random.uniform(-3, -1)  # 减速度
        
        v0 = v  # 初速度
        v = v0 + a * t  # 当前速度
        move = v0 * t + 1/2 * a * t * t  # 移动距离
        current += move
        
        # 确保不超过总距离
        if current > distance:
            current = distance
        
        tracks.append(round(current))
    
    # 模拟人类拖动过程
    slider.hover()
    time.sleep(random.uniform(0.1, 0.3))
    
    # 按下鼠标
    page.action.mouse.move_to(slider)
    page.action.mouse.button_down()
    time.sleep(random.uniform(0.1, 0.3))
    
    # 拖动滑块
    for track in tracks:
        x = slider.rect.x + track
        y = slider.rect.y
        page.action.mouse.move_to((x, y))
        time.sleep(random.uniform(0.01, 0.03))
    
    # 小幅回退，模拟人类行为
    page.action.mouse.move_to((slider.rect.x + distance - random.randint(1, 3), slider.rect.y))
    time.sleep(random.uniform(0.2, 0.3))
    
    # 释放鼠标
    page.action.mouse.button_up()
    time.sleep(1)
    
    # 检查是否成功
    if page.ele('.captcha-success', timeout=3):
        return True
    return False

# 尝试解决验证码，最多尝试3次
for attempt in range(3):
    print(f"尝试解决滑块验证码 (第{attempt+1}次)")
    if solve_slider_captcha():
        print("验证码解决成功！")
        break
    else:
        print("验证码解决失败，重试...")
        # 刷新或重置验证码
        page.refresh()
        time.sleep(2)
```

## 总结

DrissionPage 提供了丰富的高级交互操作功能，使您能够精确模拟各种复杂的用户行为：

1. **鼠标操作**：悬停、拖拽、精确点击、多次点击等
2. **键盘操作**：按键、组合键、特殊字符输入等
3. **高级表单操作**：文件上传、富文本编辑器、复杂下拉菜单等
4. **滚动操作**：页面滚动、元素滚动、滚动并等待加载等
5. **复杂交互场景**：拖拽排序、滑块控件、颜色选择器、连续操作等
6. **验证码处理**：处理文本验证码和滑块验证码等

通过合理组合这些高级交互功能，您可以构建出更真实、更健壮的自动化脚本，处理各种复杂的网页操作场景。同时，适当添加随机延时和轨迹，可以让自动化操作更加自然，有效避免被网站识别为机器人。 