import asyncio
import time

from crawl4ai import CrawlerRunConfig, AsyncWebCrawler, CacheMode
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
    ContentTypeFilter,
    ContentRelevanceFilter,
    SEOFilter,
)
from crawl4ai.deep_crawling.scorers import (
    KeywordRelevanceScorer,
)


# 1️⃣ 基础深度爬取设置
async def basic_deep_crawl():
    """
    第一部分：基础深度爬取设置 - 演示简单的两级深度爬取。

    本函数展示：
    - 如何设置BFSDeepCrawlStrategy（广度优先搜索）
    - 设置深度和域名参数
    - 处理结果以显示层次结构
    """
    print("\n===== 基础深度爬取设置 =====")

    # 配置使用广度优先搜索策略的2级深度爬取
    # max_depth=2 表示：初始页面（深度0）+ 2个更多层级
    # include_external=False 表示：只跟随同一域名内的链接
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,  # 爬取期间显示进度
    )

    async with AsyncWebCrawler() as crawler:
        start_time = time.perf_counter()
        results = await crawler.arun(url="https://docs.crawl4ai.com", config=config)

        # 按深度分组结果以可视化爬取树
        pages_by_depth = {}
        for result in results:
            depth = result.metadata.get("depth", 0)
            if depth not in pages_by_depth:
                pages_by_depth[depth] = []
            pages_by_depth[depth].append(result.url)

        print(f"✅ 总共爬取了 {len(results)} 个页面")

        # 按深度显示爬取结构
        for depth, urls in sorted(pages_by_depth.items()):
            print(f"\n深度 {depth}: {len(urls)} 个页面")
            # 显示每个深度的前3个URL作为示例
            for url in urls[:3]:
                print(f"  → {url}")
            if len(urls) > 3:
                print(f"  ... 还有 {len(urls) - 3} 个")

        print(
            f"\n✅ 性能：{len(results)} 个页面用了 {time.perf_counter() - start_time:.2f} 秒"
        )

# 2️⃣ 流式与非流式执行
async def stream_vs_nonstream():
    """
    第二部分：演示流式与非流式执行的区别。

    非流式：等待所有结果后再处理
    流式：结果可用时立即处理
    """
    print("\n===== 流式与非流式执行 =====")

    # 两个示例的通用配置
    base_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=False,
    )

    async with AsyncWebCrawler() as crawler:
        # 非流式模式
        print("\n📊 非流式模式：")
        print("  在此模式下，所有结果在返回前都会被收集。")

        non_stream_config = base_config.clone()
        non_stream_config.stream = False

        start_time = time.perf_counter()
        results = await crawler.arun(
            url="https://docs.crawl4ai.com", config=non_stream_config
        )

        print(f"  ✅ 一次性收到所有 {len(results)} 个结果")
        print(f"  ✅ 总耗时：{time.perf_counter() - start_time:.2f} 秒")

        # 流式模式
        print("\n📊 流式模式：")
        print("  在此模式下，结果可用时立即处理。")

        stream_config = base_config.clone()
        stream_config.stream = True

        start_time = time.perf_counter()
        result_count = 0
        first_result_time = None

        async for result in await crawler.arun(
            url="https://docs.crawl4ai.com", config=stream_config
        ):
            result_count += 1
            if result_count == 1:
                first_result_time = time.perf_counter() - start_time
                print(
                    f"  ✅ 第一个结果在 {first_result_time:.2f} 秒后收到: {result.url}"
                )
            elif result_count % 5 == 0:  # 为了简洁，每5个结果显示一次
                print(f"  → 结果 #{result_count}: {result.url}")

        print(f"  ✅ 总计: {result_count} 个结果")
        print(f"  ✅ 第一个结果: {first_result_time:.2f} 秒")
        print(f"  ✅ 所有结果: {time.perf_counter() - start_time:.2f} 秒")
        print("\n🔍 关键要点：流式允许立即处理结果")

# 3️⃣ 引入过滤器和评分器
async def filters_and_scorers():
    """
    第三部分：演示过滤器和评分器的使用，实现更有针对性的爬取。

    本函数逐步添加：
    1. 单个URL模式过滤器
    2. 链中的多个过滤器
    3. 用于页面优先级的评分器
    """
    print("\n===== 过滤器和评分器 =====")

    async with AsyncWebCrawler() as crawler:
        # 单个过滤器示例
        print("\n📊 示例1：单个URL模式过滤器")
        print("  只爬取URL中包含'core'的页面")

        # 创建只允许URL中包含'guide'的过滤器
        url_filter = URLPatternFilter(patterns=["*core*"])

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1,
                include_external=False,
                filter_chain=FilterChain([url_filter]),  # 单个过滤器
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            cache_mode=CacheMode.BYPASS,
            verbose=True,
        )

        results = await crawler.arun(url="https://docs.crawl4ai.com", config=config)

        print(f"  ✅ 爬取了 {len(results)} 个匹配'*core*'的页面")
        for result in results[:3]:  # 显示前3个结果
            print(f"  → {result.url}")
        if len(results) > 3:
            print(f"  ... 还有 {len(results) - 3} 个")

        # 多个过滤器示例
        print("\n📊 示例2：链中的多个过滤器")
        print("  只爬取满足以下条件的页面：")
        print("  1. URL中包含'2024'")
        print("  2. 来自'techcrunch.com'")
        print("  3. 是text/html或application/javascript内容类型")

        # 创建过滤器链
        filter_chain = FilterChain(
            [
                URLPatternFilter(patterns=["*2024*"]),
                DomainFilter(
                    allowed_domains=["techcrunch.com"],
                    blocked_domains=["guce.techcrunch.com", "oidc.techcrunch.com"],
                ),
                ContentTypeFilter(
                    allowed_types=["text/html", "application/javascript"]
                ),
            ]
        )

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1, include_external=False, filter_chain=filter_chain
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
        )

        results = await crawler.arun(url="https://techcrunch.com", config=config)

        print(f"  ✅ 应用所有过滤器后爬取了 {len(results)} 个页面")
        for result in results[:3]:
            print(f"  → {result.url}")