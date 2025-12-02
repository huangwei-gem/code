from DrissionPage import WebPage,ChromiumOptions
from concurrent.futures import ThreadPoolExecutor
import time
#https://music.163.com/weapi/comment/resource/comments/get?csrf_token=
def page_hot_Comments(url,index):
    comments = []
    tabs = page.get_tabs(as_id=True)
    if len(tabs) < thread_num:
        page.new_tab()
        tab = page.latest_tab
        tab.listen.start('https://music.163.com/weapi/comment/resource/comments/get?csrf_token=')
        tab.get(url)
    else:
        tab = page.get_tab(tabs[index % thread_num])
        tab.listen.start('https://music.163.com/weapi/comment/resource/comments/get?csrf_token=')
        tab.get(url)
    res = tab.listen.wait()
    hot_Comments = res.response.body['data']['hotComments']
    if hot_Comments != None:
        for comment in hot_Comments:
            data = {
                'username' : comment['user']['nickname'],
                'content' : comment['content'],
                'timeStr' : comment['timeStr'],
                'likedCount' : comment['likedCount'],
            }
            comments.append(data)
    else:
        # print('暂无评论')
        return ['暂无评论']
    
    # print(comments)
    return comments
    # print(res.response.body['data']['hotComments'])
    
#对音乐歌单热评数据处理
def music_hrefs(filename):
    upgrade_music_href = []

    with open(filename) as f:
        for line in f:
            music = line.strip().split(' | ')            
            if 'https://music.163.com' not in music[-1]:
                music[-1] = 'https://music.163.com'+music[-1]
            # print(music[-1])
            temp_list = []
            temp_list.append(music[-1])
            if len(music)>2:
                temp_list.append(' | '.join(music[0:-1]))
                # print(' | '.join(music[0:-1]))
            else:
                temp_list.append(music[0])
            upgrade_music_href.append(temp_list)

    return upgrade_music_href

#拿到所有音乐歌单链接和名称
musics = music_hrefs('music_href')

thread_num = 3
co = ChromiumOptions()
co.headless(True)
co.auto_port()
page = WebPage(chromium_options = co)
# url = "https://music.163.com/playlist?id=12937122744"
# url = 'https://music.163.com/#/playlist?id=9382673612'
# with ThreadPoolExecutor(max_workers=thread_num, thread_name_prefix='thread') as tp:
#     futures = [tp.submit(page_hot_Comments,music[0],index) for index,music in enumerate(musics[0:5])]
for index,music in enumerate(musics[0:10]):
    comments = page_hot_Comments(music[0],index)
    print(music[1],comments)

page.quit()