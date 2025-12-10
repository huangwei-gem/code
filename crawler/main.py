import requests

cookies = {
    'cookie2': '165d64985b19a6e687c55deebf97c570',
    't': 'ed2e039c33967996403b7ebd54c519a5',
    '_tb_token_': '31f734d73381f',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '4427291c954fa94cfdad59028ac06fd8_1765345596376',
    '_m_h5_tk_enc': '194544b57d74ebe68f2fb27ad1177379',
    'thw': 'xx',
    'xlly_s': '1',
    'cna': 'rNK/IQtESlgBASQIhFNYdf5B',
    'sca': '3701d619',
    '_samesite_flag_': 'true',
    'unb': '2216270359744',
    'uc1': 'pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie14=UoYY5pPUsWJI2Q%3D%3D',
    'sn': '',
    'uc3': 'lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD2kgkZ9IOrhl7has%3D&nk2=F5RGPuGaLchfHAC2vVI%3D&id2=UUpgQEv1TKINAKpz8w%3D%3D',
    'csg': 'da2074a9',
    'lgc': 'tb383601678590',
    'cancelledSubSites': 'empty',
    'cookie17': 'UUpgQEv1TKINAKpz8w%3D%3D',
    'dnk': 'tb383601678590',
    'skt': 'f7c52a2f5dbc54ab',
    'existShop': 'MTc2NTMzNjM3Nw%3D%3D',
    'uc4': 'nk4=0%40FY4NC%2FfAZIRxljamBGt6LY1zq7aRtu5%2BfQ%3D%3D&id4=0%40U2gqz6QfdnaFU5K1ocMVoMhQ8eaNM4gU',
    'tracknick': 'tb383601678590',
    '_cc_': 'W5iHLLyFfA%3D%3D',
    '_l_g_': 'Ug%3D%3D',
    'sg': '04c',
    '_nk_': 'tb383601678590',
    'cookie1': 'VAmowaEOXr2LGzlamcZkSV%2BGX36TVZNWtP7Kwz62XXo%3D',
    'wk_cookie2': '1010509a6d93ce08c0664c6b3b2672fb',
    'wk_unb': 'UUpgQEv1TKINAKpz8w%3D%3D',
    'sgcookie': 'E100%2Bq6a2859UpftCNePlq1diLoTDDPJu44bojNCJ7tqWJKMb57XPMpyaRYAnR%2B%2FNpVI949h7a22LALvjtNMNKJGYjh%2BbVVTne7%2BzRxMOJk%2BgWw%3D',
    'aui': '2216270359744',
    'tfstk': 'gPZo3IAPHzuWXDdVjBo5zcCP9K_xV0iI6WKK9DhFujlXwQK8Lvo3gWBSwJ57tkc4LUK8vzLn8WF0y2rK9kXnVoUJvbCSxJPtx1COXGe7F2iF61HRuD9EYvSKTZ3zbrlDb1COXihAL3J568KFhBeqIAoEU4lE3tDIgY8UTbu2gADsYXPUTj-qFATezv8ygxljLDlUTDWm0jMnYXPEYt2qGO8rNkr8063jPLJUSLZrE4caUjy8eokk6fyriH-EZY0lo8lDYHr08XxeWb76HXi-NJMuOGtS424zZxohxnouN8rEokCArRmu7Wi8098r_zF-0uzMLHymqbu04qAlifr73liqkGWg3oN8Fo2pLMkY6jy74DjNC0mramDbvstrtrzU24iBa_mUnvSPSE8NkJ-BR776RegrhxcTi05wadGZAf6cnFJIzxMr6tXDRegrhxcOntYMA4kjUfC..',
    'isg': 'BAQE2246Mc9_roUDKjvHpIAM1YL2HSiHOiTvzB6lz0-SSaYTVixyF1mvieGR0WDf',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'cookie2=165d64985b19a6e687c55deebf97c570; t=ed2e039c33967996403b7ebd54c519a5; _tb_token_=31f734d73381f; mtop_partitioned_detect=1; _m_h5_tk=4427291c954fa94cfdad59028ac06fd8_1765345596376; _m_h5_tk_enc=194544b57d74ebe68f2fb27ad1177379; thw=xx; xlly_s=1; cna=rNK/IQtESlgBASQIhFNYdf5B; sca=3701d619; _samesite_flag_=true; unb=2216270359744; uc1=pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie14=UoYY5pPUsWJI2Q%3D%3D; sn=; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD2kgkZ9IOrhl7has%3D&nk2=F5RGPuGaLchfHAC2vVI%3D&id2=UUpgQEv1TKINAKpz8w%3D%3D; csg=da2074a9; lgc=tb383601678590; cancelledSubSites=empty; cookie17=UUpgQEv1TKINAKpz8w%3D%3D; dnk=tb383601678590; skt=f7c52a2f5dbc54ab; existShop=MTc2NTMzNjM3Nw%3D%3D; uc4=nk4=0%40FY4NC%2FfAZIRxljamBGt6LY1zq7aRtu5%2BfQ%3D%3D&id4=0%40U2gqz6QfdnaFU5K1ocMVoMhQ8eaNM4gU; tracknick=tb383601678590; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=04c; _nk_=tb383601678590; cookie1=VAmowaEOXr2LGzlamcZkSV%2BGX36TVZNWtP7Kwz62XXo%3D; wk_cookie2=1010509a6d93ce08c0664c6b3b2672fb; wk_unb=UUpgQEv1TKINAKpz8w%3D%3D; sgcookie=E100%2Bq6a2859UpftCNePlq1diLoTDDPJu44bojNCJ7tqWJKMb57XPMpyaRYAnR%2B%2FNpVI949h7a22LALvjtNMNKJGYjh%2BbVVTne7%2BzRxMOJk%2BgWw%3D; aui=2216270359744; tfstk=gPZo3IAPHzuWXDdVjBo5zcCP9K_xV0iI6WKK9DhFujlXwQK8Lvo3gWBSwJ57tkc4LUK8vzLn8WF0y2rK9kXnVoUJvbCSxJPtx1COXGe7F2iF61HRuD9EYvSKTZ3zbrlDb1COXihAL3J568KFhBeqIAoEU4lE3tDIgY8UTbu2gADsYXPUTj-qFATezv8ygxljLDlUTDWm0jMnYXPEYt2qGO8rNkr8063jPLJUSLZrE4caUjy8eokk6fyriH-EZY0lo8lDYHr08XxeWb76HXi-NJMuOGtS424zZxohxnouN8rEokCArRmu7Wi8098r_zF-0uzMLHymqbu04qAlifr73liqkGWg3oN8Fo2pLMkY6jy74DjNC0mramDbvstrtrzU24iBa_mUnvSPSE8NkJ-BR776RegrhxcTi05wadGZAf6cnFJIzxMr6tXDRegrhxcOntYMA4kjUfC..; isg=BAQE2246Mc9_roUDKjvHpIAM1YL2HSiHOiTvzB6lz0-SSaYTVixyF1mvieGR0WDf',
    'referer': 'https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E7%BE%BD%E7%BB%92&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.search_manual.0&ssid=s5-e&tab=all',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36',
}



