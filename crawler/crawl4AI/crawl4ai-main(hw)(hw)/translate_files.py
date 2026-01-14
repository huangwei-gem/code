import os
import json
import re
from googletrans import Translator

translator = Translator()

# 定义源目录和目标目录
source_dir = "docs/examples"
target_dir = "docs/examples_chinese"

# 加载待处理清单
with open("translation_todo_list.json", "r", encoding="utf-8") as f:
    todo_list = json.load(f)

# 定义文件夹和文件的中文命名映射
name_mapping = {
    # 文件夹命名映射
    "adaptive_crawling": "自适应爬取",
    "assets": "资源",
    "c4a_script": "c4a脚本",
    "amazon_example": "亚马逊示例",
    "github_search": "GitHub搜索",
    "script_samples": "脚本示例",
    "tutorial": "教程",
    "capsolver_captcha_solver": "Capsolver验证码解决",
    "capsolver_api_integration": "Capsolver API集成",
    "capsolver_extension_integration": "Capsolver扩展集成",
    "cli": "命令行界面",
    "cloud_browser": "云浏览器",
    "docker": "Docker",
    "markdown": "Markdown",
    "nst_proxy": "NST代理",
    "undetectability": "不可检测性",
    "url_seeder": "URL种子",
    "website-to-api": "网站转API",
    "static": "静态资源",
    
    # .py 文件命名映射（部分示例，需要根据实际情况补充）
    "advanced_configuration.py": "高级配置.py",
    "basic_usage.py": "基本用法.py",
    "custom_strategies.py": "自定义策略.py",
    "embedding_configuration.py": "嵌入配置.py",
    "embedding_strategy.py": "嵌入策略.py",
    "embedding_vs_statistical.py": "嵌入与统计对比.py",
    "export_import_kb.py": "知识库导出导入.py",
    "llm_config_example.py": "LLM配置示例.py",
    "amazon_product_extraction_direct_url.py": "亚马逊产品提取直接URL.py",
    "amazon_product_extraction_using_hooks.py": "使用钩子提取亚马逊产品.py",
    "amazon_product_extraction_using_use_javascript.py": "使用JavaScript提取亚马逊产品.py",
    "arun_vs_arun_many.py": "arun与arun_many对比.py",
    "async_webcrawler_multiple_urls_example.py": "异步网络爬虫多URL示例.py",
    "browser_optimization_example.py": "浏览器优化示例.py",
    "builtin_browser_example.py": "内置浏览器示例.py",
    "amazon_r2d2_search.py": "亚马逊R2D2搜索.py",
    "api_usage_examples.py": "API使用示例.py",
    "c4a_script_hello_world.py": "c4a脚本Hello World.py",
    "c4a_script_hello_world_error.py": "c4a脚本Hello World错误示例.py",
    "demo_c4a_crawl4ai.py": "演示c4a_crawl4ai.py",
    "generate_script_hello_world.py": "生成脚本Hello World.py",
    "scrapeless_browser.py": "无抓取浏览器.py",
    "crawlai_vs_firecrawl.py": "CrawlAI与Firecrawl对比.py",
    "crawler_monitor_example.py": "爬虫监控示例.py",
    "crypto_analysis_example.py": "加密分析示例.py",
    "deepcrawl_example.py": "深度爬取示例.py",
    "demo_multi_config_clean.py": "演示多配置清洁.py",
    "dfs_crawl_demo.py": "DFS爬取演示.py",
    "dispatcher_example.py": "调度器示例.py",
    "demo_docker_api.py": "演示Docker API.py",
    "demo_docker_polling.py": "演示Docker轮询.py",
    "docker_client_hooks_example.py": "Docker客户端钩子示例.py",
    "docker_config_obj.py": "Docker配置对象.py",
    "docker_example.py": "Docker示例.py",
    "docker_hooks_examples.py": "Docker钩子示例.py",
    "docker_python_rest_api.py": "Docker Python REST API.py",
    "docker_python_sdk.py": "Docker Python SDK.py",
    "docker_webhook_example.py": "Docker Webhook示例.py",
    "extraction_strategies_examples.py": "提取策略示例.py",
    "hello_world.py": "Hello World.py",
    "hello_world_undetected.py": "不可检测Hello World.py",
    "hooks_example.py": "钩子示例.py",
    "identity_based_browsing.py": "基于身份的浏览.py",
    "language_support_example.py": "语言支持示例.py",
    "link_head_extraction_example.py": "链接头部提取示例.py",
    "llm_extraction_openai_pricing.py": "LLM提取OpenAI定价.py",
    "llm_markdown_generator.py": "LLM Markdown生成器.py",
    "llm_table_extraction_example.py": "LLM表格提取示例.py",
    "content_source_example.py": "内容源示例.py",
    "content_source_short_example.py": "内容源简短示例.py",
    "network_console_capture_example.py": "网络控制台捕获示例.py",
    "api_proxy_example.py": "API代理示例.py",
    "auth_proxy_example.py": "认证代理示例.py",
    "basic_proxy_example.py": "基本代理示例.py",
    "nstproxy_example.py": "NST代理示例.py",
    "proxy_rotation_demo.py": "代理轮换演示.py",
    "quickstart.py": "快速开始.py",
    "quickstart_examples_set_1.py": "快速开始示例集1.py",
    "quickstart_examples_set_2.py": "快速开始示例集2.py",
    "regex_extraction_quickstart.py": "正则表达式提取快速开始.py",
    "research_assistant.py": "研究助手.py",
    "rest_call.py": "REST调用.py",
    "scraping_strategies_performance.py": "抓取策略性能.py",
    "serp_api_project_11_feb.py": "SERP API项目2月11日.py",
    "session_id_example.py": "会话ID示例.py",
    "simple_anti_bot_examples.py": "简单反机器人示例.py",
    "ssl_example.py": "SSL示例.py",
    "stealth_mode_example.py": "隐身模式示例.py",
    "stealth_mode_quick_start.py": "隐身模式快速开始.py",
    "stealth_test_simple.py": "简单隐身测试.py",
    "summarize_page.py": "页面总结.py",
    "table_extraction_example.py": "表格提取示例.py",
    "tutorial_v0.5.py": "教程v0.5.py",
    "undetected_basic_test.py": "不可检测基本测试.py",
    "undetected_bot_test.py": "不可检测机器人测试.py",
    "undetected_cloudflare_test.py": "不可检测Cloudflare测试.py",
    "undetected_vs_regular_comparison.py": "不可检测与常规对比.py",
    "undetected_simple_demo.py": "不可检测简单演示.py",
    "bbc_sport_research_assistant.py": "BBC体育研究助手.py",
    "convert_tutorial_to_colab.py": "转换教程到Colab.py",
    "url_seeder_demo.py": "URL种子演示.py",
    "url_seeder_quick_demo.py": "URL种子快速演示.py",
    "use_geo_location.py": "使用地理位置.py",
    "virtual_scroll_example.py": "虚拟滚动示例.py",
    "api_server.py": "API服务器.py",
    "app.py": "应用.py",
    "test_api.py": "测试API.py",
    "test_models.py": "测试模型.py",
    "web_scraper_lib.py": "网络抓取库.py"
}

