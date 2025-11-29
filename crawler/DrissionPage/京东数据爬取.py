import json
import time

from DrissionPage import ChromiumPage
from DataRecorder import Recorder

# 创建数据记录器实例，用于将爬取的数据保存到Excel文件
recorder = Recorder("JD.xlsx")
# 设置不显示记录过程中的消息提示
recorder.set.show_msg(False)


def find_key_val(data, target_key, max_count=1):
    """
    从JSON数据中递归查找指定键的所有值
    
    Args:
        data: 要搜索的数据（可能是字典、列表、字符串或其他类型）
        target_key: 目标键名
        max_count: 最大返回结果数量，默认为1
        
    Returns:
        包含找到的目标键对应值的列表
    """
    # 存储找到的结果
    results = []

    # (1) 如果输入数据是字符串，尝试将其解析为JSON对象
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            # 如果解析失败，返回空结果列表
            return results

    def _search(data):
        """
        递归搜索函数
        """
        # 如果已达到最大数量限制，则停止搜索
        if len(results) == max_count:
            return
        # 处理数据为字典的情况
        if isinstance(data, dict):
            for key, val in data.items():
                if key == target_key:
                    # 找到目标键，将值添加到结果列表
                    results.append(val)
                    # 如果已达到最大数量限制，则停止搜索
                    if len(results) == max_count:
                        return
                # 递归遍历子元素继续搜索
                _search(val)

        # (2) 处理数据为列表的情况
        if isinstance(data, list):
            for item in data:
                ret = _search(item)
                if ret is not None:
                    return ret

        return None

    # 开始递归搜索
    _search(data)

    return results


def main():
    """
    主函数：爬取京东商品评价数据
    """
    # 创建Chromium浏览器页面对象
    page = ChromiumPage()
    # 开始监听包含"client.action"的网络请求
    page.listen.start("client.action")
    # 设置要爬取的京东商品页面URL
    url = "https://item.jd.com/100006466663.html"
    # 访问商品页面
    page.get(url)

    # 检查页面是否包含"全部评价"按钮元素
    if page.ele('@text()=全部评价'):
        # 点击"全部评价"按钮，进入评价页面
        page.ele('@text()=全部评价').click(by_js=True)

        # 循环爬取评价数据
        while 1:
            # 等待网络请求，最多等待10秒，期望捕获1个请求
            res = page.listen.wait(1, 10, fit_count=True)
            # 如果没有捕获到请求，则退出循环
            if not res:
                break
            # 获取网络请求的响应数据
            data = res.response.body
            print("data:::", data)
            # 从响应数据中查找最多11个"commentInfo"评价信息
            commentInfoList = find_key_val(data, "commentInfo", 11)
            # 遍历处理每条评论信息
            for commentInfo in commentInfoList:
                # 提取评价相关信息并构建数据字典
                map = {
                    "用户名": commentInfo.get("userNickName"),  # 用户昵称
                    "评论时间": commentInfo.get("commentDate"),   # 评论日期
                    "评论内容": commentInfo.get("commentData"),   # 评论内容
                    "评分": commentInfo.get("commentScore"),     # 评分
                }
                # 将数据添加到记录器
                recorder.add_data(map)
                # 将数据写入Excel文件
                recorder.record()
            # 滚动到评价列表容器底部以加载更多评价
            page.ele('@class=_rateListContainer_1ygkr_45').scroll.to_bottom()
            # 等待3秒，防止请求过于频繁被封号
            time.sleep(3)
    else:
        # 如果未找到"全部评价"按钮，输出提示信息
        print("没有等待到元素！")


if __name__ == '__main__':
    # 执行主函数
    main()