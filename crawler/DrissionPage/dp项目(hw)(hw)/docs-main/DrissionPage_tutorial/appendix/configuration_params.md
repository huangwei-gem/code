# DrissionPage 配置文件参数表

DrissionPage 的配置文件控制着工具的行为，包括浏览器设置、会话设置、超时时间等。本文档详细介绍了配置文件中的各项参数。

## 配置文件位置

默认情况下，配置文件保存在用户主目录的 `.DrissionPage` 文件夹下：

- Windows: `C:\Users\用户名\.DrissionPage\configs.ini`
- Linux: `/home/用户名/.DrissionPage/configs.ini`
- macOS: `/Users/用户名/.DrissionPage/configs.ini`

## 配置文件结构

配置文件采用 INI 格式，分为多个部分：

## [paths]

路径相关配置，指定浏览器、驱动和下载路径等。

| 参数 | 描述 | 默认值 | 示例 |
|-----|------|-------|------|
| `browser_path` | 浏览器可执行文件路径 | 自动查找 | `C:\Program Files\Google\Chrome\Application\chrome.exe` |
| `local_port` | 本地调试端口 | `9222` | `9222` |
| `download_path` | 下载文件保存路径 | 用户下载文件夹 | `D:\downloads` |
| `user_data_path` | 用户数据文件夹路径 | 临时文件夹 | `D:\chrome_data` |
| `cache_path` | 缓存文件夹路径 | 临时文件夹 | `D:\chrome_cache` |

## [chromium_options]

Chromium 浏览器相关选项。

| 参数 | 描述 | 默认值 | 示例 |
|-----|------|-------|------|
| `arguments` | 启动参数，多个参数用逗号分隔 | 内置默认参数 | `--start-maximized,--disable-gpu` |
| `extensions` | 扩展路径，多个路径用逗号分隔 | 无 | `D:\extensions\1.crx,D:\extensions\2.crx` |
| `prefs` | 预设参数，JSON格式 | `{}` | `{"download.default_directory": "D:\\downloads"}` |
| `experimental_options` | 实验性选项，JSON格式 | `{}` | `{"excludeSwitches": ["enable-automation"]}` |
| `capability` | 附加功能，JSON格式 | `{}` | `{"acceptInsecureCerts": true}` |
| `debugger_address` | 远程调试地址 | 无 | `127.0.0.1:9222` |
| `binary_location` | 浏览器可执行文件路径(同 browser_path) | 自动查找 | `C:\Program Files\Google\Chrome\Application\chrome.exe` |

## [session_options]

SessionPage 相关选项。

| 参数 | 描述 | 默认值 | 示例 |
|-----|------|-------|------|
| `headers` | 请求头，JSON格式 | 模拟 Chrome 请求头 | `{"User-Agent": "Custom Agent"}` |
| `cookies` | Cookies，JSON格式 | `{}` | `{"session": "abc123"}` |
| `auth` | HTTP认证信息，(username,password) 格式 | 无 | `admin,password` |
| `proxies` | 代理设置，JSON格式 | 无 | `{"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}` |
| `verify` | SSL验证，true/false 或 CA证书路径 | `true` | `false` |
| `cert` | 客户端证书，(cert_path,key_path) 格式 | 无 | `cert.pem,key.pem` |
| `stream` | 是否使用流式传输，true/false | `false` | `true` |
| `trust_env` | 是否信任环境变量，true/false | `true` | `false` |
| `max_redirects` | 最大重定向次数 | `30` | `10` |

## [timeouts]

超时设置。

| 参数 | 描述 | 默认值 | 示例 |
|-----|------|-------|------|
| `base` | 基本超时时间(秒) | `10` | `5` |
| `page_load` | 页面加载超时时间(秒) | `30` | `20` |
| `script` | 脚本执行超时时间(秒) | `30` | `10` |
| `implicit` | 隐式等待时间(秒) | `0` | `2` |
| `needle_in_session` | Session模式元素查找超时时间(秒) | `10` | `5` |
| `needle_in_chromium` | Chromium模式元素查找超时时间(秒) | `10` | `5` |
| `retry_times` | 查找元素重试次数 | `3` | `5` |
| `retry_interval` | 查找元素重试间隔(秒) | `0.5` | `1` |

