'''
Author: Python Crawler Developer crawler@example.com
Date: 2025-12-16 17:50:40
LastEditors: Python Crawler Developer crawler@example.com
LastEditTime: 2025-12-26 15:51:20
FilePath: \test\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# 配置chrome文件的位置。
from DrissionPage import ChromiumOptions
import os
#请改为你电脑内chrome可执行文件路径
path = r'C:\users\Administrator\AppData\LocaL\Goog'
ChromiumOptions().set_browser_path(path).save()


from DrissionPage import ChromiumPage,Chromium
import os
import pandas as pd
import json

# 实例化浏览器
dp = ChromiumPage()

# 监听网络请求
dp.listen.start('getAttractionList')
dp.get(f'https://you.ctrip.com/sight/shanghai2/s0-p1.html')
def main():
    # 获取总页数
    all_page = int(dp.ele('.ant-pagination-item ant-pagination-item-300').text)
    print(f"总页数: {all_page}")
    for i in range(2, all_page):  
        print(f"\n=== 开始处理第 {i} 页 ===")
        try:
            # 点击下一页
            dp.ele('.anticon anticon-right').click(by_js=True)
            # 等待页面加载完成
            dp.wait(5)
            res = dp.listen.wait()  # 等待并获取一个数据包
            print(res.url)
            json_data = res.response.body
            print("成功获取JSON数据")
            print(json_data)
            print(f"原始数据类型: {type(json_data).__name__}")
            # 检查数据类型，处理不同情况
            if isinstance(json_data, bytes):
                # 如果是bytes类型，先转换为字符串再解析
                json_data = str(json_data, encoding='utf-8')
                json_data = json.loads(json_data)
            elif isinstance(json_data, str):
                # 如果是字符串类型，直接解析
                json_data = json.loads(json_data)
            # 如果已经是dict类型，直接使用
            # 准备数据列表
            data = []
            if isinstance(json_data, dict):
                if 'attractionList' in json_data:
                    for item in json_data['attractionList']:
                        # 提取需要的字段，使用get()方法避免键不存在的错误
                        card = item.get('card', {})
                        poiName = card.get('poiName', '')
                        price = card.get('price', '')
                        distanceStr = card.get('distanceStr', '')
                        zoneName = card.get('zoneName', '')
                        coverImageUrl = card.get('coverImageUrl', '')
                        dynamicCoverImageUrl = card.get('dynamicCoverImageUrl', '')
                        detailUrl = card.get('detailUrl', '')
                        tagNameList = card.get('tagNameList', [])
                        otherTagList = card.get('otherTagList', []) 
                        
                        # 处理tagNameList，确保元素都是字符串
                        tagNames = []
                        for tag in tagNameList:
                            if isinstance(tag, dict):
                                tagNames.append(tag.get('name', '') or tag.get('value', ''))
                            else:
                                tagNames.append(str(tag))
                        
                        # 处理otherTagList，提取name字段
                        otherTagNames = []
                        for tag in otherTagList:
                            if isinstance(tag, dict):
                                otherTagNames.append(tag.get('name', '') or tag.get('value', ''))
                            else:
                                otherTagNames.append(str(tag))
                        
                        # 添加到数据列表
                        data.append({
                            '名称': poiName,
                            '价格': price,                        
                            '链接': detailUrl,
                            '地区': f"{zoneName} {distanceStr}",
                            '图片地址': coverImageUrl,
                            '动态图片地址': dynamicCoverImageUrl,
                            '标签': ', '.join(tagNames),
                            '其他标签': ', '.join(otherTagNames)
                        })
                    
                    print(f"找到 {len(json_data['attractionList'])} 个景点")
                    # 创建DataFrame并保存
                    if data:
                        df = pd.DataFrame(data)
                        # 保存到CSV文件
                        # 检查文件是否存在，不存在则写入表头
                        header = not os.path.exists('shanghai_sights.csv')
                        df.to_csv(f'shanghai_sights.csv', mode='a', header=header, index=False, encoding='utf-8-sig')
                        print(f"第 {i} 页数据已保存到CSV文件")
                else:
                    print(f"第 {i} 页JSON中没有attractionList字段")
            else:
                print(f"第 {i} 页响应不是预期的JSON格式，类型: {type(json_data).__name__}")
                
        except Exception as e:
            print(f"处理第 {i} 页时出错: {e}")
            continue


    # 关闭浏览器
    dp.close()



if __name__ == '__main__':
    main()














