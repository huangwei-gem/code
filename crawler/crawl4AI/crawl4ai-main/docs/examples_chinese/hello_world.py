"""
Crawl4AI 基础示例 - Hello World
这是最简单的 Crawl4AI 使用示例，展示了如何爬取一个网页并提取内容。
"""

import asyncio
from crawl4ai import (
    AsyncWebCrawler,      # 异步网络爬虫类
    BrowserConfig,        # 浏览器配置
    CrawlerRunConfig,     # 爬虫运行配置
    DefaultMarkdownGenerator,  # 默认 Markdown 生成器
    PruningContentFilter,      # 内容过滤策略
    CrawlResult            # 爬取结果类
)


async def main():
    """主函数：演示基础爬虫使用"""
    
    # 配置浏览器参数
    browser_config = BrowserConfig(
        headless=False,    # 设置为 False 可以看到浏览器界面（便于调试）
        verbose=True,       # 显示详细日志信息
    )
    
    # 使用异步上下文管理器创建爬虫实例
    async with AsyncWebCrawler(config=browser_config) as crawler:
        
        # 配置爬虫运行参数
        crawler_config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter()  # 使用内容过滤器
            ),
        )
        
        # 执行爬取任务
        result: CrawlResult = await crawler.arun(
            url="https://www.helloworld.org",  # 目标网址
            config=crawler_config
        )
        
        # 打印爬取结果的前500个字符
        print("爬取结果（前500字符）：")
        print("-" * 50)
        print(result.markdown.raw_markdown[:500])
        print("-" * 50)
        
        # 显示爬取状态
        print(f"爬取成功: {result.success}")
        print(f"响应状态码: {result.status_code}")
        print(f"页面标题: {result.metadata.get('title', '无标题')}")


if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())