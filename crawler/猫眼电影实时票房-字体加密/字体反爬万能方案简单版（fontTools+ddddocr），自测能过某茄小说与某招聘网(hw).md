#### 字体反爬万能方案简单版（fontTools+ddddocr）

## 前言

这里不会从零开始去展示站点字体反爬的破解流程，只是截取了部分混淆文本验证破解成功。一般来说对于自定义字体反爬都是使用fontTools将字体文件转成xml，然后多次对比发现不变的映射规律然后得到映射字典，但根据笔者的过往经验，有些站点的字体文件实在是很难发现不变的规律，搞起来太耗时了。这个时候要是有一个能传入一个字体文件就得到映射的话就完美了，来来来，这就引入正文。

## 万能方案简单版

### 大致思路

  1. 使用`fontTools`的`getBestCmap`方法得到所有字体的`最佳unicode cmap字典`
  2. 创建`Image`对应与对应字体的`unicode`匹配上将其转换为规则的方块
  3. 使用`ddddocr`识别`Image`方块得到结果
  4. 组合全部`unicode`和识别结果就构成映射词典了



### 代码程序
    
    
    import io
    import os
    import re
    
    import ddddocr
    from PIL import ImageDraw, ImageFont, Image
    from fontTools.ttLib import TTFont
    
    
    class UniversalFontRecognition(object):
        ocr = None
    
        def __init__(self, font_path):
            self.font_path = font_path
            self.ocr = ddddocr.DdddOcr(show_ad=False)
    
        def font_to_xml(self, xml_path=None):
            if not xml_path:
                
                filename_with_ext = os.path.basename(self.font_path)
                filename_only = os.path.splitext(filename_with_ext)[0]
                xml_path = f'{filename_only}.xml'
            font = TTFont(self.font_path)
            font.saveXML(xml_path)
    
        def font_to_img(self, char_list, img_size=100, font_ratio=0.7):
            normal_dict = {}
    
            for char in char_list:
                char_code = chr(char).encode().decode()
                img = Image.new('RGB', (img_size, img_size), 255)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(self.font_path, int(img_size * font_ratio))
                x, y = draw.textsize(char_code, font=font)
                draw.text(((img_size - x) // 2, (img_size - y) // 2), char_code, font=font, fill=0)
                img_bytes = io.BytesIO()
                img.save(img_bytes, format='JPEG')
                image_bytes = img_bytes.getvalue()
                word = self.ocr.classification(image_bytes)
                normal_dict[char] = word[0] if word else ''
    
            return normal_dict
    
        def crack(self):
            """ 最终转成的都是unicode的映射 {unicode：识别结果}, 调用时需要将文本转成unicode """
            with open(self.font_path, 'rb') as fr:
                font_bytes = fr.read()
            with TTFont(io.BytesIO(font_bytes)) as font_parse:  
                u_d = font_parse.getBestCmap()  
            return self.font_to_img(list(u_d.keys()))
    

### 过程演示

![在这里插入图片描述](attachments/veMIOkLPdZVstMZqU8vOO34rb4iQq3N5)  
![在这里插入图片描述](attachments/9e0L6WNynUq7sT7IzAyrTEtBrVsXHsLw)

### 案例展示

#### 某茄小说
    
    
    def crack_recognite_fqxs():
        u_f_r = UniversalFontRecognition(r"dc027189e0ba4cd-700.woff2")
        recognition_result = u_f_r.crack()
        print('原始文本: 阴沉沉，易冷坐江办室，冰冷，脸模糊，漂浮九霄云。')
        print('正确结果: 天阴沉沉的，易冷坐在江东理工大学人事处办公室里，心和外面的天气一样冰冷，工作人员的脸变得模糊，声音也如同漂浮在九霄云外。')
        test_text = '阴沉沉，易冷坐江办室，冰冷，脸模糊，漂浮九霄云。'
        print('识别结果: {}'.format(''.join([recognition_result.get(ord(s), s) for s in test_text])))
    

![在这里插入图片描述](attachments/mx7B9Nbbui2246XsvpIRc6qtvDZaEumB)

#### 某点小说
    
    
    def crack_recognite_qidian():
        u_f_r = UniversalFontRecognition(r"myhHpgyU.woff")
        recognition_result = u_f_r.crack()
        test_text = '&#100486;&#100483;&#100484;&#100479;&#100482;&#100484;万'
        prep_map = []
        for text in test_text.split(';'):
            if '&#' in text:
                map_text = recognition_result.get(int(text.replace('&#', '')))
                if not map_text:
                    map_text = '.'
                prep_map.append(map_text)
            else:
                prep_map.append(text)
    
        print('原始文本: &#100486;&#100483;&#100484;&#100479;&#100482;&#100484;万')
        print('正确结果: 279.19万')
        print('识别结果: {}'.format(''.join(prep_map)))
    

![在这里插入图片描述](attachments/na3G7puDxadLhaXOxPdKnqK6J82nDD3l)

#### 某直聘网
    
    
    def crack_recognite_boss():
        u_f_r = UniversalFontRecognition(r"3kovsijnt11693967587313.woff2")
        recognition_result = u_f_r.crack()
        for rec in recognition_result:
            if recognition_result[rec] == 'o':
                recognition_result[rec] = '0'
        test_text = '-K'
        print('原始文本: -K')
        print('正确结果: 15-30K')
        print('识别结果: {}'.format(''.join([recognition_result.get(ord(s), s) for s in test_text])))
    

![在这里插入图片描述](attachments/R5LdoOCEy44pOEXdt9bZZmnqH5KqILuq)

#### 某点评

离谱，笔者打开发现它竟然没有字体反爬，不知道为啥，不过拿到字体文件也是能得到映射字典的  
![在这里插入图片描述](attachments/fGp9Uvu6caqXvg4c9gynPtsCIsEGXeiR)

### 不足与优化

#### 不足

  1. 大家看某直聘网和某点小说，`ddddocr`有可能会吧`0`是被`o`，没法识别`.`，笔者是在得到识别结果后二次处理的，也算是一种解决方案吧
  2. 如果字体文件字体太多会导致识别结果比较慢，如果是遇到动态字体反爬的，可能需要结合业务情况看看进行优化了。  
识别某点评602个字体花了差不多3s  
![在这里插入图片描述](attachments/epDpxguIIS9GLilvy979q7FtD029h08f)



#### 优化

针对第一点如果能像笔者那样二次处理解决的那还好，不然的话就要自己训练识别模型了，毕竟这样能大大提高识别结果；而第二点的话，如果只有数英就还好，包含文字的话可以考虑多线程或者协程识别。

## 总结

以上是笔者结合自己的经验和网上经验实践出来的，不能保证能应用到所有站点，如果有更好的方案或者过不了的站点欢迎大家提供给笔者，感谢~