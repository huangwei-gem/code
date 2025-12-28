# -*- coding:utf-8 -*-
import requests
import re

"""分析页面，正则查找，返回所需要的值"""
def analyse_page(response):
    # .*? 是非贪婪的，即匹配最少数量的就成了
    # (.*) 是捕获匹配包括换行在内的所有字符
    pattern = re.compile("<dd>.*?board-index.*?(\d+)</</i>.*?title=(.*?)>.*?star.*?(.*?)</p>.*?setime.*?"
                         + "(.*?)</p>.*?integer.*?(.*?)</</i>.*?fraction.*?(.*?)</</i>", re.S)
    lists = re.findall(pattern, response)
    for item in lists: # 循环页找到的所有元素
        yield { # yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始
            'Number': item[0],
            'Movie_name': item[1],
            'Actors': item[2].strip()[3:],
            'Datetime': item[3].strip()[5:],
            'Score': item[4] + item[5]
        }

"""获取页面内容"""
# 预加载模式(这个是是最常用的)
obj = re.compile(r'<div><a href="(?P<url>.*?)">(?P<txt>.*?)</a></div>')
result = obj.finditer(s)
for item in result:
    url = item.group("url")
    txt = item.group("txt")
    print(url,txt)


# 匹配所有符合条件的内容
result= re.findall(r"\d+","我今天买了2个榴莲，花了200元。")
print(result)


# 搜索符合条件的第一个内容
result = re.search(r"\d+","我今天买了2个榴莲，花了200元。") 
print(result.group())

