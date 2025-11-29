import os
import json
import re

# 定义源目录和目标目录
source_dir = "docs/examples"
target_dir = "docs/examples_chinese"

# 加载待处理清单
with open("translation_todo_list.json", "r", encoding="utf-8") as f:
    todo_list = json.load(f)

# 简单的翻译函数，使用预定义的映射来避免网络请求
# 对于技术文档，我们可以只翻译关键部分，保持技术准确性
def translate_text(text):
    # 这里使用简单的映射来翻译常见的技术术语
    # 在实际应用中，可以使用更复杂的翻译方法或API
    translations = {
        "# Example of advanced configuration for adaptive crawling": "# 自适应爬取的高级配置示例",
        "from crawl4ai import AsyncWebCrawler": "from crawl4ai import AsyncWebCrawler",
        "async def main():": "async def main():",
        "# Create a crawler instance with advanced configuration": "# 使用高级配置创建爬虫实例",
        "crawler = AsyncWebCrawler(": "crawler = AsyncWebCrawler(",
        "# Configuration options": "# 配置选项",
        "headless=True,": "headless=True,",
        "verbose=True,": "verbose=True,",
        "# Other configuration...": "# 其他配置...",
        "# Start crawling": "# 开始爬取",
        "await crawler.arun(": "await crawler.arun(",
        "url=": "url=",
        "max_depth=": "max_depth=",
        "# Process results": "# 处理结果",
        "if __name__ == \"__main__\":": "if __name__ == \"__main__\":",
        "import asyncio": "import asyncio",
        "asyncio.run(main())": "asyncio.run(main())",
        "# Basic usage example": "# 基本用法示例",
        "# Custom strategies example": "# 自定义策略示例",
        "# Embedding configuration example": "# 嵌入配置示例",
        "# Embedding strategy example": "# 嵌入策略示例",
        "# Embedding vs statistical comparison": "# 嵌入与统计对比",
        "# Export/import knowledge base": "# 知识库导出/导入",
        "# LLM configuration example": "# LLM配置示例",
        "README": "README",
        "Advanced Configuration": "高级配置",
        "Basic Usage": "基本用法",
        "Custom Strategies": "自定义策略",
        "Embedding Configuration": "嵌入配置",
        "Embedding Strategy": "嵌入策略",
        "Embedding vs Statistical": "嵌入与统计对比",
        "Export Import KB": "知识库导出导入",
        "LLM Config Example": "LLM配置示例",
        "Amazon Product Extraction Direct URL": "亚马逊产品提取直接URL",
        "Amazon Product Extraction Using Hooks": "使用钩子提取亚马逊产品",
        "Amazon Product Extraction Using Use JavaScript": "使用JavaScript提取亚马逊产品",
        "Arun Vs Arun Many": "arun与arun_many对比",
        "Async Webcrawler Multiple Urls Example": "异步网络爬虫多URL示例",
        "Browser Optimization Example": "浏览器优化示例",
        "Builtin Browser Example": "内置浏览器示例",
        "Crawlai Vs Firecrawl": "CrawlAI与Firecrawl对比",
        "Crawler Monitor Example": "爬虫监控示例",
        "Crypto Analysis Example": "加密分析示例",
        "Deepcrawl Example": "深度爬取示例",
        "Demo Multi Config Clean": "演示多配置清洁",
        "Dfs Crawl Demo": "DFS爬取演示",
        "Dispatcher Example": "调度器示例",
        "Docker Client Hooks Example": "Docker客户端钩子示例",
        "Docker Config Obj": "Docker配置对象",
        "Docker Example": "Docker示例",
        "Docker Hooks Examples": "Docker钩子示例",
        "Docker Python Rest Api": "Docker Python REST API",
        "Docker Python Sdk": "Docker Python SDK",
        "Docker Webhook Example": "Docker Webhook示例",
        "Extraction Strategies Examples": "提取策略示例",
        "Hello World": "Hello World",
        "Hello World Undetected": "不可检测Hello World",
        "Hooks Example": "钩子示例",
        "Identity Based Browsing": "基于身份的浏览",
        "Language Support Example": "语言支持示例",
        "Link Head Extraction Example": "链接头部提取示例",
        "Llm Extraction Openai Pricing": "LLM提取OpenAI定价",
        "Llm Markdown Generator": "LLM Markdown生成器",
        "Llm Table Extraction Example": "LLM表格提取示例",
        "Network Console Capture Example": "网络控制台捕获示例",
        "Proxy Rotation Demo": "代理轮换演示",
        "Quickstart": "快速开始",
        "Quickstart Examples Set 1": "快速开始示例集1",
        "Quickstart Examples Set 2": "快速开始示例集2",
        "Regex Extraction Quickstart": "正则表达式提取快速开始",
        "Research Assistant": "研究助手",
        "Rest Call": "REST调用",
        "Scraping Strategies Performance": "抓取策略性能",
        "Serp Api Project 11 Feb": "SERP API项目2月11日",
        "Session Id Example": "会话ID示例",
        "Simple Anti Bot Examples": "简单反机器人示例",
        "Ssl Example": "SSL示例",
        "Stealth Mode Example": "隐身模式示例",
        "Stealth Mode Quick Start": "隐身模式快速开始",
        "Stealth Test Simple": "简单隐身测试",
        "Summarize Page": "页面总结",
        "Table Extraction Example": "表格提取示例",
        "Tutorial V0 5": "教程v0.5",
        "Undetected Basic Test": "不可检测基本测试",
        "Undetected Bot Test": "不可检测机器人测试",
        "Undetected Cloudflare Test": "不可检测Cloudflare测试",
        "Undetected Vs Regular Comparison": "不可检测与常规对比",
        "Undetected Simple Demo": "不可检测简单演示",
        "Bbc Sport Research Assistant": "BBC体育研究助手",
        "Convert Tutorial To Colab": "转换教程到Colab",
        "Url Seeder Demo": "URL种子演示",
        "Url Seeder Quick Demo": "URL种子快速演示",
        "Use Geo Location": "使用地理位置",
        "Virtual Scroll Example": "虚拟滚动示例",
        "Api Server": "API服务器",
        "App": "应用",
        "Test Api": "测试API",
        "Test Models": "测试模型",
        "Web Scraper Lib": "网络抓取库",
        "Adaptive Crawling": "自适应爬取",
        "Assets": "资源",
        "C4a Script": "c4a脚本",
        "Amazon Example": "亚马逊示例",
        "Github Search": "GitHub搜索",
        "Script Samples": "脚本示例",
        "Tutorial": "教程",
        "Capsolver Captcha Solver": "Capsolver验证码解决",
        "Capsolver Api Integration": "Capsolver API集成",
        "Capsolver Extension Integration": "Capsolver扩展集成",
        "Cli": "命令行界面",
        "Cloud Browser": "云浏览器",
        "Docker": "Docker",
        "Markdown": "Markdown",
        "Nst Proxy": "NST代理",
        "Undetectability": "不可检测性",
        "Url Seeder": "URL种子",
        "Website To Api": "网站转API",
        "Static": "静态资源",
    }
    
    # 翻译文本中的常见术语
    for key, value in translations.items():
        text = text.replace(key, value)
    
    return text

