import pandas as pd
import jieba, wordcloud
# import numpy as np
# from PIL import Image
# mask = np.array(Image.open('112233.png'))
rd = pd.read_csv('爬取抖音731电影评论.csv')
data = ' '.join([str(i) for i in rd['评论']])
print(data)
string = ' '.join(jieba.lcut(data))
print(string)

cyt = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color="white",
    font_path="msyh.ttc",
    # max_words=100,
    # max_font_size=50,
    stopwords={'我','你','的','这','流泪','发怒','感谢','炸弹','这','个','了','都','这个','看','愤怒','好','是','不','我们','去','为什么','电影','现在','真实','有','就','玫瑰','爱心','好看',},    # 设置停用词
    # mask=mask
).generate(string)
cyt.to_file('731电影评论词云.png')