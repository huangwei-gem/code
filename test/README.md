# Crawl4AI 安装和使用示例

## 安装状态
✅ **成功安装** - Crawl4AI 0.7.6 已在虚拟环境中安装完成

## 验证安装
运行测试脚本验证安装：
```bash
.\.venv\Scripts\python test_crawl4ai.py
```

## 快速开始

### 1. 激活虚拟环境
```bash
.\.venv\Scripts\activate
```

### 2. 运行示例
```bash
python crawl4ai_example.py
```

### 3. 基本使用示例
```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def crawl_webpage():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com",
            bypass_cache=True
        )
        
        if result.success:
            print(f"URL: {result.url}")
            print(f"HTML长度: {len(result.html)}")
            if result.markdown:
                print(f"Markdown长度: {len(str(result.markdown))}")

# 运行
asyncio.run(crawl_webpage())
```

## 主要功能

- **异步网页爬取**: 支持并发爬取多个网页
- **Markdown生成**: 自动将HTML转换为Markdown格式
- **内容过滤**: 智能提取主要内容
- **代理支持**: 支持代理服务器
- **浏览器模拟**: 支持JavaScript渲染
- **缓存机制**: 可选的缓存功能

## 可用工具

测试脚本显示可用的主要类：
- `AsyncWebCrawler`: 主要爬虫类
- `AdaptiveCrawler`: 自适应爬虫
- `BM25ContentFilter`: 内容过滤
- `LLMExtractionStrategy`: LLM提取策略
- `JsonCssExtractionStrategy`: CSS选择器提取

## 注意事项

1. 某些依赖项可能需要额外的系统库
2. 建议使用虚拟环境进行隔离
3. 爬取网页时请遵守robots.txt和相关法律法规

## 更多信息

- 项目主页: https://github.com/unclecode/crawl4ai
- 文档: 查看项目GitHub页面获取完整文档