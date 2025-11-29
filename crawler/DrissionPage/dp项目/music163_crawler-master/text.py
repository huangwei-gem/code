import execjs
playlist_id = 12952025836
with open('comments.js') as file:
    s = file.read() 
    aa = f'{{"rid":"A_PL_0_{playlist_id}","threadId":"A_PL_0_{playlist_id}","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}}'
    bb = '010001'
    cc = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    dd = '0CoJUm6Qyw8W8jud'
    comments_data = execjs.compile(s).call('d',aa,bb,cc,dd)