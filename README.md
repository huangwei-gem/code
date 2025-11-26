# Python爬虫项目集合

这个项目仓库收集了我的各种Python爬虫项目和逆向工程案例。

## 项目结构

```
c:\code\
├── Python_study\                    # Python学习资料
├── crawler\                        # 主要爬虫项目目录
│   ├── crawl4AI\                   # AI驱动的爬虫框架
│   │   └── crawl4ai-main\          # Crawl4AI主项目
│   ├── 7811游戏交易网爬虫\          # 7881.com网站爬虫
│   ├── 优志愿-webpack逆向\         # webpack逆向分析
│   ├── DrissionPage\               # DrissionPage爬虫项目
│   └── 常用的Python代码\            # 工具代码集合
└── test\                           # 测试和示例代码
    ├── crawl4ai_example.py         # Crawl4AI使用示例
    ├── example_result.md           # 示例结果
    └── python_org_result.md        # Python官网爬取结果
```

## 主要项目

### 1. Crawl4AI项目
- **位置**: `crawler/crawl4AI/crawl4ai-main/`
- **描述**: 先进的AI驱动爬虫框架
- **功能**: 支持异步爬取、Markdown生成、内容过滤、代理支持等
- **状态**: ✅ 已安装并测试成功

### 2. 7881游戏交易网爬虫
- **位置**: `crawler/7811游戏交易网-发送数据为json-简单请求头加密/`
- **描述**: 针对7881.com游戏交易网站的爬虫
- **特色**: 处理JSON数据格式和请求头加密
- **技术**: Python + requests + execjs + crypto-js

### 3. 优志愿-webpack逆向
- **位置**: `crawler/优志愿-webpack逆向/`
- **描述**: webpack打包逆向分析项目
- **技术**: JavaScript逆向工程

### 4. DrissionPage项目
- **位置**: `crawler/DrissionPage/`
- **描述**: 基于DrissionPage的爬虫项目
- **状态**: 项目文件已打包

## 快速开始

### 环境要求
- Python 3.8+
- Node.js（部分项目需要）
- Git

### 1. 克隆仓库
```bash
git clone <你的仓库地址>
cd python-crawler-projects
```

### 2. 设置虚拟环境
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. 安装依赖
根据具体项目安装相应的依赖包。

### 4. 运行Crawl4AI示例
```bash
cd test
python crawl4ai_example.py
```

## 技术栈

- **Python 3.8+**: 主要开发语言
- **requests**: HTTP请求库
- **execjs**: JavaScript执行引擎
- **crawl4ai**: AI爬虫框架
- **DrissionPage**: 浏览器自动化工具
- **crypto-js**: JavaScript加密库
- **playwright**: 现代浏览器自动化

## 项目特色

### 🚀 高性能爬取
- 异步爬取支持
- 并发请求处理
- 智能重试机制

### 🤖 AI驱动
- 智能内容提取
- 自适应爬取策略
- LLM辅助解析

### 🛡️ 反爬虫对抗
- 请求头加密处理
- JavaScript逆向分析
- 浏览器指纹模拟

### 📊 数据处理能力
- JSON/XML解析
- Markdown生成
- 数据清洗和过滤

## 注意事项

1. **遵守robots.txt**: 爬取网站前请检查robots.txt文件
2. **合理设置延迟**: 避免对目标网站造成过大压力
3. **法律合规**: 确保爬取行为符合相关法律法规
4. **隐私保护**: 不要收集和存储敏感个人信息
5. **版权尊重**: 尊重原创内容版权

## 更新计划

- [ ] 添加更多爬虫示例
- [ ] 完善文档和教程
- [ ] 添加配置文件管理
- [ ] 实现分布式爬取支持
- [ ] 添加数据存储方案

## 贡献

欢迎提交Issue和Pull Request来改进项目。

## 许可证

本项目采用MIT许可证 - 详见LICENSE文件。

---

**⚠️ 免责声明**: 本项目仅供学习和研究使用，请确保你的爬取行为符合相关法律法规和网站服务条款。