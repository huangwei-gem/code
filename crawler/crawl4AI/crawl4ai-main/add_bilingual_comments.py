#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为文件添加中英双注释的脚本

功能：
1. 读取清单文件中的文件列表
2. 遍历每个文件，为中文注释添加对应的英文注释
3. 更新清单文件中的状态
4. 生成处理报告
"""

import os
import re
from pathlib import Path

def read_translation_list(list_path):
    """读取翻译清单文件"""
    files = []
    with open(list_path, 'r', encoding='utf-8-sig') as f:  # 使用utf-8-sig处理BOM
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                file_path, status = line.split(',')
                # 移除可能的BOM字符
                if file_path.startswith('\ufeff'):
                    file_path = file_path[1:]
                files.append((file_path, status))
    return files


def write_translation_list(list_path, files):
    """写入翻译清单文件"""
    with open(list_path, 'w', encoding='utf-8') as f:
        f.write("# 需要添加中英双注释的文件清单\n")
        f.write("# 格式：文件路径,状态（pending/done）\n\n")
        f.write("# 根目录文件\n")
        
        # 先写入根目录文件
        for file_path, status in files:
            if '/' not in file_path:
                f.write(f"{file_path},{status}\n")
        
        f.write("\n# 子目录文件\n")
        
        # 再写入子目录文件
        for file_path, status in files:
            if '/' in file_path:
                f.write(f"{file_path},{status}\n")


def get_original_file_path(chinese_file_path):
    """根据中文文件名获取原始英文文件路径"""
    # 移除examples_chinese前缀
    relative_path = chinese_file_path.replace('examples_chinese/', '')
    
    # 读取翻译映射关系
    mapping = {}
    with open('translation_manifest.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('-') and '->' in line:
                # 移除行首的 "- "
                line = line[2:].strip()
                parts = line.split('->')
                if len(parts) >= 2:
                    original = parts[0].strip()
                    translated = parts[1].strip().replace('✓', '').strip()
                    mapping[translated] = original
    
    # 查找对应的原始文件
    if relative_path in mapping:
        return f"docs/examples/{mapping[relative_path]}"
    
    # 如果找不到精确匹配，尝试查找目录映射
    for translated_dir, original_dir in mapping.items():
        if translated_dir.endswith('/') and relative_path.startswith(translated_dir):
            remaining = relative_path[len(translated_dir):]
            return f"docs/examples/{original_dir}{remaining}"
    
    # 处理反斜杠问题（Windows路径）
    relative_path_slash = relative_path.replace('\\', '/')
    if relative_path_slash in mapping:
        return f"docs/examples/{mapping[relative_path_slash]}"
    
    # 处理目录映射中的反斜杠
    for translated_dir, original_dir in mapping.items():
        if translated_dir.endswith('/') and relative_path_slash.startswith(translated_dir):
            remaining = relative_path_slash[len(translated_dir):]
            return f"docs/examples/{original_dir}{remaining}"
    
    # 构建完整的简单映射（包含所有可能的文件）
    simple_mapping = {
        # 根目录文件
        'crawl4ai_vs_firecrawl对比.py': 'crawlai_vs_firecrawl.py',
        'Docker_Python_REST_API.py': 'docker_python_rest_api.py',
        'Docker_Python_SDK.py': 'docker_python_sdk.py',
        'Docker_webhook示例.py': 'docker_webhook_example.py',
        'Docker客户端钩子示例.py': 'docker_client_hooks_example.py',
        'Docker示例.py': 'docker_example.py',
        'Docker配置对象.py': 'docker_config_obj.py',
        'Docker钩子示例.py': 'docker_hooks_examples.py',
        'LLM_Markdown生成器.py': 'llm_markdown_generator.py',
        'LLM提取_OpenAI定价.py': 'llm_extraction_openai_pricing.py',
        'LLM表格提取示例.py': 'llm_table_extraction_example.py',
        'REST调用.py': 'rest_call.py',
        'SERP_API项目_11月.py': 'serp_api_project_11_feb.py',
        'SSL示例.py': 'ssl_example.py',
        'v0.5教程.py': 'tutorial_v0.5.py',
        '亚马逊产品提取_使用JavaScript.py': 'amazon_product_extraction_using_use_javascript.py',
        '亚马逊产品提取_使用钩子.py': 'amazon_product_extraction_using_hooks.py',
        '亚马逊产品提取_直接URL.py': 'amazon_product_extraction_direct_url.py',
        '亚马逊产品提取直接URL.py': 'amazon_product_extraction_direct_url.py',
        '代理轮换演示.py': 'proxy_rotation_demo.py',
        '会话ID示例.py': 'session_id_example.py',
        '你好世界.py': 'hello_world.py',
        '你好世界_反检测.py': 'hello_world_undetected.py',
        '你好世界_无检测.py': 'hello_world_undetected.py',
        '使用LLM提取OpenAI定价.py': 'llm_extraction_openai_pricing.py',
        '使用地理位置.py': 'use_geo_location.py',
        '内置浏览器示例.py': 'builtin_browser_example.py',
        '加密货币分析示例.py': 'crypto_analysis_example.py',
        '单次爬取与批量爬取对比.py': 'arun_vs_arun_many.py',
        '单次运行_vs_批量运行.py': 'arun_vs_arun_many.py',
        '反检测简单演示.py': 'undetected_simple_demo.py',
        '基于身份的浏览.py': 'identity_based_browsing.py',
        '多配置清理演示.py': 'demo_multi_config_clean.py',
        '异步爬虫多URL示例.py': 'async_webcrawler_multiple_urls_example.py',
        '异步网络爬虫_多URL示例.py': 'async_webcrawler_multiple_urls_example.py',
        '异步网络爬虫多URL示例.py': 'async_webcrawler_multiple_urls_example.py',
        '快速入门.py': 'quickstart.py',
        '快速入门示例集_1.py': 'quickstart_examples_set_1.py',
        '快速入门示例集_2.py': 'quickstart_examples_set_2.py',
        '快速开始.py': 'quickstart.py',
        '提取策略示例.py': 'extraction_strategies_examples.py',
        '正则表达式提取快速入门.py': 'regex_extraction_quickstart.py',
        '浏览器优化示例.py': 'browser_optimization_example.py',
        '深度优先爬取演示.py': 'dfs_crawl_demo.py',
        '深度爬取示例.py': 'deepcrawl_example.py',
        '爬取策略性能.py': 'scraping_strategies_performance.py',
        '爬虫监控示例.py': 'crawler_monitor_example.py',
        '研究助手.py': 'research_assistant.py',
        '简单反机器人示例.py': 'simple_anti_bot_examples.py',
        '简单隐身测试.py': 'stealth_test_simple.py',
        '网络和控制台捕获示例.py': 'network_console_capture_example.py',
        '虚拟滚动示例.py': 'virtual_scroll_example.py',
        '表格提取示例.py': 'table_extraction_example.py',
        '语言支持示例.py': 'language_support_example.py',
        '调度器示例.py': 'dispatcher_example.py',
        '钩子示例.py': 'hooks_example.py',
        '链接头部提取示例.py': 'link_head_extraction_example.py',
        '隐身模式快速开始.py': 'stealth_mode_quick_start.py',
        '隐身模式示例.py': 'stealth_mode_example.py',
        '页面摘要.py': 'summarize_page.py',
        
        # Docker容器目录
        'Docker容器/Docker_API演示.py': 'docker/demo_docker_api.py',
        'Docker容器/Docker轮询演示.py': 'docker/demo_docker_polling.py',
        
        # URL种子目录
        'URL种子/BBC体育研究助手.py': 'url_seeder/bbc_sport_research_assistant.py',
        'URL种子/URL种子快速演示.py': 'url_seeder/url_seeder_quick_demo.py',
        'URL种子/URL种子演示.py': 'url_seeder/url_seeder_demo.py',
        'URL种子/转换教程到Colab.py': 'url_seeder/convert_tutorial_to_colab.py',
        
        # c4a脚本目录
        'c4a脚本/API使用示例.py': 'c4a_script/api_usage_examples.py',
        'c4a脚本/GitHub搜索/GitHub搜索爬虫.py': 'c4a_script/github_search/github_search_crawler.py',
        'c4a脚本/c4a_crawl4ai演示.py': 'c4a_script/demo_c4a_crawl4ai.py',
        'c4a脚本/c4a脚本你好世界.py': 'c4a_script/c4a_script_hello_world.py',
        'c4a脚本/c4a脚本你好世界错误.py': 'c4a_script/c4a_script_hello_world_error.py',
        'c4a脚本/亚马逊示例/亚马逊R2D2搜索.py': 'c4a_script/amazon_example/amazon_r2d2_search.py',
        'c4a脚本/教程/服务器.py': 'c4a_script/tutorial/server.py',
        'c4a脚本/生成脚本你好世界.py': 'c4a_script/generate_script_hello_world.py',
        
        # markdown目录
        'markdown/内容来源示例.py': 'markdown/content_source_example.py',
        
        # 云浏览器目录
        '云浏览器/无抓取浏览器.py': 'cloud_browser/scrapeless_browser.py',
        
        # 代理配置目录
        '代理配置/API代理示例.py': 'nst_proxy/api_proxy_example.py',
        '代理配置/nstproxy示例.py': 'nst_proxy/nstproxy_example.py',
        '代理配置/基本代理示例.py': 'nst_proxy/basic_proxy_example.py',
        '代理配置/认证代理示例.py': 'nst_proxy/auth_proxy_example.py',
        
        # 反检测目录
        '反检测/反检测Cloudflare测试.py': 'undetectability/undetected_cloudflare_test.py',
        '反检测/反检测_vs_常规对比.py': 'undetectability/undetected_vs_regular_comparison.py',
        '反检测/反检测基础测试.py': 'undetectability/undetected_basic_test.py',
        '反检测/反检测机器人测试.py': 'undetectability/undetected_bot_test.py',
        
        # 文档转换目录
        '文档转换/内容源示例.py': 'markdown/content_source_example.py',
        '文档转换/内容源简短示例.py': 'markdown/content_source_short_example.py',
        
        # 网站转API目录
        '网站转API/API服务器.py': 'website-to-api/api_server.py',
        '网站转API/应用.py': 'website-to-api/app.py',
        '网站转API/测试API.py': 'website-to-api/test_api.py',
        '网站转API/测试模型.py': 'website-to-api/test_models.py',
        '网站转API/网页爬虫库.py': 'website-to-api/web_scraper_lib.py',
        
        # 自适应爬取目录
        '自适应爬取/LLM配置示例.py': 'adaptive_crawling/llm_config_example.py',
        '自适应爬取/基本用法.py': 'adaptive_crawling/basic_usage.py',
        '自适应爬取/导出导入知识库.py': 'adaptive_crawling/export_import_kb.py',
        '自适应爬取/嵌入_vs_统计.py': 'adaptive_crawling/embedding_vs_statistical.py',
        '自适应爬取/嵌入vs统计策略.py': 'adaptive_crawling/embedding_vs_statistical.py',
        '自适应爬取/嵌入策略.py': 'adaptive_crawling/embedding_strategy.py',
        '自适应爬取/嵌入配置.py': 'adaptive_crawling/embedding_configuration.py',
        '自适应爬取/知识库导出导入.py': 'adaptive_crawling/export_import_kb.py',
        '自适应爬取/自定义策略.py': 'adaptive_crawling/custom_strategies.py',
        '自适应爬取/高级配置.py': 'adaptive_crawling/advanced_configuration.py',
        
        # 验证码求解器目录
        '验证码求解器/验证码API集成/解决AWS_WAF.py': 'capsolver_captcha_solver/capsolver_api_integration/solve_aws_waf.py',
        '验证码求解器/验证码API集成/解决Cloudflare_turnstile.py': 'capsolver_captcha_solver/capsolver_api_integration/solve_cloudflare_turnstile.py',
        '验证码求解器/验证码API集成/解决Cloudflare挑战.py': 'capsolver_captcha_solver/capsolver_api_integration/solve_cloudflare_challenge.py',
        '验证码求解器/验证码API集成/解决reCAPTCHA_v2.py': 'capsolver_captcha_solver/capsolver_api_integration/solve_recaptcha_v2.py',
        '验证码求解器/验证码API集成/解决reCAPTCHA_v3.py': 'capsolver_captcha_solver/capsolver_api_integration/solve_recaptcha_v3.py',
        '验证码求解器/验证码插件集成/解决AWS_WAF.py': 'capsolver_captcha_solver/capsolver_extension_integration/solve_aws_waf.py',
        '验证码求解器/验证码插件集成/解决Cloudflare_turnstile.py': 'capsolver_captcha_solver/capsolver_extension_integration/solve_cloudflare_turnstile.py',
        '验证码求解器/验证码插件集成/解决Cloudflare挑战.py': 'capsolver_captcha_solver/capsolver_extension_integration/solve_cloudflare_challenge.py',
        '验证码求解器/验证码插件集成/解决reCAPTCHA_v2.py': 'capsolver_captcha_solver/capsolver_extension_integration/solve_recaptcha_v2.py',
        '验证码求解器/验证码插件集成/解决reCAPTCHA_v3.py': 'capsolver_captcha_solver/capsolver_extension_integration/solve_recaptcha_v3.py'
    }
    
    # 尝试直接匹配
    if relative_path in simple_mapping:
        return f"docs/examples/{simple_mapping[relative_path]}"
    
    # 尝试匹配斜杠版本
    if relative_path_slash in simple_mapping:
        return f"docs/examples/{simple_mapping[relative_path_slash]}"
    
    # 尝试匹配不带路径的文件名
    filename = os.path.basename(relative_path)
    for mapped_path, original_path in simple_mapping.items():
        if os.path.basename(mapped_path) == filename:
            return f"docs/examples/{original_path}"
    
    # 最后尝试直接构造路径
    # 例如：examples_chinese\xxx.py -> docs/examples/xxx.py
    # 替换中文文件名中的特殊字符为英文
    possible_original = relative_path
    possible_original = possible_original.replace('对比', 'vs')
    possible_original = possible_original.replace('示例', 'example')
    possible_original = possible_original.replace('演示', 'demo')
    possible_original = possible_original.replace('使用', 'using')
    possible_original = possible_original.replace('直接', 'direct')
    possible_original = possible_original.replace('异步', 'async')
    possible_original = possible_original.replace('网络爬虫', 'webcrawler')
    possible_original = possible_original.replace('浏览器', 'browser')
    possible_original = possible_original.replace('优化', 'optimization')
    possible_original = possible_original.replace('内置', 'builtin')
    possible_original = possible_original.replace('深度', 'deep')
    possible_original = possible_original.replace('爬取', 'crawl')
    possible_original = possible_original.replace('提取', 'extraction')
    possible_original = possible_original.replace('策略', 'strategies')
    possible_original = possible_original.replace('自适应', 'adaptive')
    possible_original = possible_original.replace('基本', 'basic')
    possible_original = possible_original.replace('用法', 'usage')
    possible_original = possible_original.replace('高级', 'advanced')
    possible_original = possible_original.replace('配置', 'configuration')
    possible_original = possible_original.replace('自定义', 'custom')
    possible_original = possible_original.replace('API', 'api')
    possible_original = possible_original.replace('脚本', 'script')
    possible_original = possible_original.replace('代理', 'proxy')
    possible_original = possible_original.replace('认证', 'auth')
    possible_original = possible_original.replace('反检测', 'undetected')
    possible_original = possible_original.replace('基础', 'basic')
    possible_original = possible_original.replace('测试', 'test')
    possible_original = possible_original.replace('机器人', 'bot')
    possible_original = possible_original.replace('URL', 'url')
    possible_original = possible_original.replace('种子', 'seeder')
    possible_original = possible_original.replace('网站', 'website')
    possible_original = possible_original.replace('转', 'to')
    possible_original = possible_original.replace('服务器', 'server')
    possible_original = possible_original.replace('应用', 'app')
    possible_original = possible_original.replace('网页', 'web')
    possible_original = possible_original.replace('爬虫', 'crawler')
    possible_original = possible_original.replace('库', 'lib')
    possible_original = possible_original.replace('虚拟', 'virtual')
    possible_original = possible_original.replace('滚动', 'scroll')
    possible_original = possible_original.replace('表格', 'table')
    possible_original = possible_original.replace('语言', 'language')
    possible_original = possible_original.replace('支持', 'support')
    possible_original = possible_original.replace('调度器', 'dispatcher')
    possible_original = possible_original.replace('钩子', 'hooks')
    possible_original = possible_original.replace('链接', 'link')
    possible_original = possible_original.replace('头部', 'head')
    possible_original = possible_original.replace('隐身', 'stealth')
    possible_original = possible_original.replace('模式', 'mode')
    possible_original = possible_original.replace('快速', 'quick')
    possible_original = possible_original.replace('开始', 'start')
    possible_original = possible_original.replace('页面', 'page')
    possible_original = possible_original.replace('摘要', 'summarize')
    possible_original = possible_original.replace('SSL', 'ssl')
    possible_original = possible_original.replace('SERP', 'serp')
    possible_original = possible_original.replace('项目', 'project')
    possible_original = possible_original.replace('月', 'feb')
    possible_original = possible_original.replace('教程', 'tutorial')
    possible_original = possible_original.replace('加密货币', 'crypto')
    possible_original = possible_original.replace('分析', 'analysis')
    possible_original = possible_original.replace('单次', 'single')
    possible_original = possible_original.replace('运行', 'run')
    possible_original = possible_original.replace('批量', 'many')
    possible_original = possible_original.replace('基于', 'based')
    possible_original = possible_original.replace('身份', 'identity')
    possible_original = possible_original.replace('浏览', 'browsing')
    possible_original = possible_original.replace('多', 'multi')
    possible_original = possible_original.replace('配置', 'config')
    possible_original = possible_original.replace('清理', 'clean')
    possible_original = possible_original.replace('正则表达式', 'regex')
    possible_original = possible_original.replace('优先', 'first')
    possible_original = possible_original.replace('性能', 'performance')
    possible_original = possible_original.replace('监控', 'monitor')
    possible_original = possible_original.replace('研究', 'research')
    possible_original = possible_original.replace('助手', 'assistant')
    possible_original = possible_original.replace('简单', 'simple')
    possible_original = possible_original.replace('反机器人', 'anti_bot')
    possible_original = possible_original.replace('网络', 'network')
    possible_original = possible_original.replace('控制台', 'console')
    possible_original = possible_original.replace('捕获', 'capture')
    possible_original = possible_original.replace('验证码', 'captcha')
    possible_original = possible_original.replace('求解器', 'solver')
    possible_original = possible_original.replace('API集成', 'api_integration')
    possible_original = possible_original.replace('插件集成', 'extension_integration')
    possible_original = possible_original.replace('解决', 'solve')
    possible_original = possible_original.replace('挑战', 'challenge')
    
    # 将中文文件名转换为小写并替换空格和下划线
    possible_original = possible_original.lower()
    possible_original = possible_original.replace(' ', '_')
    
    # 尝试直接构造路径
    test_path = f"docs/examples/{possible_original}"
    if os.path.exists(test_path):
        return test_path
    
    # 最后尝试替换路径分隔符
    test_path = test_path.replace('\\', '/')
    if os.path.exists(test_path):
        return test_path
    
    return None


def add_bilingual_comments(file_path):
    """为文件添加中英双注释"""
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取原始英文文件路径
    original_file_path = get_original_file_path(file_path)
    
    if not original_file_path or not os.path.exists(original_file_path):
        print(f"[WARNING] 找不到原始英文文件: {original_file_path}")
        return False
    
    # 读取原始英文文件内容
    with open(original_file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # 按行处理
    new_lines = []
    original_lines = original_content.split('\n')
    chinese_lines = content.split('\n')
    
    for i, (chinese_line, original_line) in enumerate(zip(chinese_lines, original_lines)):
        # 处理行注释
        if chinese_line.strip().startswith('#') and not original_line.strip().startswith('#'):
            # 中文行注释，添加英文注释
            comment_text = chinese_line.strip()[1:].strip()
            # 尝试从原始文件的前后行找到对应的英文注释
            english_comment = ""
            # 检查原始文件的相同行附近是否有注释
            for j in range(max(0, i-2), min(len(original_lines), i+3)):
                if original_lines[j].strip().startswith('#'):
                    english_comment = original_lines[j].strip()[1:].strip()
                    break
            
            if english_comment:
                new_line = f"# {english_comment}\n# {comment_text}"
            else:
                new_line = chinese_line
        elif chinese_line.strip().startswith('#') and original_line.strip().startswith('#'):
            # 中英文都有注释，合并
            chinese_comment = chinese_line.strip()[1:].strip()
            english_comment = original_line.strip()[1:].strip()
            if chinese_comment != english_comment:
                new_line = f"# {english_comment}\n# {chinese_comment}"
            else:
                new_line = chinese_line
        elif '#' in chinese_line and '#' in original_line:
            # 行内注释
            chinese_part, chinese_comment = chinese_line.split('#', 1)
            original_part, original_comment = original_line.split('#', 1)
            
            # 检查代码部分是否匹配
            if chinese_part.strip() == original_part.strip():
                chinese_comment_text = chinese_comment.strip()
                original_comment_text = original_comment.strip()
                
                if chinese_comment_text != original_comment_text:
                    new_line = f"{chinese_part}# {original_comment_text}\n# {chinese_comment_text}"
                else:
                    new_line = chinese_line
            else:
                new_line = chinese_line
        else:
            # 没有注释或注释处理不了，保持原样
            new_line = chinese_line
        
        new_lines.append(new_line)
    
    # 写入更新后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    return True


def main():
    """主函数"""
    list_path = 'translation_bilingual_list_all.txt'
    
    # 读取清单
    files = read_translation_list(list_path)
    
    # 处理每个文件
    processed_count = 0
    skipped_count = 0
    
    for i, (file_path, status) in enumerate(files):
        if status == 'done':
            print(f"[{i+1}/{len(files)}] 跳过已处理文件: {file_path}")
            skipped_count += 1
            continue
        
        print(f"[{i+1}/{len(files)}] 处理文件: {file_path}")
        
        try:
            success = add_bilingual_comments(file_path)
            if success:
                files[i] = (file_path, 'done')
                processed_count += 1
                print(f"[{i+1}/{len(files)}] 成功处理: {file_path}")
            else:
                print(f"[{i+1}/{len(files)}] 处理失败: {file_path}")
        except Exception as e:
            print(f"[{i+1}/{len(files)}] 处理出错: {file_path} - {e}")
    
    # 更新清单文件
    write_translation_list(list_path, files)
    
    # 生成报告
    print(f"\n=== 处理完成 ===")
    print(f"总文件数: {len(files)}")
    print(f"已处理: {processed_count}")
    print(f"已跳过: {skipped_count}")
    print(f"剩余未处理: {len(files) - processed_count - skipped_count}")
    print(f"清单文件已更新: {list_path}")


if __name__ == "__main__":
    main()