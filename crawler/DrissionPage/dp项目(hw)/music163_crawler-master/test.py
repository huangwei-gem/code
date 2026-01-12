import pandas as pd
# playlist_id = 12952025836
# s =  f'{{"rid":"A_PL_0_{playlist_id}","threadId":"A_PL_0_{playlist_id}","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}}'
# print(s)

data = {
    'commentsTitle': '全部评论',
    'comments':[
        {'user':'sam','content':'我是光'},
        {'user':'sam','content':'我是暗'},
        {'user':'sam','content':'i am beauty'},
        ],
    'hotcomments':[
        {'user':'a','content':'我是美女'},
        {'user':'b','content':'我是周杰伦'},
        {'user':'c','content':'我是林俊杰'},
        ],
    'totalCount':4590
}

df = pd.DataFrame(data)
df.to_csv('music_data.csv',index=False)