import asyncio
from crawl4ai import AsyncWebCrawler


# 基本爬虫，只要一个url
async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.example.com")
        print(f"Success: {result.success}")
        print(f"URL: {result.url}")
        print(f"Markdown: {result.markdown[:500]}...")  # 打印前500个字符

if __name__ == "__main__":
    asyncio.run(main())



# 截图功能
import base64

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business", screenshot=True)
        with open("screenshot.png", "wb") as f:
            f.write(base64.b64decode(result.screenshot))
        print("截图已保存为 'screenshot.png'!")

asyncio.run(main())



# 默认缓存效果，第二次会比第一次快

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # 第一次爬取（缓存结果）
        result1 = await crawler.arun(url="https://www.nbcnews.com/business")
        print(f"第一次爬取结果: {result1.markdown[:100]}...")

        # 强制再次爬取
        result2 = await crawler.arun(url="https://www.nbcnews.com/business", bypass_cache=True)
        print(f"第二次爬取结果: {result2.markdown[:100]}...")

asyncio.run(main())

# 作用：根据正则表达式模式对提取的文本进行分块。
# 参数 patterns：
# 类型：List[str]
# 示例：
# ["\n\n"]：按段落（空行）分割；
# [r"\.\s+"]：按句子结尾（句号+空格）分割；
# [r"(?<=\.)\s+(?=[A-Z])"]：更智能的句子分割（需注意性能与准确性）。
# ⚠️ 注意：patterns 中的字符串会被编译为 re.split() 使用的正则表达式，不保留分隔符。

from crawl4ai.chunking_strategy import RegexChunking

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            chunking_strategy=RegexChunking(patterns=["\n\n"])
        )
        print(f"RegexChunking结果: {result.extracted_content[:200]}...")

asyncio.run(main())



