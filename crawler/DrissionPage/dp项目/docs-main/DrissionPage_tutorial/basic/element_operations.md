# 元素操作基础

找到网页元素后，我们需要对元素进行各种操作，比如点击、输入文本、获取属性等。本章将介绍 DrissionPage 提供的基础元素操作。

## 元素属性和状态获取

### 获取元素文本内容

```python
# 获取元素的文本内容
element = page.ele('h1')
text = element.text
print(f'标题文本: {text}')

# 获取元素的内部HTML
inner_html = element.html
print(f'内部HTML: {inner_html}')

# 获取元素的整个HTML（包括元素自身）
outer_html = element.outer_html
print(f'整个HTML: {outer_html}')
```

### 获取元素属性

```python
# 获取元素的特定属性
element = page.ele('a')
href = element.attr('href')
print(f'链接地址: {href}')

# 获取元素的所有属性
all_attrs = element.attrs
print('所有属性:', all_attrs)

# 检查元素是否有特定属性
has_target = element.has_attr('target')
print(f'是否有target属性: {has_target}')
```

### 获取元素位置和尺寸

```python
# 获取元素在页面上的位置坐标
location = element.location
print(f'位置: x={location["x"]}, y={location["y"]}')

# 获取元素的尺寸
size = element.size
print(f'尺寸: 宽={size["width"]}, 高={size["height"]}')

# 获取元素的视图矩形（包含位置和尺寸）
rect = element.rect
print(f'矩形: x={rect["x"]}, y={rect["y"]}, 宽={rect["width"]}, 高={rect["height"]}')
```

### 检查元素状态

```python
# 检查元素是否可见
is_visible = element.is_displayed
print(f'元素是否可见: {is_visible}')

# 检查元素是否启用
is_enabled = element.is_enabled
print(f'元素是否启用: {is_enabled}')

# 检查元素是否被选中（适用于单选框、复选框等）
is_selected = element.is_selected
print(f'元素是否被选中: {is_selected}')
```

## 元素互动操作

### 点击元素

```python
# 基本点击操作
element = page.ele('button#submit')
element.click()

# 带延迟的点击（点击后等待2秒）
element.click(2)

# 指定点击位置（元素中心点的偏移量）
element.click(offset_x=10, offset_y=5)

# 右键点击
element.right_click()

# 双击
element.double_click()
```

### 输入文本

```python
# 在输入框中输入文本
input_element = page.ele('input[name="username"]')
input_element.input('user123')

# 先清空再输入
input_element.input('user123', clear=True)

# 输入文本并按回车
input_element.input('search keyword', enter=True)

# 带延迟的输入（模拟人工输入，字符间有短暂停顿）
input_element.input('slow typing', interval=0.1)
```

### 清空输入框

```python
# 清空输入框
input_element.clear()
```

### 操作表单元素

```python
# 勾选复选框
checkbox = page.ele('input[type="checkbox"]')
checkbox.click()  # 或 checkbox.check() 在某些页面对象支持

# 选择下拉框选项（通过可见文本）
select_element = page.ele('select#country')
select_element.select('中国')  # 在某些页面对象支持

# 或者找到并点击特定选项
option = page.ele('select#country > option[value="CN"]')
option.click()
```

## 元素拖放操作

```python
# 拖动元素到指定坐标
source = page.ele('#draggable')
source.drag_to(x=200, y=300)

# 拖动元素到另一个元素
source = page.ele('#draggable')
target = page.ele('#droppable')
source.drag_to(target=target)
```

## 模拟鼠标操作

```python
# 鼠标悬停在元素上
element = page.ele('.menu-item')
element.hover()

# 模拟鼠标在元素上移动
element.move_to()

# 按住元素不放
element.press()

# 释放鼠标
element.release()
```

## 元素滚动操作

```python
# 将元素滚动到视图中
element = page.ele('#section-bottom')
element.scroll_into_view()

# 滚动到元素顶部与视图顶部对齐
element.scroll_into_view(align_top=True)

# 滚动元素内容（如果元素是可滚动容器）
container = page.ele('.scrollable-container')
container.scroll(100, 200)  # 水平滚动100像素，垂直滚动200像素
```

## 等待元素特定状态

```python
# 等待元素可见
element.wait.displayed(timeout=10)

# 等待元素不可见
element.wait.not_displayed(timeout=10)

# 等待元素可点击
element.wait.clickable(timeout=10)

# 等待元素属性包含特定值
element.wait.attr('class', 'active', timeout=10)
```

## 执行元素特定的JavaScript

```python
# 在元素上执行JavaScript
result = element.run_js('return this.innerText')
print(f'通过JS获取的文本: {result}')

# 修改元素样式
element.run_js('this.style.backgroundColor = "yellow"')

# 触发元素事件
element.run_js('this.dispatchEvent(new Event("change"))')
```

## 元素截图

```python
# 获取元素截图并保存
element.screenshot('element.png')

# 指定图片格式和质量
element.screenshot('element.jpg', quality=80)
```

## 获取子元素和父元素

```python
# 获取元素的所有子元素
children = element.children
for child in children:
    print(child.tag)

# 获取父元素
parent = element.parent
print(f'父元素标签: {parent.tag}')

# 获取指定索引的子元素
third_child = element.child(2)  # 索引从0开始
```

## 小结

本章介绍了 DrissionPage 提供的基础元素操作，包括：

- 获取元素文本、属性和状态
- 点击、输入等互动操作
- 拖放和鼠标模拟操作
- 滚动操作
- 等待元素特定状态
- 元素JavaScript操作
- 元素截图
- 访问子元素和父元素

掌握这些基础操作后，你已经能够处理大多数网页自动化场景。在下一章中，我们将深入学习表单操作的具体细节。 