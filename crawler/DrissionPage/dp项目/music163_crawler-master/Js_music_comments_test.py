import requests
import json
import asyncio
import aiohttp
import aiofiles
import re
import execjs
import time


cookies = {
    'Qs_lvt_382223': '1726643116',
    'Qs_pv_382223': '2610020288482423000',
    '_ga': 'GA1.1.1674354346.1726643117',
    '_clck': 'f2kdag%7C2%7Cfpa%7C0%7C1722',
    '_ga_C6TGHFPQ1H': 'GS1.1.1726643116.1.1.1726643187.0.0.0',
    'NMTID': '00OOtMeceIc8KlyoEI_hL3LcdpJ0ngAAAGVKzndFg',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'e34a15fc20b9518b86d812cb14919b19,1740186966482',
    '_ntes_nuid': 'e34a15fc20b9518b86d812cb14919b19',
    'WEVNSM': '1.0.0',
    'WNMCID': 'gwmqym.1740186966650.01.0',
    'ntes_utid': 'tid._.Hfrt%252BaWPGzRFAgARAVeEhCDhjGZvFexK._.0',
    'WM_TID': 'uWADy2Zbm%2FtERREUABeQFBrQXrd%2BA5YI',
    'sDeviceId': 'YD-SMmxvc6YwMFAEkAFQUaVPWeVtVEjGmtT',
    'WM_NI': '%2B%2BxbI%2BP1BPZPBVkB27VbMX0FHmA%2FCSOcUIl6St5z%2BWu2q6hAgkcnuSRwvZnFGGza8YxwJ0nkGreyQkoOgJi2e%2Bbksnv2Eg6NIRTJkZJJrcjmryQNFDxUflwCaKFp5yaMc0Y%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee83c964aaaf8b86d15e8f968aa2d15f969b9a83cb47f18ea2a3c77eb0bc8db1c42af0fea7c3b92ae9f5b883cc2194ef8eb1d95c828aa5a3b13d96be83b9b34e8cb38fd0c2598dbd9baaef3e91acfb9baa5db7eebfd7eb4ba5b5ad8ff85992a9babbed4e8599b682bb53bca986d1ed6185aeab9ad461ad91a9abec3aa7f5ae8cf266b6ee8b88b5468b8e9cabea528a96be84e967b2a79fafc550bc8baa8df649a3958a91b873a393add1dc37e2a3',
    'JSESSIONID-WYYY': 'SpGbDvPvcU0HOkvA%2BY4q%5CYblZhS0%5COdxnIfB2lFgcOScaNadw%2BtZtXPtW%2B%2BYb7vvufBO2vs%2FcEAT8Vtje%5CI2%5C3KJu4HGb7vCDr95DP1OnW0fB9K4gFPdwXXzii25biYAbhbyM4Ts%2Faa0BUtjJPEABtUEDMhmQBrw%5CMI%2B8mV4uQy15m%2FN%3A1740630393839',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/playlist?id=12937122744',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    # 'cookie': 'Qs_lvt_382223=1726643116; Qs_pv_382223=2610020288482423000; _ga=GA1.1.1674354346.1726643117; _clck=f2kdag%7C2%7Cfpa%7C0%7C1722; _ga_C6TGHFPQ1H=GS1.1.1726643116.1.1.1726643187.0.0.0; NMTID=00OOtMeceIc8KlyoEI_hL3LcdpJ0ngAAAGVKzndFg; _iuqxldmzr_=32; _ntes_nnid=e34a15fc20b9518b86d812cb14919b19,1740186966482; _ntes_nuid=e34a15fc20b9518b86d812cb14919b19; WEVNSM=1.0.0; WNMCID=gwmqym.1740186966650.01.0; ntes_utid=tid._.Hfrt%252BaWPGzRFAgARAVeEhCDhjGZvFexK._.0; WM_TID=uWADy2Zbm%2FtERREUABeQFBrQXrd%2BA5YI; sDeviceId=YD-SMmxvc6YwMFAEkAFQUaVPWeVtVEjGmtT; WM_NI=%2B%2BxbI%2BP1BPZPBVkB27VbMX0FHmA%2FCSOcUIl6St5z%2BWu2q6hAgkcnuSRwvZnFGGza8YxwJ0nkGreyQkoOgJi2e%2Bbksnv2Eg6NIRTJkZJJrcjmryQNFDxUflwCaKFp5yaMc0Y%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee83c964aaaf8b86d15e8f968aa2d15f969b9a83cb47f18ea2a3c77eb0bc8db1c42af0fea7c3b92ae9f5b883cc2194ef8eb1d95c828aa5a3b13d96be83b9b34e8cb38fd0c2598dbd9baaef3e91acfb9baa5db7eebfd7eb4ba5b5ad8ff85992a9babbed4e8599b682bb53bca986d1ed6185aeab9ad461ad91a9abec3aa7f5ae8cf266b6ee8b88b5468b8e9cabea528a96be84e967b2a79fafc550bc8baa8df649a3958a91b873a393add1dc37e2a3; JSESSIONID-WYYY=SpGbDvPvcU0HOkvA%2BY4q%5CYblZhS0%5COdxnIfB2lFgcOScaNadw%2BtZtXPtW%2B%2BYb7vvufBO2vs%2FcEAT8Vtje%5CI2%5C3KJu4HGb7vCDr95DP1OnW0fB9K4gFPdwXXzii25biYAbhbyM4Ts%2Faa0BUtjJPEABtUEDMhmQBrw%5CMI%2B8mV4uQy15m%2FN%3A1740630393839',
}

