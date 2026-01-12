# 为什么有些网页只能在客户端打开，在网页打开不行，因为他限制了，所以说，绕过客户端检测，就是在客户端打开，在网页打开不行
# 那么他是怎么判断是不是网页的呢，很简单，他是通过检测UA来判断的，我们只要检测一下UA就行

# 这是修改UA的插件，具体修改成什么样，可以去网上找现成的，或者让】AI帮我们生成一份也可以
https://www.crxsoso.com/webstore/detail/bhchdcejhohfmigjafbampogmaanbfkg

# 用requests模块发送请求，设置headers参数，将UA设置为Chrome或者平板或者安卓之类的UA
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
response = requests.get('https://www.baidu.com', headers=headers)
print(response.text)