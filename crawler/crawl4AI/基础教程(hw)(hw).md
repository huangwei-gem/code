# Crawl4AI 基础设置和认识





github 地址：https://github.com/unclecode/crawl4ai



## Crawl4AI 入门指南

本快速入门指南介绍了 Crawl4AI，涵盖了基本用法、先进功能（例如分块和提取策略）以及异步编程。用户将学习如何实现各种爬虫技术，包括截图、JSON 提取和动态内容爬取。

## 1. 什么是 Crawl4AI？

Crawl4AI 是一个强大的异步网络爬虫库，旨在简化信息收集过程。它允许开发者快速、有效地从网站上提取数据，并支持多种提取策略和动态内容的处理。通过使用异步编程，Crawl4AI 能够在进行爬取时提高效率，使其在处理大量请求时表现更佳。

## 2. 安装和环境准备

使用 Crawl4AI 之前，用户需要确保安装了必要的 Python 环境和依赖项。可以通过以下命令安装 Crawl4AI：

```
pip install crawl4ai
```

## 3. 基本用法

### 3.1 导入模块和创建爬虫实例

用户首先需要导入必要的模块并创建 `AsyncWebCrawler` 的实例。使用异步上下文管理器可以自动处理爬虫的启动和关闭。

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # 在这里添加爬虫代码
        pass

if __name__ == "__main__":
    asyncio.run(main())
```

### 3.2 简单的爬虫操作

用户只需提供一个 URL，Crawl4AI 就会执行其魔法！

```python
async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business")
        print(f"基本爬取结果: {result.markdown[:500]}")  # 打印前500个字符

if __name__ == "__main__":
    asyncio.run(main())
```

## 4. 截图功能 📸

用户还可以使用 Crawl4AI 进行网页截图。

```
import base64

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business", screenshot=True)
        with open("screenshot.png", "wb") as f:
            f.write(base64.b64decode(result.screenshot))
        print("截图已保存为 'screenshot.png'!")

asyncio.run(main())
```

## 5. 理解参数 🧠

Crawl4AI 默认会缓存爬取结果，这意味着对同一 URL 的后续爬取会更快。以下是实现这一功能的示例。

```
async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # 第一次爬取（缓存结果）
        result1 = await crawler.arun(url="https://www.nbcnews.com/business")
        print(f"第一次爬取结果: {result1.markdown[:100]}...")

        # 强制再次爬取
        result2 = await crawler.arun(url="https://www.nbcnews.com/business", bypass_cache=True)
        print(f"第二次爬取结果: {result2.markdown[:100]}...")

asyncio.run(main())
```

## 6. 添加分块策略 🧩

用户可以添加分块策略，例如 `RegexChunking`，此策略基于给定的正则表达式模式分割文本。

```
from crawl4ai.chunking_strategy import RegexChunking

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            chunking_strategy=RegexChunking(patterns=["\n\n"])
        )
        print(f"RegexChunking结果: {result.extracted_content[:200]}...")

asyncio.run(main())
```

## 7. 添加提取策略 🧠

用户可以使用提取策略，如 `JsonCssExtractionStrategy`，该策略使用 CSS 选择器从 HTML 中提取结构化数据。

```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json

async def main():
    schema = {
        "name": "新闻文章",
        "baseSelector": "article.tease-card",
        "fields": [
            {
                "name": "title",
                "selector": "h2",
                "type": "text",
            },
            {
                "name": "summary",
                "selector": "div.tease-card__info",
                "type": "text",
            }
        ],
    }

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            extraction_strategy=JsonCssExtractionStrategy(schema, verbose=True)
        )
        extracted_data = json.loads(result.extracted_content)
        print(f"提取到 {len(extracted_data)} 篇文章")
        print(json.dumps(extracted_data[0], indent=2))

