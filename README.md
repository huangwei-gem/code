# Python爬虫项目集合
11
这个项目仓库收集了我的各种Python爬虫项目和逆向工程案例。

## 项目结构

```
c:\code\
├── Python_study\                    # Python学习资料
├── crawler\                        # 主要爬虫项目目录
│   ├── .venv\                      # Python虚拟环境
│   │   ├── Lib\site-packages\      # 安装的依赖包
│   │   ├── Scripts\                # 可执行脚本
│   │   └── pyvenv.cfg              # 虚拟环境配置
│   ├── crawl4AI\                   # AI驱动的爬虫框架
│   │   ├── crawl4ai-main\         # Crawl4AI主项目
│   │   │   ├── crawl4ai\           # 核心库文件
│   │   │   ├── docs\               # 文档和教程
│   │   │   ├── tests\              # 测试文件
│   │   │   ├── examples_chinese\   # 中文示例
│   │   │   └── *.py                # 各种Python脚本
│   │   ├── crawl4-mcp-master\      # MCP集成项目
│   │   └── examples_chinese\       # 中文示例集合
│   │       ├── Capsolver验证码解决\ # 验证码处理示例
│   │       ├── Docker示例\         # Docker相关示例
│   │       ├── LLM示例\            # AI大模型集成
│   │       ├── 代理示例\           # 代理服务器示例
│   │       ├── 不可检测性\        # 反检测技术
│   │       └── 基础教程.md
│   ├── 7811游戏交易网-发送数据为json-简单请求头加密\ # 7881.com爬虫
│   │   ├── main.py                  # 主爬虫脚本
│   │   ├── test.js                  # JavaScript测试
│   │   ├── node_modules\           # Node.js依赖
│   │   ├── package.json             # Node.js配置
│   │   └── Readme.md                # 项目说明
│   ├── DrissionPage\               # DrissionPage项目集合
│   │   ├── dp项目\                 # 9个爬虫项目合集
│   │   │   ├── DSAnimePictures-main\ # 动漫图片爬虫
│   │   │   ├── DrissionPage-main\   # DrissionPage核心
│   │   │   ├── Drissionpage2-main\  # 抖音电影评论分析
│   │   │   ├── JDproduct-crawler-main\ # 京东商品爬虫
│   │   │   │   ├── LDA处理\         # 主题模型分析
│   │   │   │   ├── visualizations\  # 可视化图表
│   │   │   │   ├── 数据集\          # 爬取的数据
│   │   │   │   └── 词云图\          # 词云生成
│   │   │   ├── REDnote-crawler-main\ # 小红书爬虫
│   │   │   ├── SearchAllNewsPlatform-main\ # 多平台搜索
│   │   │   ├── Spider-main\         # 通用爬虫框架
│   │   │   │   ├── SimPrograms\     # 简单爬虫示例
│   │   │   │   ├── SpiderPro\       # 专业爬虫脚本
│   │   │   │   └── utils\           # 工具函数
│   │   │   ├── docs-main\           # 教程文档
│   │   │   └── music163_crawler-master\ # 网易云音乐爬虫
│   │   ├── 京东数据爬取.py          # 京东数据爬虫
│   │   ├── 小红书.py                # 小红书爬虫
│   │   ├── 拉勾网数据爬取.py        # 拉勾网职位爬虫
│   │   └── 官方示例代码\            # DrissionPage示例
│   ├── 优志愿-webpack逆向\          # webpack逆向分析
│   ├── 常用的Python代码\             # 工具代码集合
│   ├── 数据加密\                    # 加密相关代码
│   ├── 爬虫基础\                    # 基础爬虫教程
│   └── 猫眼电影实时票房-字体加密\    # 字体加密破解
└── test\                           # 测试和示例代码
    ├── crawl4ai_example.py         # Crawl4AI使用示例
    ├── example_result.md           # 示例结果
    └── python_org_result.md        # Python官网爬取结果
```

## 📊 项目统计

