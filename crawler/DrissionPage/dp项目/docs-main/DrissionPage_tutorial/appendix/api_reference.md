# DrissionPage API 参考

本文档提供了 DrissionPage 核心 API 的详细参考。以下列出了最常用的 API，按对象类型分类。

## 页面对象 API

### 通用页面方法

| 方法/属性 | 描述 | 适用对象 |
|---------|------|---------|
| `get(url)` | 访问指定网址 | 所有页面 |
| `title` | 获取页面标题 | 所有页面 |
| `html` | 获取页面源码 | 所有页面 |
| `url` | 获取当前 URL | 所有页面 |
| `cookies` | 获取/设置 cookies | 所有页面 |
| `ele(locator)` | 查找单个元素 | 所有页面 |
| `eles(locator)` | 查找多个元素 | 所有页面 |
| `s(locator)` | ele() 的快捷方式 | 所有页面 |
| `ss(locator)` | eles() 的快捷方式 | 所有页面 |
| `get_cookies()` | 获取当前页面所有 cookies | 所有页面 |
| `set_cookies(cookies)` | 设置 cookies | 所有页面 |
| `save()` | 保存页面截图或源码 | 所有页面 |

### SessionPage 特有方法

| 方法/属性 | 描述 |
|---------|------|
| `post(url, data)` | 发送 POST 请求 |
| `download(url, target_path)` | 下载文件 |
| `set_headers(headers)` | 设置请求头 |
| `set_proxy(proxy)` | 设置代理 |
| `set_timeout(timeout)` | 设置超时时间 |

### ChromiumPage 特有方法

| 方法/属性 | 描述 |
|---------|------|
| `new_tab(url=None)` | 新建标签页 |
| `tabs` | 获取所有标签页 |
| `tab` | 当前标签页对象 |
| `to_tab(tab_id)` | 切换到指定标签页 |
| `close_tabs(tabs)` | 关闭指定标签页 |
| `run_js(script)` | 执行 JavaScript |
| `get_frame(locator)` | 获取 iframe 对象 |
| `wait.load_complete()` | 等待页面加载完成 |
| `wait.ele_display(locator)` | 等待元素显示 |
| `wait.ele_loaded(locator)` | 等待元素加载完成 |

## 元素对象 API

### 通用元素方法

| 方法/属性 | 描述 | 适用对象 |
|---------|------|---------|
| `click()` | 点击元素 | 所有元素 |
| `text` | 获取元素文本 | 所有元素 |
| `html` | 获取元素 HTML | 所有元素 |
| `attr(name)` | 获取元素属性 | 所有元素 |
| `xpath` | 获取元素 XPath | 所有元素 |
| `parent()` | 获取父元素 | 所有元素 |
| `next()` | 获取下一个兄弟元素 | 所有元素 |
| `prev()` | 获取上一个兄弟元素 | 所有元素 |
| `ele(locator)` | 在元素内查找单个元素 | 所有元素 |
| `eles(locator)` | 在元素内查找多个元素 | 所有元素 |
| `s(locator)` | ele() 的快捷方式 | 所有元素 |
| `ss(locator)` | eles() 的快捷方式 | 所有元素 |

### ChromiumElement 特有方法

| 方法/属性 | 描述 |
|---------|------|
| `input(text)` | 输入文本 |
| `prop(name)` | 获取元素属性(JavaScript 属性) |
| `style(name)` | 获取元素样式 |
| `screenshot(path)` | 截图元素 |
| `hover()` | 鼠标悬停 |
| `drag_to(target)` | 拖拽到目标元素 |
| `upload(file_path)` | 上传文件(用于文件输入框) |
| `run_js(script)` | 对元素执行 JavaScript |
| `is_displayed()` | 元素是否可见 |
| `is_enabled()` | 元素是否可用 |
| `is_selected()` | 元素是否选中(复选框等) |

## DownloadKit API

| 方法/属性 | 描述 |
|---------|------|
| `download(url, path)` | 下载文件 |
| `set_headers(headers)` | 设置请求头 |
| `set_proxy(proxy)` | 设置代理 |
| `set_timeout(timeout)` | 设置超时时间 |
| `add_task(url, path)` | 添加下载任务 |
| `add_tasks(tasks)` | 批量添加下载任务 |
| `start()` | 开始下载任务 |
| `wait()` | 等待所有任务完成 |

## 配置对象 API

| 方法/属性 | 描述 |
|---------|------|
| `read()` | 读取配置 |
| `save()` | 保存配置 |
| `set_paths(paths)` | 设置路径 |
| `set_browser_options(options)` | 设置浏览器选项 |
| `get_option(key)` | 获取配置选项 |
| `set_option(key, value)` | 设置配置选项 |

---

更多 API 详情，请参考[官方文档](https://g1879.gitee.io/drissionpagedocs/)。 