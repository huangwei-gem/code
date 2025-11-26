"""
示例：演示不同的提取策略和各种输入格式

本示例展示如何：
1. 使用不同的输入格式（markdown、HTML、fit_markdown）
2. 使用基于JSON的提取器（CSS和XPath）
3. 使用不同输入格式的LLM提取
4. 正确配置浏览器和爬虫设置
"""

import asyncio
import os

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai import LLMConfig
from crawl4ai import (
    LLMExtractionStrategy,
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy,
)
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def run_extraction(crawler: AsyncWebCrawler, url: str, strategy, name: str):
    """辅助函数：使用正确配置运行提取"""
    try:
        # 配置爬虫运行设置
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            extraction_strategy=strategy,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter()  # 支持fit_markdown
            ),
        )

        # 运行爬虫
        result = await crawler.arun(url=url, config=config)

        if result.success:
            print(f"\n=== {name} 结果 ===")
            print(f"提取内容: {result.extracted_content}")
            print(f"原始Markdown长度: {len(result.markdown.raw_markdown)}")
            print(
                f"引用Markdown长度: {len(result.markdown.markdown_with_citations)}"
            )
        else:
            print(f"{name}错误: 爬取失败")

    except Exception as e:
        print(f"{name}错误: {str(e)}")


async def main():
    # 示例URL（替换为实际URL）
    url = "https://example.com/product-page"

    # 配置浏览器设置
    browser_config = BrowserConfig(headless=True, verbose=True)

    # 初始化提取策略

    # 1. 不同输入格式的LLM提取
    markdown_strategy = LLMExtractionStrategy(
        llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY")),
        instruction="提取产品信息，包括名称、价格和描述",
    )

    html_strategy = LLMExtractionStrategy(
        input_format="html",
        llm_config=LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY")),
        instruction="从HTML中提取产品信息，包括结构化数据",
    )

    fit_markdown_strategy = LLMExtractionStrategy(
        input_format="fit_markdown",
        llm_config=LLMConfig(provider="openai/gpt-4o-mini",api_token=os.getenv("OPENAI_API_KEY")),
        instruction="从清理后的markdown中提取产品信息",
    )

    # 2. 基于JSON的CSS提取（自动使用HTML输入）
    css_schema = {
        "baseSelector": ".product",
        "fields": [
            {"name": "title", "selector": "h1.product-title", "type": "text"},
            {"name": "price", "selector": ".price", "type": "text"},
            {"name": "description", "selector": ".description", "type": "text"},
        ],
    }
    css_strategy = JsonCssExtractionStrategy(schema=css_schema)

    # 3. 基于JSON的XPath提取（自动使用HTML输入）
    xpath_schema = {
        "baseSelector": "//div[@class='product']",
        "fields": [
            {
                "name": "title",
                "selector": ".//h1[@class='product-title']/text()",
                "type": "text",
            },
            {
                "name": "price",
                "selector": ".//span[@class='price']/text()",
                "type": "text",
            },
            {
                "name": "description",
                "selector": ".//div[@class='description']/text()",
                "type": "text",
            },
        ],
    }
    xpath_strategy = JsonXPathExtractionStrategy(schema=xpath_schema)

    # 使用上下文管理器进行正确的资源处理
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 运行所有策略
        await run_extraction(crawler, url, markdown_strategy, "Markdown LLM")
        await run_extraction(crawler, url, html_strategy, "HTML LLM")
        await run_extraction(crawler, url, fit_markdown_strategy, "Fit Markdown LLM")
        await run_extraction(crawler, url, css_strategy, "CSS提取")
        await run_extraction(crawler, url, xpath_strategy, "XPath提取")


if __name__ == "__main__":
    asyncio.run(main())