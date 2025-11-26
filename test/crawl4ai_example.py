#!/usr/bin/env python3
"""
Crawl4AI 使用示例
展示如何使用 crawl4ai 进行网页爬取
"""

import asyncio
from crawl4ai import AsyncWebCrawler

async def simple_crawl_example():
    """简单的网页爬取示例"""
    
    # 创建爬虫实例
    async with AsyncWebCrawler() as crawler:
        # 爬取一个网页
        url = "https://blog.csdn.net/weixin_41477468/article/details/137524530"
        print(f"正在爬取: {url}")
        
        try:
            result = await crawler.arun(
                url=url,
                bypass_cache=True  # 绕过缓存
            )
            
            if result.success:
                print("✅ 爬取成功!")
                print(f"页面URL: {result.url}")
                print(f"HTML长度: {len(result.html)} 字符")
                if result.markdown:
                    print(f"Markdown长度: {len(str(result.markdown))} 字符")
                else:
                    print("Markdown: 无")
                
                # 保存结果到文件
                with open("example_result.md", "w", encoding="utf-8") as f:
                    f.write(f"# 爬取结果\n\n")
                    f.write(f"URL: {url}\n\n")
                    if result.markdown:
                        f.write(str(result.markdown))
                
                print("结果已保存到 example_result.md")
            else:
                print(f"❌ 爬取失败: {result.error_message}")
                
        except Exception as e:
            print(f"❌ 发生错误: {e}")

async def advanced_crawl_example():
    """高级爬取示例 - 使用配置选项"""
    
    async with AsyncWebCrawler() as crawler:
        url = "https://blog.csdn.net/weixin_41477468/article/details/137524530"
        print(f"正在爬取: {url}")
        
        try:
            result = await crawler.arun(
                url=url,
                bypass_cache=True,
                # 移除图片以减少数据量
                exclude_external_images=True,
                # 设置用户代理
                user_agent="Mozilla/5.0 (compatible; Crawl4AI/1.0)",
                # 设置超时
                timeout=30000,  # 30秒
                # 提取主要内容
                word_count_threshold=10,  # 最少字数阈值
            )
            
            if result.success:
                print("✅ 高级爬取成功!")
                print(f"页面URL: {result.url}")
                if result.markdown:
                    print(f"Markdown长度: {len(str(result.markdown))} 字符")
                else:
                    print("Markdown: 无")
                print(f"提取的链接数量: {len(result.links) if result.links else 0}")
                
                # 保存结果
                with open("python_org_result.md", "w", encoding="utf-8") as f:
                    f.write(f"# 高级爬取结果\n\n")
                    f.write(f"URL: {url}\n\n")
                    if result.markdown:
                        f.write(str(result.markdown))
                
                print("结果已保存到 python_org_result.md")
            else:
                print(f"❌ 爬取失败: {result.error_message}")
                
        except Exception as e:
            print(f"❌ 发生错误: {e}")

async def batch_crawl_example():
    """批量爬取示例"""
    
    urls = [
        "https://example.com",
        "https://httpbin.org/html",
        "https://httpbin.org/json"
    ]
    
    async with AsyncWebCrawler() as crawler:
        print(f"批量爬取 {len(urls)} 个网页...")
        
        tasks = []
        for url in urls:
            task = crawler.arun(
                url=url,
                bypass_cache=True,
                timeout=15000  # 15秒超时
            )
            tasks.append(task)
        
        # 并发执行所有任务
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        successful_count = 0
        for i, result in enumerate(results):
            url = urls[i]
            if isinstance(result, Exception):
                print(f"❌ {url} - 错误: {result}")
            elif result.success:
                successful_count += 1
                if result.markdown:
                    print(f"✅ {url} - 成功 (长度: {len(str(result.markdown))} 字符)")
                else:
                    print(f"✅ {url} - 成功 (无Markdown内容)")
            else:
                print(f"❌ {url} - 失败: {result.error_message}")
        
        print(f"\n批量爬取完成: {successful_count}/{len(urls)} 成功")

async def main():
    """主函数 - 运行所有示例"""
    
    print("🕷️  Crawl4AI 使用示例")
    print("=" * 50)
    
    # 示例 1: 简单爬取
    print("\n📋 示例 1: 简单爬取")
    print("-" * 30)
    await simple_crawl_example()
    
    # 示例 2: 高级爬取
    print("\n📋 示例 2: 高级爬取")
    print("-" * 30)
    await advanced_crawl_example()
    
    # # 示例 3: 批量爬取
    # print("\n📋 示例 3: 批量爬取")
    # print("-" * 30)
    # await batch_crawl_example()
    
    print("\n✅ 所有示例完成!")

if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())