# 翻译文本函数
def translate_text(text):
    try:
        # 翻译文本
        translated = translator.translate(text, src='en', dest='zh-cn')
        return translated.text
    except Exception as e:
        print(f"翻译错误: {e}")
        return text

# 翻译Python文件函数
def translate_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译注释
    def translate_comment(match):
        comment = match.group(0)
        if comment.startswith("#"):
            # 单行注释
            translated = "# " + translate_text(comment[2:].strip())
            return translated
        elif comment.startswith('"""') or comment.startswith("'''"):
            # 多行注释
            quote = comment[:3]
            translated = quote + translate_text(comment[3:-3].strip()) + quote
            return translated
        return comment
    
    # 翻译字符串
    def translate_string(match):
        string = match.group(0)
        quote = string[0]
        translated = quote + translate_text(string[1:-1].strip()) + quote
        return translated
    
    # 翻译注释
    content = re.sub(r'#.*$|"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', translate_comment, content, flags=re.MULTILINE)
    
    # 翻译字符串（注意：这可能会影响代码逻辑，需要谨慎使用）
    # content = re.sub(r'"[^"]*"|\'[^\']*\'', translate_string, content)
    
    return content

# 翻译Markdown文件函数
def translate_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译Markdown内容
    translated = translate_text(content)
    return translated

