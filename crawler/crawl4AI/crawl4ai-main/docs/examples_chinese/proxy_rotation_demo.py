import os
import re
from typing import List, Dict
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
    RoundRobinProxyStrategy
)

def load_proxies_from_env() -> List[Dict]:
    """从PROXIES环境变量加载代理"""
    proxies = []
    try:
        proxy_list = os.getenv("PROXIES", "").split(",")
        for proxy in proxy_list:
            if not proxy:
                continue
            ip, port, username, password = proxy.split(":")
            proxies.append({
                "server": f"http://{ip}:{port}",
                "username": username,
                "password": password,
                "ip": ip  # 存储原始IP用于验证
            })
    except Exception as e:
        print(f"从环境加载代理时出错: {e}")
    return proxies

async def demo_proxy_rotation():
    """
    使用RoundRobinProxyStrategy的代理轮换演示
    ===============================================
    演示使用策略模式的代理轮换。
    """
    print("\n=== 代理轮换演示（轮询） ===")
    
    # 加载代理并创建轮换策略
    proxies = load_proxies_from_env()
    if not proxies:
        print("环境中未找到代理。设置PROXIES环境变量！")
        return
        
    proxy_strategy = RoundRobinProxyStrategy(proxies)
    
    # 创建配置
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        proxy_rotation_strategy=proxy_strategy
    )
    
    # 测试URL
    urls = ["https://httpbin.org/ip"] * len(proxies)  # 每个代理测试一次
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        for url in urls:
            result = await crawler.arun(url=url, config=run_config)
            
            if result.success:
                # 从响应中提取IP
                ip_match = re.search(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', result.html)
                current_proxy = run_config.proxy_config if run_config.proxy_config else None
                
                if current_proxy:
                    print(f"代理 {current_proxy['server']} -> 响应IP: {ip_match.group(0) if ip_match else '未找到'}")
                    verified = ip_match and ip_match.group(0) == current_proxy['ip']
                    if verified:
                        print(f"✅ 代理工作正常！IP匹配: {current_proxy['ip']}")
                    else:
                        print("❌ 代理失败或IP不匹配！")
            else:
                print(f"请求失败: {result.error_message}")

async def demo_proxy_rotation_batch():
    """
    批量处理代理轮换演示
    =======================================
    演示使用arun_many和内存调度器的代理轮换。
    """
    print("\n=== 批量代理轮换演示 ===")
    
    try:
        # 加载代理并创建轮换策略
        proxies = load_proxies_from_env()
        if not proxies:
            print("环境中未找到代理。设置PROXIES环境变量！")
            return
            
        proxy_strategy = RoundRobinProxyStrategy(proxies)
        
        # 配置
        browser_config = BrowserConfig(headless=True, verbose=False)
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            proxy_rotation_strategy=proxy_strategy,
            markdown_generator=DefaultMarkdownGenerator()
        )

        # 测试URL - 多个请求以测试轮换
        urls = ["https://httpbin.org/ip"] * (len(proxies) * 2)  # 每个代理测试两次

        print("\n📈 使用代理轮换初始化爬虫...")
        async with AsyncWebCrawler(config=browser_config) as crawler:
            monitor = CrawlerMonitor(
                max_visible_rows=10,
                display_mode=DisplayMode.DETAILED
            )
            
            dispatcher = MemoryAdaptiveDispatcher(
                memory_threshold_percent=80.0,
                check_interval=0.5,
                max_session_permit=1, #len(proxies),  # 并发会话数与代理数匹配
                # monitor=monitor
            )
            
            print("\n🚀 开始使用代理轮换进行批量爬取...")
            results = await crawler.arun_many(
                urls=urls,
                config=run_config,
                dispatcher=dispatcher
            )

            # 验证结果
            success_count = 0
            for result in results:
                if result.success:
                    ip_match = re.search(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', result.html)
                    current_proxy = run_config.proxy_config if run_config.proxy_config else None
                    
                    if current_proxy and ip_match:
                        print(f"URL {result.url}")
                        print(f"代理 {current_proxy['server']} -> 响应IP: {ip_match.group(0)}")
                        verified = ip_match.group(0) == current_proxy['ip']
                        if verified:
                            print(f"✅ 代理工作正常！IP匹配: {current_proxy['ip']}")
                            success_count += 1
                        else:
                            print("❌ 代理失败或IP不匹配！")
                    print("---")
                    
            print(f"\n✅ 完成了{len(results)}个请求，其中{success_count}个代理验证成功")
            
    except Exception as e:
        print(f"\n❌ 批量代理轮换演示出错: {str(e)}")

if __name__ == "__main__":
    import asyncio
    from crawl4ai import (
        CrawlerMonitor, 
        DisplayMode,
        MemoryAdaptiveDispatcher,
        DefaultMarkdownGenerator
    )
    
    async def run_demos():
        # await demo_proxy_rotation()  # 原始单请求演示
        await demo_proxy_rotation_batch()  # 新的批处理演示
        
    asyncio.run(run_demos())