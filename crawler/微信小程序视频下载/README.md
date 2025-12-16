# 微信小程序视频下载器

一个用于下载微信小程序视频的工具，支持多线程和异步协程两种下载模式。

## 功能特性

- 🚀 支持多线程下载
- ⚡ 支持异步协程下载
- 📱 微信小程序视频解析
- 🔒 支持AES加密视频解密
- 📁 自动合并TS文件
- 📋 批量下载支持
- 🎯 支持命令行参数配置
- 📊 详细的日志记录

## 环境要求

- Python >= 3.7
- 依赖库：见requirements.txt

## 安装方法

1. 克隆或下载项目代码
2. 安装依赖库

```bash
pip install -r requirements.txt
```

## 使用说明

### 基本用法

```bash
# 使用多线程模式下载（默认）
python main.py

# 使用异步协程模式下载
python main.py --mode async
```

### 命令行参数

| 参数 | 缩写 | 说明 | 默认值 |
|------|------|------|--------|
| --mode | -m | 下载模式：sync（多线程）或 async（异步协程） | sync |
| --max-workers | | 最大线程数（仅sync模式有效） | 10 |
| --max-concurrency | | 最大并发数（仅async模式有效） | 10 |
| --log-level | | 日志级别：DEBUG, INFO, WARNING, ERROR, CRITICAL | INFO |
| --help | -h | 显示帮助信息 | |

### 示例

```bash
# 使用异步协程模式，最大并发数20
python main.py --mode async --max-concurrency 20

# 使用多线程模式，最大线程数15，日志级别DEBUG
python main.py --max-workers 15 --log-level DEBUG
```

## 项目结构

```
微信小程序视频下载器/
├── config.py          # 配置文件
├── utils.py           # 工具函数
├── gen_id.py          # 获取资源ID
├── id_to_m3u8.py      # ID转换为M3U8链接
├── download_m3u8.py   # 多线程下载器
├── async_downloader.py # 异步协程下载器
├── main.py           # 主程序入口
├── requirements.txt   # 依赖库列表
└── README.md         # 项目说明文档
```

## 配置说明

配置文件 `config.py` 包含了所有可配置的参数，包括：

- 下载路径
- 线程数/并发数
- 请求超时设置
- API URL
- 请求头和Cookie

可以通过修改配置文件或使用环境变量来调整配置。

## 注意事项

1. 请确保遵守相关网站的使用条款和版权规定
2. 下载视频可能涉及版权问题，请谨慎使用
3. 建议合理设置线程数和并发数，避免对服务器造成过大压力
4. 部分视频可能需要登录才能访问，请确保Cookie有效

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！