# 翻译HTML文件函数
def translate_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 翻译HTML内容，保留标签
    def translate_html_content(match):
        text = match.group(1)
        translated = translate_text(text)
        return translated
    
    translated = re.sub(r'>([^<]+)<', lambda m: '>' + translate_text(m.group(1)) + '<', content)
    return translated

# 处理文件翻译
def process_file_translation():
    for file_path in todo_list["未翻译文件"]:
        # 获取完整源文件路径
        full_source_path = os.path.join(source_dir, file_path)
        
        # 获取目标文件路径
        full_target_path = os.path.join(target_dir, file_path)
        
        print(f"翻译文件: {file_path}")
        
        # 根据文件类型选择翻译方法
        if file_path.endswith(".py"):
            translated_content = translate_python_file(full_source_path)
        elif file_path.endswith(".md"):
            translated_content = translate_markdown_file(full_source_path)
        elif file_path.endswith(".html"):
            translated_content = translate_html_file(full_source_path)
        else:
            # 对于其他文件类型，直接复制
            with open(full_source_path, "rb") as f:
                translated_content = f.read()
            with open(full_target_path, "wb") as f:
                f.write(translated_content)
            continue
        
        # 写入翻译后的内容
        with open(full_target_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

# 处理文件夹和文件重命名
def process_renaming():
    # 首先处理文件重命名，因为文件夹重命名会影响文件路径
    for file_path in todo_list["待重命名.py 文件"]:
        # 获取文件所在目录和文件名
        dir_path, file_name = os.path.split(file_path)
        
        # 获取中文文件名
        if file_name in name_mapping:
            chinese_file_name = name_mapping[file_name]
        else:
            # 如果没有映射，使用翻译后的文件名
            chinese_file_name = translate_text(file_name[:-3]) + ".py"
        
        # 构建源路径和目标路径
        full_source_path = os.path.join(target_dir, file_path)
        full_target_path = os.path.join(target_dir, dir_path, chinese_file_name)
        
        print(f"重命名文件: {file_path} -> {os.path.join(dir_path, chinese_file_name)}")
        
        # 重命名文件
        if os.path.exists(full_source_path):
            os.rename(full_source_path, full_target_path)
    
    # 处理文件夹重命名（需要从最深层开始重命名）
    # 按路径深度排序，从深到浅
    folders = sorted(todo_list["待重命名文件夹"], key=lambda x: x.count(os.sep), reverse=True)
    
    for folder_path in folders:
        # 获取父目录和文件夹名
        parent_dir, folder_name = os.path.split(folder_path)
        
        # 获取中文文件夹名
        if folder_name in name_mapping:
            chinese_folder_name = name_mapping[folder_name]
        else:
            # 如果没有映射，使用翻译后的文件夹名
            chinese_folder_name = translate_text(folder_name)
        
        # 构建源路径和目标路径
        full_source_path = os.path.join(target_dir, folder_path)
        full_target_path = os.path.join(target_dir, parent_dir, chinese_folder_name)
        
        print(f"重命名文件夹: {folder_path} -> {os.path.join(parent_dir, chinese_folder_name)}")
        
        # 重命名文件夹
        if os.path.exists(full_source_path):
            os.rename(full_source_path, full_target_path)

# 执行翻译和重命名
if __name__ == "__main__":
    # 先执行文件翻译
    process_file_translation()
    
    # 再执行重命名
    process_renaming()
    
    print("翻译和重命名完成！")
