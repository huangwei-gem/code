"""
示例：在Crawl4AI中使用表格提取策略

本示例演示如何使用不同的表格提取策略
从网页中提取表格。
"""

import asyncio
import pandas as pd
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    CacheMode,
    DefaultTableExtraction,
    NoTableExtraction,
    TableExtractionStrategy
)
from typing import Dict, List, Any


async def example_default_extraction():
    """示例1：使用默认表格提取（自动）。"""
    print("\n" + "="*50)
    print("示例1：默认表格提取")
    print("="*50)
    
    async with AsyncWebCrawler() as crawler:
        # 无需指定table_extraction - 自动使用DefaultTableExtraction
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            table_score_threshold=7  # 调整敏感度（默认：7）
        )
        
        result = await crawler.arun(
            "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)",
            config=config
        )
        
        if result.success and result.tables:
            print(f"找到 {len(result.tables)} 个表格")
            
            # 将第一个表格转换为pandas DataFrame
            if result.tables:
                first_table = result.tables[0]
                df = pd.DataFrame(
                    first_table['rows'],
                    columns=first_table['headers'] if first_table['headers'] else None
                )
                print(f"\n第一个表格预览:")
                print(df.head())
                print(f"形状: {df.shape}")


async def example_custom_configuration():
    """示例2：自定义表格提取配置。"""
    print("\n" + "="*50)
    print("示例2：自定义表格配置")
    print("="*50)
    
    async with AsyncWebCrawler() as crawler:
        # 创建具有特定设置的自定义提取策略
        table_strategy = DefaultTableExtraction(
            table_score_threshold=5,  # 较低阈值，更宽松的检测
            min_rows=3,  # 只提取至少有3行的表格
            min_cols=2,  # 只提取至少有2列的表格
            verbose=True
        )
        
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            table_extraction=table_strategy,
            # 使用CSS选择器定位特定表格
            css_selector="div.main-content"
        )
        
        result = await crawler.arun(
            "https://example.com/data",
            config=config
        )
        
        if result.success:
            print(f"找到 {len(result.tables)} 个匹配条件的表格")
            
            for i, table in enumerate(result.tables):
                print(f"\n表格 {i+1}:")
                print(f"  标题: {table.get('caption', '无标题')}")
                print(f"  大小: {table['metadata']['row_count']} 行 × {table['metadata']['column_count']} 列")
                print(f"  有表头: {table['metadata']['has_headers']}")


async def example_disable_extraction():
    """示例3：不需要时禁用表格提取。"""
    print("\n" + "="*50)
    print("示例3：禁用表格提取")
    print("="*50)
    
    async with AsyncWebCrawler() as crawler:
        # 使用NoTableExtraction完全跳过表格处理
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            table_extraction=NoTableExtraction()  # 不会提取任何表格
        )
        
        result = await crawler.arun(
            "https://example.com",
            config=config
        )
        
        if result.success:
            print(f"提取的表格数: {len(result.tables)} (应该是0)")
            print("表格提取已禁用 - 对于非表格内容性能更好")


class FinancialTableExtraction(TableExtractionStrategy):
    """
    用于提取具有特定要求的财务表格的自定义策略。
    """
    
    def __init__(self, currency_symbols=None, **kwargs):
        super().__init__(**kwargs)
        self.currency_symbols = currency_symbols or ['$', '€', '£', '¥']
    
    def extract_tables(self, element, **kwargs):
        """只提取看起来包含财务数据的表格。"""
        tables_data = []
        
        for table in element.xpath(".//table"):
            # 检查表格是否包含货币符号
            table_text = ''.join(table.itertext())
            has_currency = any(symbol in table_text for symbol in self.currency_symbols)
            
            if not has_currency:
                continue
            
            # 使用基础逻辑提取（可以重用DefaultTableExtraction逻辑）
            headers = []
            rows = []
            
            # 提取表头
            for th in table.xpath(".//thead//th | .//tr[1]//th"):
                headers.append(th.text_content().strip())
            
            # 提取行
            for tr in table.xpath(".//tbody//tr | .//tr[position()>1]"):
                row = []
                for td in tr.xpath(".//td"):
                    cell_text = td.text_content().strip()
                    # 清理货币值
                    for symbol in self.currency_symbols:
                        cell_text = cell_text.replace(symbol, '')
                    row.append(cell_text)
                if row:
                    rows.append(row)
            
            if headers or rows:
                tables_data.append({
                    "headers": headers,
                    "rows": rows,
                    "caption": table.xpath(".//caption/text()")[0] if table.xpath(".//caption") else "",
                    "summary": table.get("summary", ""),
                    "metadata": {
                        "type": "financial",
                        "has_currency": True,
                        "row_count": len(rows),
                        "column_count": len(headers) if headers else len(rows[0]) if rows else 0
                    }
                })
        
        return tables_data


async def example_custom_strategy():
    """示例4：自定义表格提取策略。"""
    print("\n" + "="*50)
    print("示例4：自定义财务表格策略")
    print("="*50)
    
    async with AsyncWebCrawler() as crawler:
        # 对财务表格使用自定义策略
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            table_extraction=FinancialTableExtraction(
                currency_symbols=['$', '€'],
                verbose=True
            )
        )
        
        result = await crawler.arun(
            "https://finance.yahoo.com/",
            config=config
        )
        
        if result.success:
            print(f"找到 {len(result.tables)} 个财务表格")
            
            for table in result.tables:
                if table['metadata'].get('type') == 'financial':
                    print(f"  ✓ 财务表格，有 {table['metadata']['row_count']} 行")


async def main():
    """运行所有表格提取示例。"""
    print("开始表格提取示例...")
    
    try:
        await example_default_extraction()
        await example_custom_configuration()
        await example_disable_extraction()
        await example_custom_strategy()
        
        print("\n" + "="*50)
        print("所有表格提取示例完成！")
        print("="*50)
        
    except Exception as e:
        print(f"运行示例时出错: {e}")


if __name__ == "__main__":
    asyncio.run(main())