params = {
    'csrf_token': '',
}



# response = requests.post(
#     'https://music.163.com/weapi/comment/resource/comments/get',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )
def music_href_list():
    url_list = []
    with open('music_href') as f:
        for line in f:
            #“相信有纯白会越过山海” \ https://music.163.com/#/playlist?id=910247465
            line = line.strip().split(' \\ ')
            music_id = line[1].split('playlist?id=')[-1]
            line.append(music_id)
            url_list.append(line)
    # print(url_list)
    return url_list

def music_data(s,playlist_id):
    aa = f'{{"rid":"A_PL_0_{playlist_id}","threadId":"A_PL_0_{playlist_id}","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}}'
    bb = '010001'
    cc = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    dd = '0CoJUm6Qyw8W8jud'
    comments_data = execjs.compile(s).call('d',aa,bb,cc,dd)
    return comments_data

def do_music_data(f,title,href,data):
    music = {
        '歌曲主题':[],
        '歌曲链接':[],
        '评论用户':[],
        '评论内容':[],
        '评论时间':[],
        '点赞数':[],
    }
    music['歌曲主题'].append(title)
    music['歌曲链接'].append(href)
    hotcomments  = data['data']['hotComments']
    if hotcomments != None:
        for hotcomment in hotcomments:
            music['评论用户'].append(hotcomment['user']['nickname'])
            music['评论内容'].append(hotcomment['content'])
            music['评论时间'].append(hotcomment['timeStr'])
            music['点赞数'].append(hotcomment['likedCount'])
        # new_row = pd.DataFrame(music)
        # df._append(new_row, ignore_index=True)
        # wirte_file(json.dumps(music))
        # wirte_file(json.dumps(music,ensure_ascii=False)+'\n')
        f.write(json.dumps(music,ensure_ascii=False)+'\n')
    else:
        music['评论用户'].append('暂无')
        music['评论内容'].append('暂无')
        music['评论时间'].append('暂无')
        music['点赞数'].append('暂无')
        # new_row = pd.DataFrame(music)
        # df._append(new_row, ignore_index=True)
        # wirte_file(json.dumps(music)+'\n')
        f.write(json.dumps(music,ensure_ascii=False)+'\n')


def fetch(s,f,session,music):
    # print("发送请求::",url)
    title = music[0]
    url = 'https://music.163.com/weapi/comment/resource/comments/get'
    id = music[-1]
    h = music_data(s,id)
    data = {
    'params':h['encText'],
    'encSecKey':h['encSecKey']
    }
    response = session.post(url,params=params,cookies=cookies,headers=headers,data=data)
    music_comments_data = response.text
    do_music_data(f,title,music[1],json.loads(music_comments_data))


def main():
    music_list = music_href_list()
    session = requests.session()
    with open('comments.js') as file:
        s = file.read() 
    with open('music_data.csv','a') as f:
        for music in music_list[0:50]:
            fetch(s,f,session,music)



if __name__ == '__main__':
    # print(urlist)
    #href="/playlist?id=12646326771" class="msk
    # <a title="韩流教科书｜一秒沦陷宿命感极强的韩流" href="/playlist?id=13015254350" class="msk"></a>
    # music_href_list = re.findall('<a title="(.*?)" href="(.*?)" class="msk',response.text)
    # print(music_href_list)
    st = time.time()
    main()
    print(f'{time.time()-st}')
    # asyncio.run(main())
    # for i in music_href_list():
    #     print(len(i))

#拿数据
# print((response.json())['data']['hotComments'])