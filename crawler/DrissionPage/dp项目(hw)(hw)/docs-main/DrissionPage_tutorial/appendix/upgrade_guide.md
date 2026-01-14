# DrissionPage 升级指南

本文档提供了从旧版本升级到新版本 DrissionPage 的指南，包括重要的更改、废弃的功能和新增的功能。

## 升级到 v4.0.x

DrissionPage v4.0 是一个重大更新版本，引入了许多新功能，同时也有一些不兼容的更改。请按照以下指南升级您的代码。

### 重大变更

1. **类名和包名变更**
   
   v4.0 重命名了一些核心类以使其更符合功能定位：

   | 旧类名 | 新类名 |
   |-------|-------|
   | `ChromiumDriver` | `ChromiumPage` |
   | `SessionDriver` | `SessionPage` |
   | `Driver` | `WebPage` |

   升级代码示例：
   ```python
   # 旧版本
   from DrissionPage import ChromiumDriver, SessionDriver, Driver
   
   # 新版本
   from DrissionPage import ChromiumPage, SessionPage, WebPage
   ```

2. **配置类变更**

   配置类也进行了重命名：

   | 旧类名 | 新类名 |
   |-------|-------|
   | `ChromiumOptions` | 保持不变 |
   | `SessionOptions` | 保持不变 |
   | `DriverOptions` | `WebPageOptions` |

   升级代码示例：
   ```python
   # 旧版本
   from DrissionPage import DriverOptions
   
   # 新版本
   from DrissionPage import WebPageOptions
   ```

3. **元素操作方法变更**

   某些元素操作方法发生了变化：

   | 旧方法 | 新方法 |
   |-------|-------|
   | `ele.click()` | 保持不变 |
   | `ele.input()` | 保持不变 |
   | `ele.attr()` | 保持不变 |
   | `ele.move_to()` | `ele.hover()` |
   | `ele.click_at()` | `ele.click(x, y)` |
   | `ele.get_src()` | `ele.attr('src')` |
   | `ele.get_value()` | `ele.attr('value')` |

4. **查找方法统一**

   元素查找方法进行了统一和简化：

   | 旧方法 | 新方法 |
   |-------|-------|
   | `page.get_element()` | `page.ele()` |
   | `page.get_elements()` | `page.eles()` |
   | `page.get_element_by_id()` | `page.ele('#id')` |
   | `page.get_element_by_class_name()` | `page.ele('.class')` |
   | `page.get_element_by_name()` | `page.ele('@name=value')` |
   | `page.get_element_by_xpath()` | `page.ele('xpath://xpath')` |
   | `page.get_element_by_tag()` | `page.ele('tag:div')` |
   | `page.get_element_by_text()` | `page.ele('text=文本')` |

5. **等待机制变更**

   等待相关方法被整合到 `wait` 属性下：

   | 旧方法 | 新方法 |
   |-------|-------|
   | `page.wait_element()` | `page.wait.ele_display()` |
   | `page.wait_element_loaded()` | `page.wait.ele_loaded()` |
   | `page.wait_doc_loaded()` | `page.wait.doc_loaded()` |
   | `page.wait_ele_deleted()` | `page.wait.ele_deleted()` |

6. **页面相关方法变更**

   一些页面操作方法发生了变化：

   | 旧方法 | 新方法 |
   |-------|-------|
   | `page.get()` | 保持不变 |
   | `page.post()` | 保持不变 |
   | `page.goto()` | `page.get()` |
   | `page.driver` | 移除，直接使用页面对象 |
   | `page.cookies` | 保持不变 |
   | `page.title` | 保持不变 |
   | `page.url` | 保持不变 |

### 新功能和改进

1. **快捷元素选择器**
   
   v4.0 引入了简化的选择器 `s()` 和 `ss()` 方法，它们是 `ele()` 和 `eles()` 的别名：
   
   ```python
   # 使用新的快捷方法
   button = page.s('#submit-button')  # 等同于 page.ele('#submit-button')
   links = page.ss('tag:a')  # 等同于 page.eles('tag:a')
   ```

2. **增强的滚动操作**

   滚动相关方法被整合到 `scroll` 属性下：
   
   ```python
   # 使用新的滚动方法
   page.scroll.up(300)  # 向上滚动300像素
   page.scroll.down(500)  # 向下滚动500像素
   page.scroll.to_top()  # 滚动到顶部
   page.scroll.to_bottom()  # 滚动到底部
   element.scroll.to_see()  # 滚动直到元素可见
   ```

