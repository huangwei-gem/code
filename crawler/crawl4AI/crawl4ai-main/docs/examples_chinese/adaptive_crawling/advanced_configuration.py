"""
高级自适应爬取配置示例

本示例演示自适应爬取的所有配置选项，
包括阈值调整、持久化和自定义参数。
"""

import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler, AdaptiveCrawler, AdaptiveConfig


async def main():
    """演示高级配置选项"""
    
    # 示例1：针对不同用例的自定义阈值
    print("="*60)
    print("示例1：自定义置信度阈值")
    print("="*60)
    
    # 高精度配置（详尽爬取）
    high_precision_config = AdaptiveConfig(
        confidence_threshold=0.9,      # 需要非常高的置信度
        max_pages=50,                  # 允许更多页面
        top_k_links=5,                 # 每页跟随更多链接
        min_gain_threshold=0.02        # 降低阈值以继续
    )
    
    # 平衡配置（默认用例）
    balanced_config = AdaptiveConfig(
        confidence_threshold=0.7,      # 中等置信度
        max_pages=20,                  # 合理限制
        top_k_links=3,                 # 中等分支
        min_gain_threshold=0.05        # 标准增益阈值
    )
    
    # 快速探索配置
    quick_config = AdaptiveConfig(
        confidence_threshold=0.5,      # 可接受的较低置信度
        max_pages=10,                  # 严格限制
        top_k_links=2,                 # 最小分支
        min_gain_threshold=0.1         # 需要高增益
    )
    
    async with AsyncWebCrawler(verbose=False) as crawler:
        # 测试不同配置
        for config_name, config in [
            ("高精度", high_precision_config),
            ("平衡", balanced_config),
            ("快速探索", quick_config)
        ]:
            print(f"\n测试{config_name}配置...")
            adaptive = AdaptiveCrawler(crawler, config=config)
            
            result = await adaptive.digest(
                start_url="https://httpbin.org",
                query="http headers authentication"
            )
            
            print(f"  - 爬取页面数: {len(result.crawled_urls)}")
            print(f"  - 达到置信度: {adaptive.confidence:.2%}")
            print(f"  - 覆盖率评分: {adaptive.coverage_stats['coverage']:.2f}")
    
    # 示例2：持久化和状态管理
    print("\n" + "="*60)
    print("示例2：状态持久化")
    print("="*60)
    
    state_file = "crawl_state_demo.json"
    
    # 带持久化的配置
    persistent_config = AdaptiveConfig(
        confidence_threshold=0.8,
        max_pages=30,
        save_state=True,              # 启用自动保存
        state_path=state_file         # 指定保存位置
    )
    
    async with AsyncWebCrawler(verbose=False) as crawler:
        # 第一次爬取 - 将被中断
        print("\n开始初始爬取（5页后中断）...")
        
        interrupt_config = AdaptiveConfig(
            confidence_threshold=0.8,
            max_pages=5,              # 人为降低以模拟中断
            save_state=True,
            state_path=state_file
        )
        
        adaptive = AdaptiveCrawler(crawler, config=interrupt_config)
        result1 = await adaptive.digest(
            start_url="https://docs.python.org/3/",
            query="exception handling try except finally"
        )
        
        print(f"第一次爬取完成: {len(result1.crawled_urls)} 页面")
        print(f"达到置信度: {adaptive.confidence:.2%}")
        
        # 从保存状态恢复爬取
        print("\n从保存状态恢复爬取...")
        
        resume_config = AdaptiveConfig(
            confidence_threshold=0.8,
            max_pages=20,             # 增加限制
            save_state=True,
            state_path=state_file
        )
        
        adaptive2 = AdaptiveCrawler(crawler, config=resume_config)
        result2 = await adaptive2.digest(
            start_url="https://docs.python.org/3/",
            query="exception handling try except finally",
            resume_from=state_file
        )
        
        print(f"恢复爬取完成: {len(result2.crawled_urls)} 总页面数")
        print(f"最终置信度: {adaptive2.confidence:.2%}")
        
        # 清理
        Path(state_file).unlink(missing_ok=True)
    
    # 示例3：链接选择策略
    print("\n" + "="*60)
    print("示例3：链接选择策略")
    print("="*60)
    
    # 保守的链接跟随
    conservative_config = AdaptiveConfig(
        confidence_threshold=0.7,
        max_pages=15,
        top_k_links=1,                # 只跟随最佳链接
        min_gain_threshold=0.15       # 高阈值
    )
    
    # 激进的链接跟随
    aggressive_config = AdaptiveConfig(
        confidence_threshold=0.7,
        max_pages=15,
        top_k_links=10,               # 跟随许多链接
        min_gain_threshold=0.01       # 非常低阈值
    )
    
    async with AsyncWebCrawler(verbose=False) as crawler:
        for strategy_name, config in [
            ("保守", conservative_config),
            ("激进", aggressive_config)
        ]:
            print(f"\n{strategy_name}链接选择:")
            adaptive = AdaptiveCrawler(crawler, config=config)
            
            result = await adaptive.digest(
                start_url="https://httpbin.org",
                query="api endpoints"
            )
            
            # 分析爬取模式
            print(f"  - 总页面数: {len(result.crawled_urls)}")
            print(f"  - 唯一域名数: {len(set(url.split('/')[2] for url in result.crawled_urls))}")
            print(f"  - 最大深度: {max(url.count('/') for url in result.crawled_urls) - 2}")
            
            # 显示饱和趋势
            if hasattr(result, 'new_terms_history') and result.new_terms_history:
                print(f"  - 发现新词: {result.new_terms_history[:5]}...")
                print(f"  - 饱和趋势: {'下降' if result.new_terms_history[-1] < result.new_terms_history[0] else '上升'}")
    
    # 示例4：监控爬取进度
    print("\n" + "="*60)
    print("示例4：进度监控")
    print("="*60)
    
    # 带详细监控的配置
    monitor_config = AdaptiveConfig(
        confidence_threshold=0.75,
        max_pages=10,
        top_k_links=3
    )
    
    async with AsyncWebCrawler(verbose=False) as crawler:
        adaptive = AdaptiveCrawler(crawler, config=monitor_config)
        
        # 开始爬取
        print("\n监控爬取进度...")
        result = await adaptive.digest(
            start_url="https://httpbin.org",
            query="http methods headers"
        )
        
        # 详细统计
        print("\n详细爬取分析:")
        adaptive.print_stats(detailed=True)
        
        # 导出分析
        print("\n导出知识库用于外部分析...")
        adaptive.export_knowledge_base("knowledge_export_demo.jsonl")
        print("知识库导出到: knowledge_export_demo.jsonl")
        
        # 显示导出数据样本
        with open("knowledge_export_demo.jsonl", 'r') as f:
            first_line = f.readline()
            print(f"导出样本: {first_line[:100]}...")


if __name__ == "__main__":
    asyncio.run(main())