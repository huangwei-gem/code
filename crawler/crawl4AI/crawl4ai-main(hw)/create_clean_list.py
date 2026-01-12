#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建干净的翻译清单文件
"""

import os

def main():
    # 读取所有Python文件列表
    with open('all_python_files_clean.txt', 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip()]
    
    # 去重
    unique_files = list(set(files))
    unique_files.sort()
    
    # 写入干净的清单文件
    with open('translation_bilingual_list_all.txt', 'w', encoding='utf-8') as f:
        f.write("# 需要添加中英双注释的文件清单\n")
        f.write("# 格式：文件路径,状态（pending/done）\n\n")
        
        for file_path in unique_files:
            f.write(f"{file_path},pending\n")
    
    print(f"已创建干净的清单文件，包含 {len(unique_files)} 个文件")

if __name__ == "__main__":
    main()