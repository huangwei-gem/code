#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查翻译文件状态的脚本
从 translation_manifest.txt 中读取文件映射关系，
检查对应的文件是否已经在 examples_chinese/ 中存在
"""

import os
import re
from pathlib import Path

def parse_translation_manifest(manifest_path):
    """解析翻译清单文件"""
    file_mappings = []
    
    with open(manifest_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配文件映射关系（跳过注释和空行）
    pattern = r'^-\s*([^\s]+)\s*->\s*([^\s]+)(?:\s*✓)?$'
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('-') and '->' in line and not line.startswith('#'):
            match = re.match(pattern, line)
            if match:
                source_file = match.group(1)
                target_file = match.group(2).replace('✓', '').strip()
                file_mappings.append((source_file, target_file))
    
    return file_mappings

def check_file_exists(base_path, relative_path):
    """检查文件是否存在"""
    full_path = os.path.join(base_path, relative_path)
    return os.path.exists(full_path)

def main():
    # 基础路径
    base_dir = r"c:\code\crawler\crawl4AI\crawl4ai-main"
    manifest_path = os.path.join(base_dir, "translation_manifest.txt")
    examples_chinese_dir = os.path.join(base_dir, "examples_chinese")
    
    # 输出文件
    output_file = os.path.join(base_dir, "translation_check_result.txt")
    
    print("=== 翻译文件状态检查 ===\n")
    
    # 解析翻译清单
    file_mappings = parse_translation_manifest(manifest_path)
    print(f"找到 {len(file_mappings)} 个文件映射关系\n")
    
    # 统计信息
    existing_files = []
    missing_files = []
    
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.write("=== 翻译文件状态检查结果 ===\n\n")
        
        # 检查每个文件
        for source_file, target_file in file_mappings:
            # 构建完整的源文件路径（相对于 docs/examples）
            source_full_path = os.path.join(base_dir, "docs", "examples", source_file)
            target_full_path = os.path.join(examples_chinese_dir, target_file)
            
            # 检查源文件是否存在
            if not os.path.exists(source_full_path):
                status_msg = f"[ERROR] 源文件不存在: {source_file}"
                print(status_msg)
                out_f.write(status_msg + "\n")
                continue
            
            # 检查目标文件是否存在
            if check_file_exists(examples_chinese_dir, target_file):
                status = "[OK]"
                existing_files.append((source_file, target_file))
            else:
                status = "[X]"
                missing_files.append((source_file, target_file))
            
            status_msg = f"{status} {source_file} -> {target_file}"
            print(status_msg)
            out_f.write(status_msg + "\n")
        
        # 打印统计信息
        out_f.write(f"\n=== 统计结果 ===\n")
        out_f.write(f"已存在文件: {len(existing_files)}\n")
        out_f.write(f"缺失文件: {len(missing_files)}\n")
        out_f.write(f"总计: {len(existing_files) + len(missing_files)}\n")
        
        # 打印缺失文件列表
        if missing_files:
            out_f.write(f"\n=== 缺失文件列表 ===\n")
            for source_file, target_file in missing_files:
                out_f.write(f"[X] {source_file} -> {target_file}\n")
    
    print(f"\n=== 统计结果 ===")
    print(f"已存在文件: {len(existing_files)}")
    print(f"缺失文件: {len(missing_files)}")
    print(f"总计: {len(existing_files) + len(missing_files)}")
    print(f"\n详细结果已保存到: {output_file}")
    
    return existing_files, missing_files

if __name__ == "__main__":
    main()