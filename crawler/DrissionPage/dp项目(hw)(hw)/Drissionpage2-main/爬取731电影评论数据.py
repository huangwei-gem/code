from DrissionPage import ChromiumPage # 自动化模块
import datetime,time    # 转换时间戳 和 睡眠用到的模块
import csv, os  # 存储表格用的
# 存储表格
file_name = '爬取抖音731电影评论.csv'
file_exists = os.path.isfile('爬取抖音731电影评论.csv') and os.path.getsize('爬取抖音731电影评论.csv') > 0
file = open(file_name, 'a', encoding='utf-8-sig', newline='')
csvwriter = csv.DictWriter(file,fieldnames=[
    '用户',
    '评论',
    '地区',
    '点赞数',
    '时间'
])
if not file_exists:
    csvwriter.writeheader()
# 打开浏览器
dp = ChromiumPage()
# 监听数据包
dp.listen.start('/comment/list')
# 自动打开网站
dp.get('https://www.douyin.com/user/self?modal_id=7548661320325811465')
# 延迟 基于不同电脑 等待反应
time.sleep(3)
#  定位到评论元素 - 执行自动点击
dp.ele('css:.jp8u3iov').click()
# 翻100页的评论
for p in range(1, 101):
    print(f'\n======正在爬取第{p}页数据========\n')
    # 等待数据包
    resp = dp.listen.wait()
    # 获得数据
    data = resp.response.body
    try:
        msg = data['comments']  # 返回Json内容  列表提取数据
    except:
        print('没有更多数据了。')
        pass
    # 遍历数据
    for i in msg:
        keys = [item for item in i.keys()]  # 判断ip_label字段是否存在-有些用户的评论没有地区ip
        if 'ip_label' not in keys:  # 如果不存在 显示未知地区
            ip_label = '未知'
        else:   # 否则，也就是存在 - 显示用户真实地区
            ip_label = i['ip_label']
        t = i['create_time']    # 转换时间戳
        time = datetime.datetime.fromtimestamp(t)
        # 存储数据
        dic = {
            '用户':i['user']['nickname'],
            '评论':i['text'],
            '地区': f'{ip_label}',
            '点赞数':i['digg_count'],
            '时间': f'{time}'
        }
        csvwriter.writerow(dic)
        print(dic)
    try:
        fy = dp.ele('xpath://*[@id="merge-all-comment-container"]/div/div[3]')  # 定位翻页元素
        fy.scroll.to_bottom()   # 一直自动滚动到网页底部
    except:
        pass