import time

from DrissionPage import ChromiumPage
from DataRecorder import Recorder

# 创建数据记录器实例，用于将数据保存到Excel文件
recorder = Recorder("data.xlsx")
# 设置不显示记录过程中的消息提示
recorder.set.show_msg(False)


def find_first_key_value(data, target_key):
    """
    递归查找字典或列表数据结构中的指定键值
    
    Args:
        data: 要搜索的数据（可能是字典、列表或其他类型）
        target_key: 目标键名
        
    Returns:
        找到的目标键对应的值，未找到则返回None
    """
    # (1) 处理数据为字典的递归遍历
    if isinstance(data, dict):
        for key, val in data.items():
            if key == target_key:
                return val
            # 递归遍历子元素
            ret = find_first_key_value(val, target_key)

            if ret is not None:
                return ret

    # (2) 处理数据为列表的递归遍历
    if isinstance(data, list):
        for item in data:
            ret = find_first_key_value(item, target_key)
            if ret is not None:
                return ret

    return None


def handler(page, keyword):
    """
    处理小红书搜索关键词并采集数据的主函数
    
    Args:
        page: ChromiumPage浏览器页面对象
        keyword: 搜索关键词
    """
    # 访问小红书搜索结果页面
    page.get(f"https://www.xiaohongshu.com/search_result?keyword={keyword}&source=unknown&type=51")
    # 等待页面加载完成
    time.sleep(3)
    # 创建集合用于去重已处理的卡片索引
    s = set()  # {}
    # 循环处理最多50页内容
    for i in range(1, 51):
        try:
            # 查找所有笔记卡片元素
            cards = page.eles('@class=note-item')
            # (1) 开始监听卡片详情接口数据
            page.listen.start("web/v1/feed")
            # 遍历所有卡片
            for card in cards:
                # 获取卡片的唯一索引用于去重
                index = card.attr("data-index")
                # 如果该卡片已经处理过则跳过
                if index in s:
                    continue
                # 将当前卡片索引加入已处理集合
                s.add(index)

                # 打印当前处理的卡片信息
                print(card)
                # 点击卡片中的图片以打开详情页
                card.ele('@tag()=img').click(by_js=True)
                # (2) 等待卡片详情接口数据返回
                res = page.listen.wait(count=1, timeout=1, fit_count=True)
                # (3) 获取接口响应数据
                data = res.response.body
                print("data:::", data)

                # 从响应数据中提取所需字段
                nickname = find_first_key_value(data, "nickname")  # 博主昵称
                title = find_first_key_value(data, "title")        # 笔记标题
                desc = find_first_key_value(data, "desc")          # 笔记详情
                comment_count = find_first_key_value(data, "comment_count")  # 评论数
                liked_count = find_first_key_value(data, "liked_count")      # 点赞数

                # 构造要保存的数据字典
                map = {
                    "博主昵称": nickname,
                    "标题": title,
                    "详情": desc,
                    "评论数": comment_count,
                    "点赞数": liked_count,
                }
                # 将数据添加到记录器并保存到Excel
                recorder.add_data(map)
                recorder.record()

                # 查找并点击关闭按钮关闭详情页
                close_btn = page.ele('@class=close close-mask-dark')
                close_btn.click()
                # 等待页面关闭完成
                time.sleep(3)

        except Exception as e:
            # 捕获并打印处理过程中出现的异常
            print("error:::", e)

        finally:
            # 滚动页面以加载更多内容
            # 向上滚动一点
            page.scroll.up(100)
            time.sleep(1)
            # 滚动到底部触发加载更多
            page.scroll.to_bottom()
            time.sleep(1)


def main():
    """主函数，负责读取关键词并启动爬虫"""
    # 从文件中读取搜索关键词列表
    with open("关键词.txt", mode="r", encoding="utf8") as f:
        keyword_list = f.readlines()

    # 创建浏览器驱动对象
    page = ChromiumPage()
    # 访问小红书探索页面
    page.get("https://www.xiaohongshu.com/explore")

    # 等待用户手动登录（扫码登录等）
    input("等待登录")

    # 遍历关键词列表，依次处理每个关键词
    for keyword in keyword_list:
        handler(page, keyword)


# 启动主程序
main()