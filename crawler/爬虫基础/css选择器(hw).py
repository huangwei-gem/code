
# 基础语法
# 选择器	示例	说明
# 标签选择器	'div'	所有div元素
# 类选择器	'.product'	class="product"的元素
# ID选择器	'#header'	id="header"的元素
# 属性选择器	'[href]'	所有带href属性的元素
# 组合选择器	'div.product'	div标签且class="product"
# 后代选择器	'div p'	div内部的所有p元素



books = []
# 提取所有图书信息
# 选择所有 <article class="product_pod"> 元素
for book in soup.select('article.product_pod'):
    title = book.h3.a['title']
    # 即选择 <p class="price_color"> 元素
    price = book.select_one('p.price_color').text
    # 选择 <p class="star-rating"> 元素，这类元素通常用于显示商品评分
    rating = book.select_one('p.star-rating')['class'][1]
    link = base_url + '/' + book.h3.a['href']


# 获取所有 ID= "s-top-left" 的元素
items = soup.select('#s-top-left')
# 获取所有 div中有ID= "s-top-left" 的元素
items = soup.select('div#s-top-left')


# 获取所有 a标签中有class="mnav1" 的元素
items = soup.select('a.mnav1')
# 选择具有class属性的a标签
items = soup.select('a[class]')


# 选择id为wrapper下的子一代为div子二代为a的标签，注意表达式中相邻标签必须为父子关系，即id为wrapper的标签的儿子节点为div，孙子节点为a标签
items = soup.select('#wrapper > div > a')
# 选择body标签下的li标签的span标签，其中body和li并不是直接父子关系，但是li是body的子孙节点，所以用空格表示即可
items = soup.select('body li span')



# 选择具有href属性的标签
items = soup.select('[href]')
# 选择所有a标签中具有href属性的标签
items = soup.select('a[href]')
for item in items:
    print(item)
# 选择所有a标签中href属性值为https://haokan.baidu.com/?sfrom=baidu-top的标签
items = soup.select('[href="https://haokan.baidu.com/?sfrom=baidu-top"]')
# 选择以hao123.com结尾的a标签
items = soup.select('a[href$="hao123.com"]')
# 选择href属性包含‘www’的a标签
items = soup.select('a[href*="www"]')



# 选择 id为s-top-left的div元素 或者 id为hotsearch-content-wrapper的ul元素
items = soup.select('div#s-top-left, ul#hotsearch-content-wrapper')







