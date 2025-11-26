"""
浏览器优化示例
演示 Crawl4AI 中最佳的浏览器使用模式：
1. 会话重用的顺序爬取
2. 浏览器实例重用的并行爬取  
3. 性能优化设置
"""

import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def crawl_sequential(urls: List[str]):
    """
    使用会话重用的顺序爬取 - 适合中等工作负载
    
    这种方法最高效，因为它：
    - 重用同一个浏览器实例
    - 在同一个标签页中顺序访问页面
    - 减少了浏览器启动和关闭的开销
    """
    print("\n=== 顺序爬取（会话重用） ===")

    # 配置浏览器优化设置
    browser_config = BrowserConfig(
        headless=True,  # 无头模式，提高性能
        browser_args=[
            "--disable-gpu",  # 禁用 GPU 加速
            "--disable-dev-shm-usage",  # 禁用 /dev/shm 使用
            "--no-sandbox",  # Docker 环境必需
        ],
        viewport={
            "width": 800,
            "height": 600,
        },  # 较小的视口以提高性能
    )

    # 配置爬取设置
    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            # content_filter=PruningContentFilter(),  # 如需使用内容过滤
        ),
    )

    # 创建单个爬虫实例
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        session_id = "session1"  # 所有 URL 使用相同的会话
        for url in urls:
            result = await crawler.arun(
                url=url,
                config=crawl_config,
                session_id=session_id,  # 重用同一个浏览器标签页
            )
            if result.success:
                print(f"成功爬取 {url}")
                print(f"内容长度: {len(result.markdown.raw_markdown)}")
                print(f"页面标题: {result.metadata.get('title', '无标题')}")
                print("-" * 40)
    finally:
        await crawler.close()


async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    """
    浏览器实例重用的并行爬取 - 适合大型工作负载
    
    这种方法最佳，因为它：
    - 重用同一个浏览器实例
    - 通过多个标签页并行处理
    - 控制并发数量避免资源耗尽
    """
    print("\n=== 并行爬取（浏览器重用） ===")

    browser_config = BrowserConfig(
        headless=True,
        browser_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
        viewport={"width": 800, "height": 600},
    )

    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            # content_filter=PruningContentFilter(),  # 如需使用内容过滤
        ),
    )

    # 为所有并行任务创建单个爬虫实例
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        # 分批创建任务以控制并发数
        for i in range(0, len(urls), max_concurrent):
            batch = urls[i : i + max_concurrent]
            tasks = []

            for j, url in enumerate(batch):
                session_id = f"parallel_session_{j}"  # 每个并发任务使用不同的会话
                task = crawler.arun(url=url, config=crawl_config, session_id=session_id)
                tasks.append(task)

            # 等待批次完成
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # 处理结果
            for url, result in zip(batch, results):
                if isinstance(result, Exception):
                    print(f"爬取 {url} 时出错: {str(result)}")
                elif result.success:
                    print(f"成功爬取 {url}")
                    print(f"内容长度: {len(result.markdown.raw_markdown)}")
                    print("-" * 40)
    finally:
        await crawler.close()


async def crawl_with_performance_monitoring(urls: List[str]):
    """
    带性能监控的爬取
    演示如何监控和优化爬取性能
    """
    print("\n=== 性能监控爬取 ===")
    
    import time
    
    start_time = time.time()
    
    browser_config = BrowserConfig(
        headless=True,
        browser_args=[
            "--disable-gpu",
            "--disable-dev-shm-usage", 
            "--no-sandbox",
            "--disable-images",  # 禁用图片加载提高速度
            "--disable-javascript"  # 禁用 JavaScript（如果不需要）
        ],
        viewport={"width": 800, "height": 600},
    )

    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,  # 启用缓存
        timeout=30,  # 设置超时时间
        markdown_generator=DefaultMarkdownGenerator(),
    )

    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        success_count = 0
        total_content_length = 0
        
        for i, url in enumerate(urls):
            page_start = time.time()
            
            result = await crawler.arun(
                url=url,
                config=crawl_config,
                session_id=f"perf_session_{i}",
            )
            
            page_time = time.time() - page_start
            
            if result.success:
                success_count += 1
                content_length = len(result.markdown.raw_markdown)
                total_content_length += content_length
                
                print(f"✓ {url}")
                print(f"  耗时: {page_time:.2f}秒")
                print(f"  内容长度: {content_length}")
            else:
                print(f"✗ {url} - 失败")
                
            print("-" * 40)
        
        total_time = time.time() - start_time
        
        print(f"\n性能统计:")
        print(f"总耗时: {total_time:.2f}秒")
        print(f"成功爬取: {success_count}/{len(urls)}")
        print(f"总内容长度: {total_content_length}")
        print(f"平均每个页面: {total_time/len(urls):.2f}秒")
        
    finally:
        await crawler.close()


async def main():
    """主函数：演示不同的优化爬取方法"""
    
    # 示例 URL 列表
    urls = [
        "https://example.com/page1",
        "https://example.com/page2", 
        "https://example.com/page3",
        "https://example.com/page4",
    ]

    print("开始浏览器优化爬取演示...")
    
    # 1. 演示顺序爬取
    await crawl_sequential(urls)

    # 2. 演示并行爬取
    await crawl_parallel(urls, max_concurrent=2)
    
    # 3. 演示性能监控爬取
    await crawl_with_performance_monitoring(urls)


if __name__ == "__main__":
    asyncio.run(main())