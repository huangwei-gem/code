# 基础概念

本章将介绍 DrissionPage 的基础概念，帮助您理解该工具的设计架构和工作原理。掌握这些核心概念对于高效使用 DrissionPage 至关重要。

## 三种页面对象介绍

DrissionPage 提供了三种核心页面对象，每种对象都有其特定用途和优势。

### 1. SessionPage（数据包模式）

**SessionPage** 是一个专注于发送和接收数据包的页面对象，基于 Python 的 requests 库进行了增强。

特点：
- 高效发送 HTTP 请求
- 处理 Cookie 和会话
- 解析和提取页面内容
- 不显示浏览器界面，仅处理网络数据

适用场景：
- 简单的数据采集
- API 调用和测试
- 不需要执行 JavaScript 的网页访问
- 对性能和资源消耗有较高要求的场景

示例：
```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://httpbin.org/get')
print(page.status_code)  # 显示状态码
print(page.html)  # 显示页面源码
```

### 2. ChromiumPage（浏览器模式）

**ChromiumPage** 是一个控制浏览器的页面对象，可以模拟用户在浏览器中的各种操作。

特点：
- 控制真实浏览器
- 执行 JavaScript
- 处理动态渲染的内容
- 支持用户交互操作（点击、输入等）
- 可截图和录屏
- 管理多个标签页

适用场景：
- 需要执行 JavaScript 的网页自动化
- 交互式网页测试
- 模拟用户行为
- 爬取动态加载内容的网站

示例：
```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.ele('#kw').input('DrissionPage')
page.ele('#su').click()
```

### 3. WebPage（混合模式）

**WebPage** 是 DrissionPage 最强大的页面对象，它集成了 SessionPage 和 ChromiumPage 的功能，并提供了两种模式之间的切换能力。

特点：
- 同时具备 SessionPage 和 ChromiumPage 的所有功能
- 可在数据包模式（s 模式）和浏览器模式（d 模式）之间无缝切换
- 可共享 Cookie 和会话数据
- 提供更灵活的操作选择

适用场景：
- 需要同时使用两种模式的复杂自动化任务
- 需要高效处理部分内容，同时又需要浏览器处理其他内容的场景
- 同一网站的不同页面需要不同处理方式

示例：
```python
from DrissionPage import WebPage

page = WebPage()
# 默认使用 d 模式（浏览器模式）
page.get('https://www.baidu.com')
page.ele('#kw').input('DrissionPage')
page.ele('#su').click()

# 切换到 s 模式（数据包模式）
page.change_mode('s')
page.get('https://httpbin.org/get')
print(page.status_code)
```

## 页面和元素的关系

在 DrissionPage 中，页面对象和元素对象之间有着密切的关系，理解这种关系有助于更高效地编写自动化脚本。

### 元素类型

DrissionPage 中的元素类型与页面对象类型对应：

1. **SessionElement**：从 SessionPage 中获取的元素对象
2. **ChromiumElement**：从 ChromiumPage 中获取的元素对象
3. **ChromiumFrame**：特殊的 ChromiumElement，表示 iframe 或 frame 元素，同时具有页面特性
4. **ChromiumShadowElement**：表示 Shadow DOM 的根元素，可用于获取 Shadow DOM 中的元素

### 元素获取方式

从页面对象获取元素的主要方法：

1. **单个元素获取**：使用 `ele()` 方法
   ```python
   # 获取单个元素
   element = page.ele('#id')
   ```

2. **多个元素获取**：使用 `eles()` 方法
   ```python
   # 获取多个元素
   elements = page.eles('.class')
   ```

3. **元素链式查找**：从已获取的元素中继续查找子元素
   ```python
   # 链式查找
   child_element = page.ele('#container').ele('.item')
   ```

### 元素与页面的关系模型

```
页面对象 (Page)
    │
    ├── 元素1 (Element)
    │      │
    │      ├── 子元素1 (Element)
    │      │
    │      └── 子元素2 (Element)
    │
    ├── 元素2 (Element)
    │      │
    │      └── 子元素 (Element)
    │
    └── iframe元素 (ChromiumFrame)
           │
           ├── iframe内元素1 (Element)
           │
           └── iframe内元素2 (Element)
```

