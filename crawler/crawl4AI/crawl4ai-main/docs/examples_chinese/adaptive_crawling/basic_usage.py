"""
自适应爬虫基础示例

本示例演示了自适应爬虫的最简单用例：
查找特定主题的信息并知道何时停止爬取。
"""

import asyncio
from crawl4ai import AsyncWebCrawler, AdaptiveCrawler


async def main():
    """自适应爬虫基础示例"""
    
    # 初始化爬虫
    async with AsyncWebCrawler(verbose=True) as crawler:
        
        # 创建自适应爬虫（默认使用统计策略）
        adaptive = AdaptiveCrawler(crawler)
        
        # 注意：你也可以使用嵌入策略进行语义理解：
        # from crawl4ai import AdaptiveConfig
        # config = AdaptiveConfig(strategy="embedding")
        # adaptive = AdaptiveCrawler(crawler, config)
        
        # 开始自适应爬取
        print("开始自适应爬取 Python 异步编程相关信息...")
        result = await adaptive.digest(
            start_url="https://docs.python.org/3/library/asyncio.html",
            query="async await context managers coroutines"
        )
        
        # 显示爬取统计信息
        print("\n" + "="*50)
        print("爬取统计信息")
        print("="*50)
        adaptive.print_stats(detailed=False)
        
        # 获取最相关的内容
        print("\n" + "="*50)
        print("最相关的页面")
        print("="*50)
        
        relevant_pages = adaptive.get_relevant_content(top_k=5)
        for i, page in enumerate(relevant_pages, 1):
            print(f"\n{i}. {page['url']}")
            print(f"   相关性评分: {page['score']:.2%}")
            
            # 显示内容片段
            content = page['content'] or ""
            if content:
                snippet = content[:200].replace('\n', ' ')
                if len(content) > 200:
                    snippet += "..."
                print(f"   预览: {snippet}")
        
        # 显示最终置信度
        print(f"\n{'='*50}")
        print(f"最终置信度: {adaptive.confidence:.2%}")
        print(f"爬取页面总数: {len(result.crawled_urls)}")
        print(f"知识库大小: {len(adaptive.state.knowledge_base)} 个文档")
        
        # 示例：检查是否可以回答特定问题
        print(f"\n{'='*50}")
        print("信息充分性检查")
        print(f"{'='*50}")
        
        if adaptive.confidence >= 0.8:
            print("✓ 高置信度 - 可以回答关于 Python 异步编程的详细问题")
        elif adaptive.confidence >= 0.6:
            print("~ 中等置信度 - 可以回答基本问题") 
        else:
            print("✗ 低置信度 - 需要更多信息")


if __name__ == "__main__":
    asyncio.run(main())