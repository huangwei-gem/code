```python
# 准备一个etree将html源码加载到里面去
tree=etree.HTML(response)
# 先写出第一个房源的信息
 
title=tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/div[1]/h3/text()')[0]
 
structure=''.join(tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[1]/p[1]/span/text()'))
# 使用''连接字符串的每个字符
square=tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[1]/p[2]/text()')[0].strip()
# 使用strip去除两端空格
 
house_name=tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[2]/p[1]/text()')[0]
 
place='-'.join(tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[2]/p[2]/span/text()'))
 
detail='/'.join(tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[3]/span/text()'))
 
total_price=''.join(tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[2]/p[1]/span/text()'))
 
avg_price=tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[2]/p[2]/text()')[0]



```

一般的步骤就是：先解析数据，然后拿到大的xml，再循环，拿到每一个小的内容就行了