### 重要概念

1. **元素层级关系**：元素之间存在父子、兄弟关系，可以通过相对定位查找元素
   ```python
   # 获取父元素
   parent = element.parent
   
   # 获取兄弟元素
   next_sibling = element.next
   prev_sibling = element.prev
   ```

2. **元素集合**：使用 `eles()` 获取的是元素集合，可以像列表一样操作
   ```python
   elements = page.eles('li')
   for element in elements:
       print(element.text)
       
   # 使用索引访问
   first_element = elements[0]
   # 获取数量
   count = len(elements)
   ```

3. **元素检查**：获取元素后应检查元素是否存在
   ```python
   element = page.ele('#maybe-not-exist')
   if element:  # 检查元素是否存在
       element.click()
   ```

## 配置对象

DrissionPage 使用配置对象来设置页面对象的行为。配置对象在创建页面对象时使用，用于自定义各种参数。

### 1. SessionOptions（用于 SessionPage）

**SessionOptions** 用于配置 SessionPage 的行为，如请求头、代理设置等。

示例：
```python
from DrissionPage import SessionOptions, SessionPage

# 创建配置对象
so = SessionOptions()

# 设置请求头
so.set_headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

# 设置代理
so.set_proxy('http://127.0.0.1:7890')

# 使用配置创建 SessionPage
page = SessionPage(so)
```

主要配置项：
- 请求头（Headers）
- 代理（Proxy）
- 超时设置（Timeout）
- Cookie 设置

### 2. ChromiumOptions（用于 ChromiumPage）

**ChromiumOptions** 用于配置 ChromiumPage 的行为，如浏览器路径、窗口大小、无头模式等。

示例：
```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 创建配置对象
co = ChromiumOptions()

# 设置浏览器窗口大小
co.set_window_size(1920, 1080)

# 启用无头模式（不显示浏览器界面）
co.set_headless(True)

# 指定浏览器路径
co.set_browser_path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

# 使用配置创建 ChromiumPage
page = ChromiumPage(co)
```

主要配置项：
- 浏览器路径
- 用户数据目录
- 窗口大小
- 无头模式设置
- 代理设置
- 下载路径
- 浏览器启动参数

### 3. 配置文件使用

DrissionPage 支持将配置保存为文件，方便重复使用和团队共享。

```python
from DrissionPage import ChromiumOptions

# 创建配置对象
co = ChromiumOptions()

# 进行各种设置
co.set_window_size(1920, 1080)
co.set_headless(True)

# 保存配置到默认位置（用户目录下的 .DrissionPage 文件夹）
co.save()

# 或保存到指定位置
co.save('my_chrome_config.json')
```

加载已保存的配置：

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 加载默认配置
co = ChromiumOptions()

# 或加载指定配置文件
co = ChromiumOptions('my_chrome_config.json')

# 可以对加载的配置进行修改
co.set_headless(False)  # 覆盖配置文件中的设置

# 使用配置创建页面对象
page = ChromiumPage(co)
```

### 对象和配置的对应关系

| 页面对象类型 | 配置对象类型 | 模式 |
|------------|------------|------|
| SessionPage | SessionOptions | 数据包模式 |
| ChromiumPage | ChromiumOptions | 浏览器模式 |
| WebPage | SessionOptions + ChromiumOptions | 混合模式（可切换） |

## 小结

理解 DrissionPage 的核心概念有助于更高效地使用该工具：

1. **三种页面对象**（SessionPage、ChromiumPage、WebPage）提供了不同的功能和适用场景
2. **页面和元素的关系**构成了 DrissionPage 的操作模型
3. **配置对象**（SessionOptions、ChromiumOptions）用于自定义页面对象的行为

根据实际需求选择合适的页面对象和配置，可以大大提高自动化脚本的效率和可靠性。

下一章，我们将学习基础的页面操作方法。查看 [基础页面操作](./page_operations.md) 继续学习。 