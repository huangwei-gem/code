import time
import argparse
from gen_id import get_resource_id
from id_to_m3u8 import get_m3u8_url
from download_m3u8 import download_video
from utils import logger
from config import config


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='微信小程序视频下载器')
    parser.add_argument('--mode', '-m', 
                      choices=['sync', 'async'], 
                      default='sync',
                      help='下载模式：sync（多线程）或 async（异步协程）')
    parser.add_argument('--max-workers', 
                      type=int,
                      default=config.max_workers,
                      help='最大线程数（仅sync模式有效）')
    parser.add_argument('--max-concurrency', 
                      type=int,
                      default=config.max_concurrency,
                      help='最大并发数（仅async模式有效）')
    parser.add_argument('--log-level', 
                      choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                      default=config.log_level,
                      help='日志级别')
    return parser.parse_args()


def main():
    """主程序入口"""
    # 解析命令行参数
    args = parse_arguments()
    
    # 设置使用的模式
    use_async = args.mode == 'async'
    
    logger.info(f"开始执行微信小程序视频下载，模式：{args.mode}")
    logger.info(f"最大{'并发数' if use_async else '线程数'}：{args.max_concurrency if use_async else args.max_workers}")
    
    start_time = time.time()
    
    try:
        # 获取资源ID列表
        id_list = get_resource_id()
        
        if not id_list:
            logger.error("没有获取到任何资源ID，下载失败")
            return
        
        # 遍历资源ID列表，下载每个视频
        for index, item in enumerate(id_list, 1):
            chapter_title = item['chapter_title']
            resource_id = item['resource_id']
            course_id = item['course_id']
            
            logger.info(f"\n=== 开始下载第 {index}/{len(id_list)} 个视频 ===")
            logger.info(f"章节标题: {chapter_title}")
            logger.info(f"资源ID: {resource_id}")
            logger.info(f"课程ID: {course_id}")
            
            # 获取M3U8 URL
            m3u8_url = get_m3u8_url(resource_id)
            
            if m3u8_url:
                # 下载视频
                download_video(m3u8_url, chapter_title, use_async=use_async)
                
                # 下载完成后等待一段时间，避免请求过于频繁
                logger.info("等待5秒后继续下载下一个视频...")
                time.sleep(5)
            else:
                logger.error(f"获取 {chapter_title} 的M3U8 URL失败，跳过该视频")
        
        end_time = time.time()
        logger.info("\n=== 所有视频下载完成 ===")
        logger.info(f"总耗时: {end_time - start_time:.2f}秒")
        logger.info(f"成功处理 {len(id_list)} 个视频")
        
    except KeyboardInterrupt:
        logger.info("用户中断了下载操作")
    except Exception as e:
        logger.error(f"程序执行出错: {e}")


if __name__ == '__main__':
    main()
