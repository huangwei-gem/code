#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试使用ddddocr进行字体识别的功能
"""

import requests
import re
from demo import build_font_mapping

def download_test_font():
    """下载测试用的字体文件"""
    # 这里应该是一个真实的请求，为了测试我们使用现有的字体文件
    # 如果你有一个字体文件的URL，可以取消下面的注释并使用它
    
    '''
    font_url = "YOUR_FONT_URL_HERE"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(font_url, headers=headers)
    with open('test_font.woff', 'wb') as f:
        f.write(response.content)
    '''
    
    # 如果已经有font.woff文件，我们复制它作为测试文件
    try:
        with open('font.woff', 'rb') as src, open('test_font.woff', 'wb') as dst:
            dst.write(src.read())
        print("已复制现有字体文件作为测试文件")
        return True
    except FileNotFoundError:
        print("未找到字体文件，请先运行main.py以获取字体文件")
        return False

def test_ocr_mapping():
    """测试OCR字体映射功能"""
    print("开始测试OCR字体映射功能...")
    
    if not download_test_font():
        return
    
    # 使用新的OCR方法构建字体映射
    font_mapping = build_font_mapping('test_font.woff')
    print("字体映射结果:")
    for char, digit in font_mapping.items():
        print(f"  '{char}' -> '{digit}'")
    
    print(f"\n总共识别出 {len(font_mapping)} 个字符映射")

if __name__ == "__main__":
    test_ocr_mapping()