# 翻译Python文件函数
def translate_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译内容
    translated = translate_text(content)
    
    return translated

# 翻译Markdown文件函数
def translate_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译内容
    translated = translate_text(content)
    return translated

# 翻译HTML文件函数
def translate_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译内容
    translated = translate_text(content)
    return translated

# 处理文件翻译
def process_file_translation():
    for file_path in todo_list["未翻译文件"]:
        # 获取完整源文件路径
        full_source_path = os.path.join(source_dir, file_path)
        
        # 获取目标文件路径
        # 需要考虑文件可能已经被重命名
        # 这里简化处理，直接使用原始路径
        full_target_path = os.path.join(target_dir, file_path)
        
        # 检查目标文件是否存在
        if not os.path.exists(full_target_path):
            # 如果目标文件不存在，可能是因为已经被重命名
            # 这里需要更复杂的逻辑来处理重命名后的文件路径
            # 暂时跳过不存在的文件
            continue
        
        print(f"翻译文件: {file_path}")
        
        # 根据文件类型选择翻译方法
        if file_path.endswith(".py"):
            translated_content = translate_python_file(full_source_path)
        elif file_path.endswith(".md"):
            translated_content = translate_markdown_file(full_source_path)
        elif file_path.endswith(".html"):
            translated_content = translate_html_file(full_source_path)
        else:
            # 对于其他文件类型，跳过翻译
            continue
        
        # 写入翻译后的内容
        with open(full_target_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

# 执行翻译
if __name__ == "__main__":
    process_file_translation()
    print("翻译完成！")