- **总项目数**: 15+ 个独立爬虫项目
- **总文件数**: 8,193+ 个文件（仅dp项目）
- **主要技术栈**: Python, JavaScript, DrissionPage, Crawl4AI
- **覆盖领域**: 电商、社交媒体、新闻、音乐、动漫、招聘等
- **数据处理能力**: 文本分析、可视化、机器学习（LDA）

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

### 4. DrissionPage项目集合
- **位置**: `crawler/DrissionPage/`
- **描述**: 基于DrissionPage的爬虫项目集合，包含9个完整项目
- **状态**: ✅ 已上传完整项目文件夹（8193个文件）

#### dp项目文件夹内容（9个子项目）：

1. **DSAnimePictures-main** - 动漫图片爬虫
   - `WebCrawler(AnimePictures).py` - 主爬虫脚本
   - `README.md` - 项目说明

2. **DrissionPage-main** - DrissionPage核心项目
   - `binance.py` - 币安数据爬虫
   - `test.py` - 测试脚本
   - `LICENSE`, `README.md` - 项目文档

3. **Drissionpage2-main** - 抖音电影评论分析
   - `爬取731电影评论数据.py` - 数据爬取脚本
   - `基本词云图.py` - 词云生成
   - `用户地区分布图 - 可视化.py` - 地理可视化
   - `可视化地区分布图.html` - 交互式图表
   - `731电影评论词云.png`, `视频效果.mp4` - 成果展示

4. **JDproduct-crawler-main** - 京东商品爬虫 + LDA分析
   - `crawler.py` - 主爬虫脚本
   - `LDA处理/` - 主题模型分析
     - `LDA.py`, `LDA _visualization.py` - LDA算法实现
     - `LDA分析.txt`, `stopwords.txt` - 分析结果和停用词
   - `数据集/` - 爬取的商品数据（分词、CSV、JSON格式）
   - `visualizations/` - 环保主题商品可视化图表（HTML）
   - `词云图/` - 词云生成相关文件

5. **REDnote-crawler-main** - 小红书爬虫
   - `utils.py`, `data_writer.py` - 工具函数
   - `data/` - 爬取的数据文件（JSON格式）
   - `requirements.txt` - 依赖配置

6. **SearchAllNewsPlatform-main** - 多平台新闻搜索
   - `all_search.py` - 统一搜索接口
   - `search_sohu.py`, `search_toutiao.py`, `search_weibo.py` - 各平台实现
   - `filter.py`, `storage.py`, `util.py` - 数据处理工具

7. **Spider-main** - 通用爬虫框架
   - `SimPrograms/` - 简单爬虫示例（淘宝、当当、B站等）
   - `SpiderPro/` - 专业爬虫脚本（多个新闻网站）
   - `Spi_DataSave/` - 数据保存示例
   - `utils/` - 工具函数（格式化、正则测试等）

8. **docs-main** - DrissionPage教程文档
   - `DrissionPage_tutorial/` - 完整教程（基础、进阶、高级）
   - `mcp_tutorial/` - MCP协议教程（20+篇文档）

9. **music163_crawler-master** - 网易云音乐爬虫
   - `JS_music_comments.py`, `hot_comment.py` - 评论爬虫
   - `comments.js` - JavaScript加密处理
   - `music_data.csv` - 爬取的音乐数据
   - `music_data/`, `music_href/` - 数据文件夹

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

### 5. 使用SSH一键提交脚本
项目提供了两个一键提交脚本，方便快速将代码提交到GitHub仓库：

- `ssh_git_commit.bat` - Windows批处理脚本
- `ssh_git_commit.ps1` - PowerShell脚本

使用方法：
1. 确保已配置好SSH密钥并添加到GitHub账户
2. 双击运行对应的脚本文件
3. 按提示输入提交信息（可选）
4. 脚本将自动完成添加、提交和推送操作

注意：脚本默认使用SSH方式推送到`git@github.com:huangwei-gem/code.git`仓库。

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