asyncio.run(main())
```





## 6 和 7 的区别



###  一、核心目的不同

| 策略类型                                    | 目的                                                         |
| ------------------------------------------- | ------------------------------------------------------------ |
| **`JsonCssExtractionStrategy`（提取策略）** | **从 HTML 中结构化地抽取特定字段**（如标题、摘要），输出是 **结构化数据**（如 JSON 列表）。 |
| **`RegexChunking`（分块策略）**             | **将原始文本按规则切分成片段**（chunks），输出仍是 **非结构化的文本块列表**，用于后续处理（如向量化、摘要、RAG）。 |





> ✅ 提取 = “我要新闻的标题和摘要”
>  ✅ 分块 = “把整篇文章按段落切开，方便后面分析”



### 二、处理阶段不同

- **提取策略**：在 **HTML 解析阶段** 工作，直接操作 DOM 树，使用 CSS 选择器定位元素。
- **分块策略**：在 **文本清理之后、返回结果之前** 工作，操作的是纯文本（通常是 `crawler` 提取的 `cleaned_html` 或 `markdown` 内容）。





流程示意：



```tex
1HTML → (可选：JS 渲染) → 清理文本（去噪、转 Markdown） → [分块策略] → 返回 chunks
2                             ↓
3                      [提取策略] → 返回结构化 JSON
```





⚠️ 注意：**提取策略和分块策略通常不会同时生效**。如果你指定了 `extraction_strategy`，`chunking_strategy` 一般会被忽略（取决于 `crawl4ai` 的实现逻辑）。两者是互斥的使用路径。

###  三、输出格式对比

#### 使用 `JsonCssExtractionStrategy`：





```json
1[
2  {
3    "title": "Trump appeals to the Supreme Court...",
4    "summary": "A federal court ruled his tariffs illegal..."
5  },
6  ...
7]
```





→ 可直接用于数据分析、数据库入库等。

#### 使用 `RegexChunking(patterns=["\n\n"])`：





```python
1[
2  "Trump appeals to the Supreme Court to preserve his sweeping tariffs\n\nChris Ratcliffe / Bloomberg via Getty Images file",
3  "Apple has survived Trump's tariffs so far. It might raise iPhone prices anyway.\n\nLATEST BUSINESS NEWS",
4  ...
5]
```







→ 每个 chunk 是一段连续文本，保留原始语言，适合送入 LLM 做摘要、问答或嵌入。

------

### 🛠 四、适用场景不同

| 场景                                     | 推荐策略                             |
| ---------------------------------------- | ------------------------------------ |
| 构建新闻聚合 API，需要标题+摘要          | ✅ `JsonCssExtractionStrategy`        |
| 将网页内容切片后存入向量数据库（RAG）    | ✅ `RegexChunking` 或 `TokenChunking` |
| 抓取商品价格、作者、发布时间等结构化字段 | ✅ 提取策略                           |
| 对长文章做语义分段以便 LLM 理解          | ✅ 分块策略                           |

------

### 🌰 举个实际例子（基于你提供的 NBC 页面）

- **用提取策略**：你想得到“每篇新闻的标题”，但页面没有清晰的 `<article>` 结构 → **可能失败或为空**。
- **用分块策略**：你不在乎结构，只想把页面所有文字按空行切开 → **能拿到一堆文本段落**，即使混杂了图片说明、重复标签，也能作为原始素材进一步清洗。

------

### ✅ 总结：关键区别一览

| 维度         | 提取策略 (`ExtractionStrategy`) | 分块策略 (`ChunkingStrategy`) |
| ------------ | ------------------------------- | ----------------------------- |
| **目标**     | 抽取结构化字段                  | 切分原始文本                  |
| **输入**     | HTML DOM                        | 清理后的纯文本                |
| **输出**     | JSON / 字典列表                 | 字符串列表（chunks）          |
| **依赖**     | HTML 结构稳定性                 | 文本分隔模式（如 `\n\n`）     |
| **典型用途** | 数据采集、爬虫入库              | RAG、LLM 上下文准备           |
| **是否互斥** | 通常与分块策略互斥              | 通常与提取策略互斥            |

------

### 💡 建议

- 如果你知道目标网站有 **稳定结构**（如电商产品页、博客列表），优先用 **提取策略**。
- 如果网站结构混乱、动态渲染强（如新闻门户、论坛），或你需要 **全文语义处理**，优先用 **分块策略 + LLM 后处理**。

如果你希望先分块再对每个 chunk 做结构化提取，可能需要 **分两步**：先用 `chunking_strategy` 获取文本块，再对每个 chunk 单独调用 LLM 提取信息。







## 8. 使用 LLM 提取策略 🤖



LLMExtractionStrategy 使用大型语言模型从网页中提取相关信息。

```python
from crawl4ai.extraction_strategy import LLMExtractionStrategy
import os
from pydantic import BaseModel, Field

class OpenAIModelFee(BaseModel):
    model_name: str = Field(..., description="OpenAI模型名称。")
    input_fee: str = Field(..., description="OpenAI模型输入token的费用。")
    output_fee: str = Field(..., description="OpenAI模型输出token的费用。")

