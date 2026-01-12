# 基础页面操作

本章节将介绍 DrissionPage 中的基础页面操作，包括如何打开网页、获取页面信息以及截图等功能。

## 打开网页

DrissionPage 提供了多种方式打开网页，最常用的是通过 `get()` 方法：

```python
from DrissionPage import ChromiumPage

# 创建浏览器页面对象
page = ChromiumPage()

# 打开网页
page.get('https://www.example.com')
```

对于 SessionPage，操作方式类似：

```python
from DrissionPage import SessionPage

# 创建会话页面对象
page = SessionPage()

# 打开网页
page.get('https://www.example.com')
```

WebPage 因为同时支持两种模式，所以可以在两种模式下使用相同的接口：

```python
from DrissionPage import WebPage

# 创建网页对象（默认d模式，即驱动模式）
page = WebPage()

# 打开网页
page.get('https://www.example.com')

# 切换到s模式（会话模式）
page.change_mode()

# 同样的接口打开网页
page.get('https://www.example.com')
```

## 页面导航

DrissionPage 提供了常用的导航功能：

### 前进和后退

```python
# 后退
page.back()

# 前进
page.forward()
```

### 刷新页面

```python
page.refresh()
```

### 设置页面加载超时

```python
# 设置页面加载超时时间为10秒
page.set.load_timeout(10)
```

## 获取页面信息

DrissionPage 允许你获取当前页面的各种信息：

### 获取页面标题

```python
title = page.title
print(f'页面标题: {title}')
```

### 获取页面URL

```python
url = page.url
print(f'当前URL: {url}')
```

### 获取页面源码

```python
# 获取HTML源码
html = page.html
print(html[:100])  # 打印前100个字符
```

### 获取页面cookies

```python
# 获取当前页面的所有cookies
cookies = page.cookies
print(cookies)

# 获取指定cookie
cookie_value = page.get_cookie('cookie_name')
print(cookie_value)
```

## 页面截图

在自动化测试或开发过程中，截图是一个非常有用的功能：

### 截取整个页面

```python
# 截取整个可见页面并保存
page.screenshot('screenshot.png')
```

### 截取特定元素

```python
# 查找元素
element = page.ele('#some-element')

# 截取特定元素
element.screenshot('element.png')
```

### 自定义截图区域

```python
# 自定义截图区域 (x, y, width, height)
page.screenshot('custom.png', region=(100, 100, 500, 300))
```

## 执行JavaScript

在浏览器模式下，可以执行JavaScript代码：

```python
# 执行JavaScript并获取返回值
result = page.run_js('return document.title')
print(result)

# 修改页面内容
page.run_js('document.getElementById("example").innerHTML = "Hello DrissionPage!"')
```

## 关闭页面

使用完页面后，应该正确关闭它：

```python
# 关闭页面
page.close()
```

对于 ChromiumPage 和 WebPage 的驱动模式，这会关闭浏览器窗口。对于 SessionPage 和 WebPage 的会话模式，这会结束会话。

## 小结

通过本章节，我们学习了 DrissionPage 的基础页面操作，包括：

- 打开网页
- 页面导航（前进、后退、刷新）
- 获取页面信息（标题、URL、源码、cookies）
- 页面截图
- 执行JavaScript
- 关闭页面

这些基础操作是进行网页自动化的第一步，掌握这些操作后，我们可以进一步学习如何查找和操作页面上的元素。 