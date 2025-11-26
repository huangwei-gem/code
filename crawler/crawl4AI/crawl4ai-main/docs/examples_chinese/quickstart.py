"""
Crawl4AI 快速入门示例
本示例展示了 Crawl4AI 的主要功能，包括基础爬取、内容清理、链接分析、JavaScript执行等。
"""

import os, sys
from crawl4ai import LLMConfig

# 添加项目路径到系统路径
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

import asyncio
import time
import json
import re
from typing import Dict
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai import (
    JsonCssExtractionStrategy,
    LLMExtractionStrategy,
)

# 获取当前文件位置
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print("Crawl4AI: 高级网络爬虫和数据提取工具")
print("GitHub 仓库: https://github.com/unclecode/crawl4ai")
print("Twitter: @unclecode")
print("网站: https://crawl4ai.com")


# 基础示例 - 简单爬取
async def simple_crawl():
    """最简单的爬取示例"""
    print("\n--- 基础使用 ---")
    
    # 浏览器配置
    browser_config = BrowserConfig(headless=True)  # 无头模式
    crawler_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)  # 绕过缓存

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",  # 目标网址
            config=crawler_config
        )
        print("爬取结果（前500字符）：")
        print(result.markdown[:500])


# 内容清理示例
async def clean_content():
    """演示如何清理和优化爬取的内容"""
    print("\n--- 内容清理 ---")
    
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # 绕过缓存
        excluded_tags=["nav", "footer", "aside"],  # 排除导航、页脚、侧边栏
        remove_overlay_elements=True,  # 移除覆盖元素
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.48,  # 内容过滤阈值
                threshold_type="fixed",  # 固定阈值
                min_word_threshold=0  # 最小词汇阈值
            ),
            options={"ignore_links": True},  # 忽略链接
        ),
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://en.wikipedia.org/wiki/Apple",  # 维基百科页面
            config=crawler_config,
        )
        
        # 比较原始内容和过滤后的内容长度
        full_markdown_length = len(result.markdown.raw_markdown)
        fit_markdown_length = len(result.markdown.fit_markdown)
        print(f"原始 Markdown 长度: {full_markdown_length}")
        print(f"优化后 Markdown 长度: {fit_markdown_length}")
        print(f"内容压缩率: {(1 - fit_markdown_length/full_markdown_length)*100:.1f}%")


# 链接分析示例
async def link_analysis():
    """分析页面中的链接"""
    print("\n--- 链接分析 ---")
    
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,  # 启用缓存
        exclude_external_links=True,    # 排除外部链接
        exclude_social_media_links=True,  # 排除社交媒体链接
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=crawler_config,
        )
        
        print(f"找到 {len(result.links['internal'])} 个内部链接")
        print(f"找到 {len(result.links['external'])} 个外部链接")

        print("\n前5个内部链接:")
        for link in result.links["internal"][:5]:
            print(f"链接: {link['href']}")
            print(f"文本: {link['text']}")
            print("-" * 40)


# JavaScript 执行示例
async def simple_example_with_running_js_code():
    """演示如何执行 JavaScript 代码"""
    print("\n--- 执行 JavaScript 代码 ---")

    browser_config = BrowserConfig(
        headless=True,  # 无头模式
        java_script_enabled=True  # 启用 JavaScript
    )

    # JavaScript 代码：点击"加载更多"按钮
    js_code = """
    const loadMoreButton = Array.from(document.querySelectorAll('button'))
        .find(button => button.textContent.includes('Load More'));
    loadMoreButton && loadMoreButton.click();
    """

    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # 绕过缓存
        js_code=js_code,  # 要执行的 JavaScript 代码
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=crawler_config
        )
        print("执行 JS 后的爬取结果（前500字符）：")
        print(result.markdown[:500])


# CSS 选择器示例
async def simple_example_with_css_selector():
    """使用 CSS 选择器提取特定内容"""
    print("\n--- 使用 CSS 选择器 ---")
    
    browser_config = BrowserConfig(headless=True)
    
    # 只提取具有特定 CSS 类的元素
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        css_selector=".wide-tease-item__description"  # CSS 选择器
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=crawler_config
        )
        print("CSS 选择器提取结果（前500字符）：")
        print(result.markdown[:500])


# 媒体处理示例
async def media_handling():
    """处理页面中的媒体内容（图片等）"""
    print("\n--- 媒体处理 ---")
    
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # 绕过缓存
        exclude_external_images=True,  # 排除外部图片
        screenshot=True  # 启用截图功能
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=crawler_config
        )
        
        print("页面图片信息（前5张）:")
        for img in result.media["images"][:5]:
            print(f"图片 URL: {img['src']}")
            print(f"替代文本: {img['alt']}")
            print(f"相关性评分: {img['score']}")
            print("-" * 40)


# 自定义钩子示例
async def custom_hook_workflow(verbose=True):
    """演示如何使用钩子函数自定义爬虫行为"""
    print("\n--- 自定义钩子工作流 ---")
    
    async with AsyncWebCrawler() as crawler:
        # 设置 'before_goto' 钩子：在导航前执行自定义代码
        crawler.crawler_strategy.set_hook(
            "before_goto",
            lambda page, context: print("[钩子] 准备导航到页面..."),
        )

        # 执行爬取操作
        result = await crawler.arun(url="https://crawl4ai.com")
        
        print("爬取结果（前500字符，换行符替换为' -- '）：")
        print(result.markdown.raw_markdown[:500].replace("\n", " -- "))


# 代理使用示例
async def use_proxy():
    """演示如何使用代理服务器"""
    print("\n--- 使用代理服务器 ---")
    
    browser_config = BrowserConfig(
        headless=True,
        proxy_config={
            "server": "http://proxy.example.com:8080",  # 代理服务器地址
            "username": "username",  # 用户名
            "password": "password",  # 密码
        },
    )
    crawler_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=crawler_config
        )
        if result.success:
            print("使用代理爬取成功，结果（前500字符）：")
            print(result.markdown[:500])


# 截图保存示例
async def capture_and_save_screenshot(url: str, output_path: str):
    """爬取网页并保存截图"""
    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # 绕过缓存
        screenshot=True  # 启用截图
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)

        if result.success and result.screenshot:
            import base64

            # 解码 base64 截图数据
            screenshot_data = base64.b64decode(result.screenshot)
            
            # 保存到文件
            with open(output_path, "wb") as f:
                f.write(screenshot_data)
            print(f"截图成功保存到 {output_path}")
        else:
            print("截图失败")


# 主函数：运行所有示例
async def main():
    """主函数：按顺序运行所有示例"""
    
    print("开始运行 Crawl4AI 快速入门示例...")
    
    # 1. 基础爬取
    await simple_crawl()
    
    # 2. 内容清理
    await clean_content()
    
    # 3. 链接分析
    await link_analysis()
    
    # 4. JavaScript 执行
    await simple_example_with_running_js_code()
    
    # 5. CSS 选择器
    await simple_example_with_css_selector()
    
    # 6. 媒体处理
    await media_handling()
    
    # 7. 自定义钩子
    await custom_hook_workflow()
    
    print("\n所有示例运行完成！")


if __name__ == "__main__":
    asyncio.run(main())