async def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("未找到OpenAI API密钥。跳过此示例。")
        return

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://openai.com/api/pricing/",
            word_count_threshold=1,
            extraction_strategy=LLMExtractionStrategy(
                provider="openai/gpt-4o",
                api_token=os.getenv("OPENAI_API_KEY"),
                schema=OpenAIModelFee.schema(),
                extraction_type="schema",
                instruction="""从爬取内容中提取所有提到的模型名称以及其输入和输出token的费用。 
                不要遗漏内容中的任何模型。提取的模型JSON格式应如下所示: 
                {"model_name": "GPT-4", "input_fee": "US$10.00 / 1M tokens", "output_fee": "US$30.00 / 1M tokens"}。""",
            ),
            bypass_cache=True,
        )
        print(result.extracted_content)

asyncio.run(main())
```

## 9. 交互式提取 🖱️

用户可以使用 JavaScript 与页面进行交互，然后再进行提取。

```python
async def main():
    js_code = """
    const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More'));
    loadMoreButton && loadMoreButton.click();
    """

    wait_for = """() => {
        return Array.from(document.querySelectorAll('article.tease-card')).length > 10;
    }"""

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            js_code=js_code,
            wait_for=wait_for,
            css_selector="article.tease-card",
            bypass_cache=True,
        )
        print(f"JavaScript交互结果: {result.extracted_content[:500]}")

asyncio.run(main())
```

## 10. 高级会话爬取与动态内容 🔄

在现代 Web 应用程序中，内容通常在不更改 URL 的情况下动态加载。这在单页面应用程序（SPA）或使用无限滚动的网站中很常见。传统的依赖 URL 变化的爬取方法无法在这里工作。Crawl4AI 的高级会话爬取技术非常有用。

### 10.1 会话保持

通过使用 `session_id`，用户可以在与页面多次交互的过程中保持爬虫会话的状态。这对于导航动态加载的内容至关重要。

### 10.2 异步 JavaScript 执行

用户可以执行自定义 JavaScript，以触发内容加载或导航。下面是一个示例，爬取 GitHub 仓库中的多个页的提交。

```python
import json
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        url = "https://github.com/microsoft/TypeScript/commits/main"
        session_id = "typescript_commits_session"
        all_commits = []

        js_next_page = """
        const button = document.querySelector('a[data-testid="pagination-next-button"]');
        if (button) button.click();
        """

        wait_for = """() => {
            const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
            if (commits.length === 0) return false;
            const firstCommit = commits[0].textContent.trim();
            return firstCommit !== window.lastCommit;
        }"""

        schema = {
            "name": "提交提取器",
            "baseSelector": "li.Box-sc-g0xbh4-0",
            "fields": [
                {
                    "name": "title",
                    "selector": "h4.markdown-title",
                    "type": "text",
                    "transform": "strip",
                },
            ],
        }
        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

        for page in range(3):  # 爬取3页
            result = await crawler.arun(
                url=url,
                session_id=session_id,
                css_selector="li.Box-sc-g0xbh4-0",
                extraction_strategy=extraction_strategy,
                js_code=js_next_page if page > 0 else None,
                wait_for=wait_for if page > 0 else None,
                js_only=page > 0,
                bypass_cache=True,
                headless=False,
            )

            assert result.success, f"爬取第 {page + 1} 页失败"

            commits = json.loads(result.extracted_content)
            all_commits.extend(commits)

            print(f"第 {page + 1} 页: 找到 {len(commits)} 个提交")

        await crawler.crawler_strategy.kill_session(session_id)
        print(f"成功爬取 {len(all_commits)} 个提交，共3页")

asyncio.run(main())
```

在此示例中，用户爬取 GitHub 仓库中的多个提交页面。URL 在加载更多提交时不会发生变化，因此用户使用 JavaScript 单击“加载更多”按钮，并指定 `wait_for` 条件以确保在提取之前新内容已完全加载。这种强大的组合使用户能够轻松导航和提取复杂的动态加载 Web 应用程序中的数据。





























# 入门 Crawl4AI

欢迎使用 **Crawl4AI**，一个开源的 LLM 友好型网页爬虫和抓取工具。在本教程中，你将学会：

1. 运行你的 **第一个爬取任务**，并使用最小化配置。
2. 生成 **Markdown** 输出（并了解内容过滤器如何影响其结果）。
3. 体验一个简单的 **基于 CSS 的提取** 方法。
4. 了解 **基于 LLM 的提取**（包括开源和闭源模型选项）。
5. 爬取一个 **动态** 页面，该页面通过 JavaScript 加载内容。

------

## 1. 介绍

Crawl4AI 提供以下功能：

- 一个异步爬虫，**`AsyncWebCrawler`**。
- 通过 **`BrowserConfig`** 和 **`CrawlerRunConfig`** 可配置浏览器和运行设置。
- 通过 **`DefaultMarkdownGenerator`** 自动将 HTML 转换为 Markdown（支持可选过滤器）。
- 多种提取策略（基于 LLM 或 “传统” CSS/XPath）。

在本指南结束时，你将完成基本爬取、生成 Markdown、尝试两种提取策略，并爬取一个使用“加载更多”按钮或 JavaScript 更新的动态页面。

------

## 2. 你的第一个爬取任务

下面是一个最小化的 Python 脚本，创建了 **`AsyncWebCrawler`**，获取网页并打印前 300 个字符的 Markdown 输出：

```
import asynciofrom crawl4ai import AsyncWebCrawlerasync def main():    async with AsyncWebCrawler() as crawler:        result = await crawler.arun("https://example.com")        print(result.markdown[:300])  # 打印前 300 个字符if __name__ == "__main__":    asyncio.run(main())
```

**发生了什么？**

- **`AsyncWebCrawler`** 启动了一个无头浏览器（默认使用 Chromium）。
- 它获取 `https://example.com`。
- Crawl4AI 自动将 HTML 转换为 Markdown。