## [flags]

功能开关。

| 参数 | 描述 | 默认值 | 示例 |
|-----|------|-------|------|
| `incognito` | 是否使用无痕模式，true/false | `false` | `true` |
| `headless` | 是否使用无头模式，true/false | `false` | `true` |
| `auto_port` | 是否自动分配端口，true/false | `true` | `false` |
| `load_mode` | 页面加载模式，normal/eager/none | `normal` | `eager` |
| `show_log` | 是否显示日志，true/false | `true` | `false` |
| `download_with_chromium` | 是否使用Chromium下载，true/false | `true` | `false` |
| `auto_handle_alerts` | 是否自动处理弹窗，true/false/accept/dismiss | `false` | `accept` |
| `check_page_state` | 是否检查页面状态，true/false | `true` | `false` |
| `block_images` | 是否阻止图片加载，true/false | `false` | `true` |
| `abort_timeout` | 是否在超时后中止，true/false | `true` | `false` |
| `enable_stealth_js` | 是否启用隐身JS，true/false | `false` | `true` |
| `auto_set_options` | 自动设置实验性选项，true/false | `true` | `false` |

## 配置文件示例

以下是一个完整的配置文件示例：

```ini
[paths]
browser_path = C:\Program Files\Google\Chrome\Application\chrome.exe
local_port = 9222
download_path = D:\downloads
user_data_path = D:\chrome_data
cache_path = D:\chrome_cache

[chromium_options]
arguments = --start-maximized,--disable-gpu
extensions = 
prefs = {"download.default_directory": "D:\\downloads"}
experimental_options = {"excludeSwitches": ["enable-automation"]}
capability = {"acceptInsecureCerts": true}
debugger_address = 
binary_location = 

[session_options]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
cookies = {}
auth = 
proxies = {}
verify = true
cert = 
stream = false
trust_env = true
max_redirects = 30

[timeouts]
base = 10
page_load = 30
script = 30
implicit = 0
needle_in_session = 10
needle_in_chromium = 10
retry_times = 3
retry_interval = 0.5

[flags]
incognito = false
headless = false
auto_port = true
load_mode = normal
show_log = true
download_with_chromium = true
auto_handle_alerts = false
check_page_state = true
block_images = false
abort_timeout = true
enable_stealth_js = false
auto_set_options = true
```

## 使用代码修改配置

除了直接编辑配置文件，您还可以使用代码动态修改配置：

```python
from DrissionPage import ChromiumOptions

# 创建配置对象
co = ChromiumOptions()

# 修改路径
co.set_browser_path(r'C:\Chrome\chrome.exe')
co.set_download_path(r'D:\downloads')

# 修改浏览器选项
co.set_argument('--start-maximized')
co.set_headless(True)
co.set_no_imgs(True)

# 修改超时设置
co.set_timeouts(page_load=20, script=10)

# 保存配置
co.save('my_config.ini')

# 使用配置创建页面对象
from DrissionPage import ChromiumPage
page = ChromiumPage(co)
```

## 配置文件优先级

DrissionPage 按以下优先级使用配置：

1. 代码中直接传入的配置对象
2. 通过路径指定的配置文件
3. 默认配置文件
4. 内置默认配置

例如，创建页面对象时可以指定配置文件：

```python
from DrissionPage import ChromiumPage

# 使用自定义配置文件
page = ChromiumPage(config_path='my_config.ini')
```

或者可以同时使用配置对象和配置文件：

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 加载配置文件到配置对象
co = ChromiumOptions('my_config.ini')
# 修改部分设置
co.set_headless(True)
# 使用修改后的配置
page = ChromiumPage(co)
``` 