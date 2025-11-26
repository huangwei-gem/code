"""
钩子函数示例
演示 Crawl4AI 中不同类型的钩子函数使用方法
"""

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from playwright.async_api import Page, BrowserContext


async def main():
    print("🔗 钩子示例：演示不同钩子的使用场景")

    # 配置浏览器设置
    browser_config = BrowserConfig(headless=True)

    # 配置爬虫设置
    crawler_run_config = CrawlerRunConfig(
        js_code="window.scrollTo(0, document.body.scrollHeight);",  # 滚动到页面底部
        wait_for="body",  # 等待 body 元素加载
        cache_mode=CacheMode.BYPASS,  # 绕过缓存
    )

    # 创建爬虫实例
    crawler = AsyncWebCrawler(config=browser_config)

    # 定义和设置钩子函数
    async def on_browser_created(browser, context: BrowserContext, **kwargs):
        """浏览器创建后调用的钩子"""
        print("[钩子] on_browser_created - 浏览器准备就绪！")
        # 示例：为所有请求设置 cookie
        return browser

    async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
        """新页面和上下文创建后调用的钩子"""
        print("[钩子] on_page_context_created - 新页面已创建！")
        # 示例：设置默认视口大小
        await context.add_cookies(
            [
                {
                    "name": "session_id",
                    "value": "example_session",
                    "domain": ".example.com",
                    "path": "/",
                }
            ]
        )
        await page.set_viewport_size({"width": 1080, "height": 800})
        return page

    async def on_user_agent_updated(
        page: Page, context: BrowserContext, user_agent: str, **kwargs
    ):
        """用户代理更新时调用的钩子"""
        print(f"[钩子] on_user_agent_updated - 新用户代理: {user_agent}")
        return page

    async def on_execution_started(page: Page, context: BrowserContext, **kwargs):
        """自定义 JavaScript 执行后调用的钩子"""
        print("[钩子] on_execution_started - 自定义 JavaScript 已执行！")
        return page

    async def before_goto(page: Page, context: BrowserContext, url: str, **kwargs):
        """导航到每个 URL 之前调用的钩子"""
        print(f"[钩子] before_goto - 即将访问: {url}")
        # 示例：为请求添加自定义头部
        await page.set_extra_http_headers({"Custom-Header": "my-value"})
        return page

    async def after_goto(
        page: Page, context: BrowserContext, url: str, response: dict, **kwargs
    ):
        """导航到每个 URL 之后调用的钩子"""
        print(f"[钩子] after_goto - 成功加载: {url}")
        # 示例：等待特定元素加载
        try:
            await page.wait_for_selector(".content", timeout=1000)
            print("内容元素已找到！")
        except:
            print("内容元素未找到，继续执行")
        return page

    async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs):
        """获取 HTML 内容之前调用的钩子"""
        print("[钩子] before_retrieve_html - 即将获取 HTML 内容")
        # 示例：滚动到底部触发延迟加载
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        return page

    async def before_return_html(
        page: Page, context: BrowserContext, html: str, **kwargs
    ):
        """返回 HTML 内容之前调用的钩子"""
        print(f"[钩子] before_return_html - 获取到 HTML 内容 (长度: {len(html)})")
        # 示例：可以在此处修改 HTML 内容
        return page

    # 设置所有钩子
    crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created)
    crawler.crawler_strategy.set_hook(
        "on_page_context_created", on_page_context_created
    )
    crawler.crawler_strategy.set_hook("on_user_agent_updated", on_user_agent_updated)
    crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started)
    crawler.crawler_strategy.set_hook("before_goto", before_goto)
    crawler.crawler_strategy.set_hook("after_goto", after_goto)
    crawler.crawler_strategy.set_hook("before_retrieve_html", before_retrieve_html)
    crawler.crawler_strategy.set_hook("before_return_html", before_return_html)

    await crawler.start()

    # 示例：爬取简单网站
    url = "https://example.com"
    result = await crawler.arun(url, config=crawler_run_config)
    print(f"\n爬取 URL: {result.url}")
    print(f"HTML 长度: {len(result.html)}")
    print(f"爬取成功: {result.success}")

    await crawler.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())