response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.7.4&appKey=12574478&t=1765336479043&sign=9d68fd51c73f8be4af7fa11fb4b9bf02&api=mtop.relationrecommend.wirelessrecommend.recommend&v=2.0&timeout=10000&type=jsonp&dataType=jsonp&callback=mtopjsonp17&data=%7B%22appId%22%3A%2234385%22%2C%22params%22%3A%22%7B%5C%22device%5C%22%3A%5C%22HMA-AL00%5C%22%2C%5C%22isBeta%5C%22%3A%5C%22false%5C%22%2C%5C%22grayHair%5C%22%3A%5C%22false%5C%22%2C%5C%22from%5C%22%3A%5C%22nt_history%5C%22%2C%5C%22brand%5C%22%3A%5C%22HUAWEI%5C%22%2C%5C%22info%5C%22%3A%5C%22wifi%5C%22%2C%5C%22index%5C%22%3A%5C%224%5C%22%2C%5C%22rainbow%5C%22%3A%5C%22%5C%22%2C%5C%22schemaType%5C%22%3A%5C%22auction%5C%22%2C%5C%22elderHome%5C%22%3A%5C%22false%5C%22%2C%5C%22isEnterSrpSearch%5C%22%3A%5C%22true%5C%22%2C%5C%22newSearch%5C%22%3A%5C%22false%5C%22%2C%5C%22network%5C%22%3A%5C%22wifi%5C%22%2C%5C%22subtype%5C%22%3A%5C%22%5C%22%2C%5C%22hasPreposeFilter%5C%22%3A%5C%22false%5C%22%2C%5C%22prepositionVersion%5C%22%3A%5C%22v2%5C%22%2C%5C%22client_os%5C%22%3A%5C%22Android%5C%22%2C%5C%22gpsEnabled%5C%22%3A%5C%22false%5C%22%2C%5C%22searchDoorFrom%5C%22%3A%5C%22srp%5C%22%2C%5C%22debug_rerankNewOpenCard%5C%22%3A%5C%22false%5C%22%2C%5C%22homePageVersion%5C%22%3A%5C%22v7%5C%22%2C%5C%22searchElderHomeOpen%5C%22%3A%5C%22false%5C%22%2C%5C%22search_action%5C%22%3A%5C%22initiative%5C%22%2C%5C%22sugg%5C%22%3A%5C%22_4_1%5C%22%2C%5C%22sversion%5C%22%3A%5C%2213.6%5C%22%2C%5C%22style%5C%22%3A%5C%22list%5C%22%2C%5C%22ttid%5C%22%3A%5C%22600000%40taobao_pc_10.7.0%5C%22%2C%5C%22needTabs%5C%22%3A%5C%22true%5C%22%2C%5C%22areaCode%5C%22%3A%5C%22CN%5C%22%2C%5C%22vm%5C%22%3A%5C%22nw%5C%22%2C%5C%22countryNum%5C%22%3A%5C%22156%5C%22%2C%5C%22m%5C%22%3A%5C%22pc%5C%22%2C%5C%22page%5C%22%3A1%2C%5C%22n%5C%22%3A48%2C%5C%22q%5C%22%3A%5C%22%25E7%25BE%25BD%25E7%25BB%2592%25E6%259C%258D%5C%22%2C%5C%22qSource%5C%22%3A%5C%22manual%5C%22%2C%5C%22pageSource%5C%22%3A%5C%22a21bo.jianhua%2Fa.search_manual.0%5C%22%2C%5C%22channelSrp%5C%22%3A%5C%22%5C%22%2C%5C%22tab%5C%22%3A%5C%22all%5C%22%2C%5C%22pageSize%5C%22%3A%5C%2252%5C%22%2C%5C%22totalPage%5C%22%3A%5C%22100%5C%22%2C%5C%22totalResults%5C%22%3A%5C%22800000%5C%22%2C%5C%22sourceS%5C%22%3A%5C%220%5C%22%2C%5C%22sort%5C%22%3A%5C%22_coefp%5C%22%2C%5C%22bcoffset%5C%22%3A%5C%22%5C%22%2C%5C%22ntoffset%5C%22%3A%5C%22%5C%22%2C%5C%22filterTag%5C%22%3A%5C%22%5C%22%2C%5C%22service%5C%22%3A%5C%22%5C%22%2C%5C%22prop%5C%22%3A%5C%22%5C%22%2C%5C%22loc%5C%22%3A%5C%22%5C%22%2C%5C%22start_price%5C%22%3Anull%2C%5C%22end_price%5C%22%3Anull%2C%5C%22startPrice%5C%22%3Anull%2C%5C%22endPrice%5C%22%3Anull%2C%5C%22itemIds%5C%22%3Anull%2C%5C%22p4pIds%5C%22%3Anull%2C%5C%22p4pS%5C%22%3Anull%2C%5C%22categoryp%5C%22%3A%5C%22%5C%22%2C%5C%22ha3Kvpairs%5C%22%3Anull%2C%5C%22myCNA%5C%22%3A%5C%22rNK%2FIQtESlgBASQIhFNYdf5B%5C%22%2C%5C%22screenResolution%5C%22%3A%5C%221280x800%5C%22%2C%5C%22userAgent%5C%22%3A%5C%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F122.0.6261.95%20Safari%2F537.36%5C%22%2C%5C%22couponUnikey%5C%22%3A%5C%22%5C%22%2C%5C%22subTabId%5C%22%3A%5C%22%5C%22%2C%5C%22np%5C%22%3A%5C%22%5C%22%2C%5C%22clientType%5C%22%3A%5C%22h5%5C%22%2C%5C%22isNewDomainAb%5C%22%3A%5C%22false%5C%22%2C%5C%22forceOldDomain%5C%22%3A%5C%22false%5C%22%7D%22%7D&bx-ua=defaultFY2_load_failed%20with%20timeout%40%40https%3A%2F%2Fs.taobao.com%2Fsearch%40%401765336479051&bx-umidtoken=defaultFY2_load_failed%20with%20timeout%40%40https%3A%2F%2Fs.taobao.com%2Fsearch%40%401765336479051&bx_et=gaOqKE4eEjhVilqSG3CZadlM7r5A51oIgCs1SFYGlijccFbG_3xskiTiDhRNqFpjkOiY7rdyY5NjDxLg_11iADGIOELf61mQu2rkB-QGu5c_n-fAZt4-PbGIOELYlZ0BrX9br-klWRVMjtXlENslSrXDjTVlWgVcSSbgq47Oq1VGnOYlrN7Tj-2DjU0PWgjGstxGZ47OqGfGsji2jHNPWt0JP3P50maFhMYc45VUJiWDkXI8s5APuUSHoRFgsQ7VnQRgiDmNhdYdpITj_7CX8Lfluhcnm_YHUe62gDPfX_sNKw-j5RQyQFAdM6ziiU5V09AVKPVMxU8MdTRS-XCViiv1MFaEcUR2cEdy5P2lgs9PLI5n9oj6FeRN7CntaH8DKhvN4xrOrqK262sQQtbRzMgrzG3BMZmdxsWzBRBAeaSIoq2TBtbRzMgrzReOh7QPAq0c.',
    cookies=cookies,
    headers=headers,
)

print(response.text)