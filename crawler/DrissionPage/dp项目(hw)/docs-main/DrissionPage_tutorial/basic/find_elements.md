# 元素查找基础

在网页自动化中，找到正确的元素是首要任务。DrissionPage 提供了多种强大而灵活的方法来查找页面元素。

## 元素查找方法概览

DrissionPage 支持以下主要查找方法：

1. CSS 选择器查找
2. XPath 查找
3. 文本和属性查找
4. 组合查找

每个页面对象（ChromiumPage、SessionPage、WebPage）都提供了两类查找方法：
- `ele()`: 查找单个元素，找不到则返回 `None`
- `eles()`: 查找所有匹配的元素，返回元素列表

## CSS 选择器查找

CSS 选择器是最常用的元素查找方式之一，语法简洁，易于理解。

### 基本使用

```python
# 通过ID查找元素
element = page.ele('#login-button')

# 通过class查找元素
element = page.ele('.container')

# 通过标签名查找元素
element = page.ele('div')

# 组合选择器
element = page.ele('div.container > p.content')

# 查找所有匹配元素
elements = page.eles('li.item')
```

### 使用属性选择器

```python
# 查找具有特定属性的元素
element = page.ele('[data-test="login"]')

# 查找属性值包含特定文本的元素
element = page.ele('[href*="example"]')

# 查找属性值以特定文本开头的元素
element = page.ele('[class^="btn-"]')
```

## XPath 查找

XPath 提供了强大的查询能力，特别是处理复杂结构时。

### 基本使用

```python
# 绝对路径查找
element = page.ele('xpath://html/body/div/main')

# 相对路径查找
element = page.ele('xpath://div[@id="container"]')

# 查找文本包含特定内容的元素
element = page.ele('xpath://button[contains(text(), "登录")]')

# 使用属性查找
element = page.ele('xpath://input[@name="username"]')
```

### 高级 XPath 技巧

```python
# 查找具有多个条件的元素
element = page.ele('xpath://div[@class="item" and @data-id="123"]')

# 查找父元素
element = page.ele('xpath://span[@class="highlight"]/parent::div')

# 使用索引查找第n个元素
element = page.ele('xpath://ul/li[3]')  # 查找第3个li元素
```

## 通过文本和属性查找

DrissionPage 提供了便捷的方法直接通过文本或属性查找元素。

### 通过文本查找

```python
# 精确匹配文本
element = page.ele('@text=登录')

# 包含文本
element = page.ele('@text*=用户名')

# 以某文本开头
element = page.ele('@text^=欢迎')

# 以某文本结尾
element = page.ele('@text$=系统')
```

### 通过属性查找

```python
# 精确匹配属性
element = page.ele('@href=https://www.example.com')

# 属性包含某值
element = page.ele('@class*=button')

# 属性以某值开头
element = page.ele('@id^=user-')

# 属性以某值结尾
element = page.ele('@src$=.png')
```

## 组合查找策略

DrissionPage 允许混合使用多种查找策略，提高查找精准度。

```python
# 组合CSS和文本查找
element = page.ele('.button@text=登录')

# 组合XPath和文本查找
element = page.ele('xpath://div[@class="navbar"]@text*=首页')

# 多重属性查询
element = page.ele('@title=提示@class*=info')
```

## 链式查找

链式查找允许你从已找到的元素继续查找其子元素。

```python
# 先找到容器，再在容器中查找子元素
container = page.ele('#content')
item = container.ele('.item')

# 一行链式查找
item = page.ele('#content').ele('.item')

# 多层链式查找
text = page.ele('#main').ele('.container').ele('p.description').text
```

## 超时和等待

设置合理的查找超时可以处理动态加载的页面：

```python
# 设置查找超时为10秒
element = page.ele('#loading-content', timeout=10)

# 对整个页面设置查找超时（影响所有ele和eles调用）
page.set.ele_timeout(10)
```

## 处理查找失败

优雅地处理元素查找失败：

```python
try:
    element = page.ele('#non-existent', raise_err=True)  # 找不到元素会抛出异常
except:
    print("Element not found")

# 或者使用默认方式，不抛出异常
element = page.ele('#non-existent')
if element is None:
    print("Element not found")
```

## 查找结果处理

```python
# 检查元素是否存在
if page.ele('#notification'):
    print("Notification exists")

# 获取所有匹配元素的数量
count = len(page.eles('li.item'))
print(f"Found {count} items")

# 遍历所有匹配元素
for item in page.eles('.product'):
    print(item.text)
```

## 小结

本章介绍了 DrissionPage 中的基础元素查找方法，包括：

- CSS 选择器查找
- XPath 查找
- 文本和属性查找
- 组合查找策略
- 链式查找
- 超时处理

掌握这些基础查找方法，你将能够在大多数网页自动化场景中准确定位到需要操作的元素。下一章我们将学习如何对找到的元素进行各种操作。 