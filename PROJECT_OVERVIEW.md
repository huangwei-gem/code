# 项目概览

## 项目背景

这是一个Python爬虫项目集合，包含了多个不同类型的爬虫和逆向工程项目。项目涵盖了从基础的HTTP请求到高级的AI驱动爬虫框架，以及JavaScript逆向分析等多种技术。

## 技术架构

### 核心爬虫技术
- **传统爬虫**: requests + BeautifulSoup
- **浏览器自动化**: Selenium, Playwright, DrissionPage
- **AI驱动爬虫**: Crawl4AI框架
- **异步爬虫**: aiohttp, asyncio

### 反爬虫对抗
- **请求头加密**: 自定义签名算法
- **JavaScript逆向**: webpack分析，函数还原
- **浏览器指纹**: UserAgent轮换，行为模拟
- **代理池**: 多IP轮换

### 数据处理
- **HTML解析**: lxml, BeautifulSoup4
- **JSON处理**: 内置json库，pandas
- **Markdown生成**: html2text, crawl4ai内置
- **数据存储**: SQLite, MongoDB, Redis

## 项目特色

### 1. 7881游戏交易网爬虫
**技术亮点**:
- 请求头签名加密 (`lb-sign`, `lb-timestamp`)
- JSON数据格式处理
- JavaScript加密函数调用 (通过execjs)

**关键代码**:
```python
# 动态生成签名
with open('test.js', encoding='utf-8') as f:
    code = f.read()
ctll = execjs.compile(code)
obj = ctll.call("sign", json_data)
headers['lb-sign'] = obj['lb-sign']
headers['lb-timestamp'] = str(obj['lb-timestamp'])
```

### 2. Crawl4AI项目
**技术亮点**:
- AI驱动的内容提取
- 异步并发处理
- 智能缓存机制
- Markdown自动生成

**核心功能**:
- `AsyncWebCrawler`: 主要爬虫类
- `AdaptiveCrawler`: 自适应爬虫
- `LLMExtractionStrategy`: LLM提取策略
- `JsonCssExtractionStrategy`: CSS选择器提取

### 3. 优志愿-webpack逆向
**技术亮点**:
- webpack打包结构分析
- 加密函数定位与还原
- 动态调试与跟踪

## 项目结构详解

```
c:\code\
├── crawler\                           # 主要爬虫项目目录
│   ├── .venv\                       # Python虚拟环境
│   ├── crawl4AI\                    # AI爬虫框架
│   │   └── crawl4ai-main\           # Crawl4AI主项目
│   │       ├── crawl4ai\            # 核心库
│   │       ├── deploy\              # 部署相关
│   │       ├── docs\                # 文档
│   │       └── tests\               # 测试代码
│   ├── 7811游戏交易网爬虫\          # 7881.com爬虫项目
│   │   ├── main.py                  # 主程序
│   │   ├── test.js                  # JavaScript加密函数
│   │   ├── node_modules\           # Node.js依赖
│   │   └── package*.json            # 包管理文件
│   ├── 优志愿-webpack逆向\         # webpack逆向项目
│   │   ├── mian.py                  # 主程序
│   │   └── webpack.js               # webpack分析文件
│   ├── DrissionPage\                # DrissionPage项目
│   │   └── dp项目.zip               # 项目压缩包
│   ├── main.py                      # JavaScript混淆代码
│   └── 常用的Python代码\            # 工具函数集合
├── test\                            # 测试目录
│   ├── .venv\                       # 测试环境虚拟环境
│   ├── crawl4ai_example.py         # Crawl4AI使用示例
│   ├── example_result.md           # 示例结果
│   └── python_org_result.md        # Python官网爬取结果
└── Python_study\                   # Python学习资料
    └── crawler\                     # 学习用爬虫代码
```

## 使用指南

### 环境准备
1. **Python环境**: 建议使用Python 3.8+
2. **虚拟环境**: 为每个项目创建独立的虚拟环境
3. **依赖安装**: 根据项目需求安装相应的依赖包

### 项目启动步骤

#### 7881爬虫项目
```bash
cd "crawler/7811游戏交易网-发送数据为json-简单请求头加密"
# 安装Node.js依赖
npm install
# 运行Python主程序
python main.py
```

#### Crawl4AI项目
```bash
cd test
# 激活虚拟环境
.\.venv\Scripts\activate
# 运行示例
python crawl4ai_example.py
```

## 技术难点与解决方案

### 1. JavaScript加密处理
**问题**: 7881网站使用JavaScript进行请求头加密
**解决方案**: 使用execjs库在Python中执行JavaScript代码

### 2. 异步爬虫优化
**问题**: 大规模爬取时的性能问题
**解决方案**: 使用asyncio和aiohttp实现异步并发

### 3. 内容提取准确性
**问题**: 从复杂HTML中提取有用信息
**解决方案**: 使用Crawl4AI的AI驱动提取功能

### 4. 反爬虫检测
**问题**: 网站的各种反爬虫机制
**解决方案**: 
- 请求头模拟
- IP代理池
- 访问频率控制
- 浏览器行为模拟

## 扩展计划

### 短期目标
- [ ] 完善项目文档
- [ ] 添加更多爬虫示例
- [ ] 实现统一的配置管理
- [ ] 添加错误处理和日志系统

### 中期目标
- [ ] 构建分布式爬虫系统
- [ ] 实现智能调度系统
- [ ] 添加数据可视化功能
- [ ] 完善反爬虫策略库

### 长期目标
- [ ] 构建爬虫管理平台
- [ ] 实现机器学习辅助爬取
- [ ] 添加自然语言处理功能
- [ ] 构建完整的爬虫生态

## 最佳实践

### 1. 代码规范
- 遵循PEP 8编码规范
- 使用类型注解
- 添加充分的注释
- 编写单元测试

### 2. 爬虫伦理
- 遵守robots.txt协议
- 控制访问频率
- 不收集敏感信息
- 尊重版权和隐私

### 3. 性能优化
- 使用连接池
- 实现智能重试
- 合理使用缓存
- 优化内存使用

## 相关资源

- [Crawl4AI官方文档](https://github.com/unclecode/crawl4ai)
- [Python爬虫最佳实践](https://docs.python-guide.org/)
- [requests库文档](https://docs.python-requests.org/)
- [BeautifulSoup文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 联系方式

如有问题或建议，欢迎提交Issue或Pull Request。

---

**注意**: 本项目仅供学习和研究使用，请确保你的爬取行为符合相关法律法规和网站服务条款。