你现在已经成功运行了一个简单的爬取任务！

------

## 3. 基础配置（轻量介绍）

Crawl4AI 的爬虫可以通过两个主要类进行高度自定义：

1. **`BrowserConfig`**：控制浏览器行为（无头模式或带 UI，用户代理，JavaScript 开关等）。
2. **`CrawlerRunConfig`**：控制爬取运行方式（缓存、提取、超时、钩子等）。

下面是一个简单的使用示例：

```
import asynciofrom crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheModeasync def main():    browser_conf = BrowserConfig(headless=True)  # 设为 False 以观察浏览器    run_conf = CrawlerRunConfig(        cache_mode=CacheMode.BYPASS    )    async with AsyncWebCrawler(config=browser_conf) as crawler:        result = await crawler.arun(            url="https://example.com",            config=run_conf        )        print(result.markdown)if __name__ == "__main__":    asyncio.run(main())
```

> **重要**：默认情况下，缓存模式设置为 `CacheMode.ENABLED`。如果需要获取最新内容，请将其设置为 `CacheMode.BYPASS`。

在后续教程中，我们将探索更高级的配置（如启用代理、PDF 输出、多标签页会话等）。目前，你只需知道如何传递这些对象来管理爬取任务。

------

## 4. 生成 Markdown 输出

Crawl4AI 默认会自动将每个爬取的页面转换为 Markdown。但具体的输出取决于你是否指定了 **Markdown 生成器** 或 **内容过滤器**。

- **`result.markdown`**： 直接的 HTML 转 Markdown 转换结果。
- **`result.markdown.fit_markdown`**： 应用了任何已配置 **内容过滤器**（如 `PruningContentFilter`）后的 Markdown。

### 示例：使用 `DefaultMarkdownGenerator` 进行过滤

```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfigfrom crawl4ai.content_filter_strategy import PruningContentFilterfrom crawl4ai.markdown_generation_strategy import DefaultMarkdownGeneratormd_generator = DefaultMarkdownGenerator(    content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed"))config = CrawlerRunConfig(    cache_mode=CacheMode.BYPASS,    markdown_generator=md_generator)async with AsyncWebCrawler() as crawler:    result = await crawler.arun("https://news.ycombinator.com", config=config)    print("原始 Markdown 长度:", len(result.markdown.raw_markdown))    print("过滤后 Markdown 长度:", len(result.markdown.fit_markdown))
```

**注意**：如果 **不** 指定内容过滤器或 Markdown 生成器，你通常只能看到原始 Markdown。`PruningContentFilter` 可能会增加 `50ms` 处理时间。

------

## 5. 简单数据提取（基于 CSS）

Crawl4AI 允许使用 CSS 或 XPath 选择器提取结构化数据（JSON）。以下是一个基于 CSS 的最小示例：

```
import asyncioimport jsonfrom crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheModefrom crawl4ai.extraction_strategy import JsonCssExtractionStrategyasync def main():    schema = {        "name": "Example Items",        "baseSelector": "div.item",        "fields": [            {"name": "title", "selector": "h2", "type": "text"},            {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}        ]    }    raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"    async with AsyncWebCrawler() as crawler:        result = await crawler.arun(            url="raw://" + raw_html,            config=CrawlerRunConfig(                cache_mode=CacheMode.BYPASS,                extraction_strategy=JsonCssExtractionStrategy(schema)            )        )        data = json.loads(result.extracted_content)        print(data)if __name__ == "__main__":    asyncio.run(main())
```

**为什么使用？**

- 适用于重复的页面结构（如商品列表、文章等）。
- 无需 AI，节省 API 成本。
- 爬虫返回 JSON 字符串，方便解析或存储。