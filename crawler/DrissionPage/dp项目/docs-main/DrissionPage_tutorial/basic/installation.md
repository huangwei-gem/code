# 环境配置

本章将指导您完成 DrissionPage 的环境配置，包括安装 Python、安装 DrissionPage 以及配置浏览器。

## 安装 Python

DrissionPage 是基于 Python 的自动化工具，因此首先需要安装 Python 环境。

### Python 版本要求

DrissionPage 支持 Python 3.6 及以上版本。推荐使用 Python 3.8 或更高版本以获得更好的性能和兼容性。

### Windows 系统安装 Python

1. 访问 [Python 官网](https://www.python.org/downloads/) 下载最新版本的 Python 安装包
2. 运行安装包，勾选 "**Add Python to PATH**"（将 Python 添加到环境变量）
3. 点击 "Install Now"（现在安装）进行标准安装
4. 安装完成后，打开命令提示符（CMD），输入以下命令验证安装：
   ```bash
   python --version
   ```
   如果显示 Python 版本号，则安装成功

### macOS 系统安装 Python

1. 使用 Homebrew 安装（推荐）：
   ```bash
   brew install python
   ```
   
2. 或者从 [Python 官网](https://www.python.org/downloads/) 下载 macOS 安装包安装

3. 安装完成后，在终端中验证：
   ```bash
   python3 --version
   ```

### Linux 系统安装 Python

大多数 Linux 发行版已预装 Python，可以在终端中验证：

```bash
python3 --version
```

如果需要安装或升级：

- Ubuntu/Debian：
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

- CentOS/RHEL：
  ```bash
  sudo yum install python3 python3-pip
  ```

## 安装 DrissionPage

安装 Python 后，您可以通过 pip 工具安装 DrissionPage。

### 使用 pip 安装

打开命令提示符或终端，输入以下命令：

```bash
pip install DrissionPage
```

### 升级到最新版本

如果您已经安装了 DrissionPage，可以使用以下命令升级到最新版本：

```bash
pip install -U DrissionPage
```

### 验证安装

安装完成后，您可以通过导入 DrissionPage 来验证安装是否成功：

```python
# 创建一个测试文件 test_installation.py
from DrissionPage import ChromiumPage

# 如果没有报错，则安装成功
print("DrissionPage 安装成功！")
```

运行此测试文件：

```bash
python test_installation.py
```

## 配置浏览器

DrissionPage 支持 Chromium 内核的浏览器，如 Google Chrome 和 Microsoft Edge。以下是配置步骤：

### 安装浏览器

如果您还没有安装浏览器，请先下载并安装：

- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/edge)

### 初始化配置

DrissionPage 首次使用时会自动生成配置文件。您可以通过以下方式手动初始化配置：

```python
from DrissionPage import ChromiumOptions

# 创建配置对象并保存为默认配置
ChromiumOptions().save()
```

执行上述代码后，在用户目录下会生成 `.DrissionPage` 文件夹，其中包含配置文件 `chrome_options.json`。

### 指定浏览器路径

如果您的浏览器不在默认路径，或者您想使用特定版本的浏览器，可以手动指定浏览器路径：

```python
from DrissionPage import ChromiumOptions

# 创建配置对象
co = ChromiumOptions()

# 设置浏览器路径
co.set_browser_path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')  # Windows 路径示例
# 或
# co.set_browser_path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')  # macOS 路径示例

# 保存配置
co.save()
```

### 常用配置设置

以下是一些常用的浏览器配置选项：

```python
from DrissionPage import ChromiumOptions

co = ChromiumOptions()

# 设置下载路径
co.set_download_path(r'D:\Downloads')

# 设置用户数据目录（保存浏览器配置、历史记录等）
co.set_user_data_path(r'D:\ChromeUserData')

# 设置浏览器窗口大小
co.set_window_size(1920, 1080)

# 无头模式（不显示浏览器界面）
co.set_headless(True)

# 设置代理服务器
co.set_proxy('http://127.0.0.1:7890')

# 保存配置
co.save()
```

## 常见问题排查

### 1. 找不到浏览器

错误信息：`NoBrowserError: Chrome.exe not found.`

解决方案：
- 确保已正确安装 Chrome 或 Edge 浏览器
- 使用 `set_browser_path()` 方法手动指定浏览器路径

### 2. WebSocket 连接失败

错误信息：`WebSocketConnectionError`

解决方案：
- 检查浏览器是否已启动
- 尝试关闭所有浏览器进程后重新运行程序
- 确保没有防火墙或安全软件阻止连接

### 3. 权限问题

错误信息：`PermissionError`

解决方案：
- Windows：以管理员身份运行 Python
- Linux/macOS：检查用户权限，必要时使用 `sudo`

## 系统要求

DrissionPage 支持在以下操作系统上运行：

- Windows 7 及以上版本
- macOS 10.13 及以上版本
- 主流 Linux 发行版（Ubuntu、Debian、CentOS 等）

硬件推荐配置：
- 处理器：双核 2GHz 或更高
- 内存：4GB 或更多
- 存储空间：至少 1GB 可用空间

## 下一步

完成环境配置后，您可以继续阅读 [快速入门](./quick_start.md) 章节，开始使用 DrissionPage 进行网页自动化操作。 