3. **iframe 支持改进**

   改进了对 iframe 的支持：
   
   ```python
   # 使用新的 iframe 处理方法
   frame = page.get_frame('#myFrame')
   element = frame.ele('.content')
   ```

4. **Shadow DOM 支持**

   添加了对 Shadow DOM 的支持：
   
   ```python
   # 处理 Shadow DOM
   shadow_host = page.ele('#shadow-host')
   shadow_root = shadow_host.shadow_root
   shadow_element = shadow_root.ele('.inside-shadow')
   ```

5. **强大的下载功能**

   整合了 DownloadKit，提供更强大的下载功能：
   
   ```python
   # 使用下载功能
   from DrissionPage.download import DownloadKit
   
   dk = DownloadKit()
   dk.download('https://example.com/file.zip', './downloads/')
   ```

### 废弃的功能

以下功能在 v4.0 中已被废弃：

1. `Tab` 类：使用 `ChromiumTab` 代替
2. `RawDriver`：不再支持直接使用 Selenium WebDriver
3. `d_set_proxy()`：使用 `set_proxy()` 方法代替
4. `set_headless()`：移至 `ChromiumOptions` 类

### 完整迁移示例

下面是一个从 v3.x 迁移到 v4.0 的完整示例：

**旧版本代码**：

```python
from DrissionPage import ChromiumDriver, SessionDriver, Driver, DriverOptions

# 创建配置
do = DriverOptions()
do.set_headless(True)

# 创建浏览器对象
driver = Driver(driver_or_options=do)

# 打开网页
driver.get('https://example.com')

# 查找元素
button = driver.get_element_by_id('login')
button.click()

# 等待元素
driver.wait_element('xpath://div[@class="result"]')

# 获取结果
result = driver.get_element('xpath://div[@class="result"]').text

# 切换到另一个页面
new_tab = driver.new_tab('https://example.org')
new_tab.wait_doc_loaded()
```

**新版本代码**：

```python
from DrissionPage import WebPage, WebPageOptions

# 创建配置
wpo = WebPageOptions()
wpo.chromium_options.set_headless(True)

# 创建页面对象
page = WebPage(options=wpo)

# 打开网页
page.get('https://example.com')

# 查找元素
button = page.ele('#login')
button.click()

# 等待元素
page.wait.ele_display('xpath://div[@class="result"]')

# 获取结果
result = page.ele('xpath://div[@class="result"]').text

# 切换到另一个页面
page.get('https://example.org')
page.wait.doc_loaded()
```

## 升级到 v3.0.x

如果您正在从 v2.x 升级到 v3.x，以下是主要的变更：

1. `Chrome` 类更名为 `ChromiumDriver`
2. `Session` 类更名为 `SessionDriver`
3. 添加了 `Driver` 类，可以在浏览器和会话模式之间切换
4. 查找元素方法标准化
5. 添加了更多的等待方法

请参考 v3.x 的文档进行详细的迁移。

## 升级到 v2.0.x

如果您正在从 v1.x 升级到 v2.x，以下是主要的变更：

1. 添加了 Tab 类，支持多标签页操作
2. 改进了元素定位策略
3. 添加了更多的浏览器操作功能

请参考 v2.x 的文档进行详细的迁移。

## 常见问题

### 升级后找不到某些方法

如果升级后找不到某些方法，请检查以下几点：

1. 确认类名是否已更改（例如 `ChromiumDriver` → `ChromiumPage`）
2. 确认方法是否已移动到其他属性下（例如 `wait_element()` → `wait.ele_display()`）
3. 确认方法是否已更名（例如 `move_to()` → `hover()`）

### 升级后元素查找不工作

如果升级后元素查找不正常工作，可能是由于选择器语法或查找方法的变化。请确认您使用的选择器语法是否符合新版本的规范。

### 配置文件兼容性

新版本的配置文件格式可能与旧版本不完全兼容。建议在升级后重新生成配置文件，而不是使用旧版本的配置文件。

### 第三方库集成

如果您的代码集成了第三方库或框架，请注意这些集成可能需要更新以适应 DrissionPage 的新版本。

---

如果您在升级过程中遇到任何未在本指南中提及的问题，请查看 [GitHub Issues](https://github.com/g1879/DrissionPage/issues) 或加入 QQ 交流群获取帮助。 