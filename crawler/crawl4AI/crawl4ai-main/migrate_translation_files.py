#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移翻译文件的脚本
基于检查结果文件中的[X]标记，将缺失的文件从docs/examples/复制到examples_chinese/并创建对应的目录结构
"""

import os
import shutil
import re

def parse_check_result_file(result_file_path):
    """解析检查结果文件，获取需要迁移的文件映射"""
    file_mappings = []
    
    with open(result_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        # 查找标记为[X]的行
        if line.startswith('[X]') and '->' in line:
            # 移除[X]标记并解析文件映射
            content = line[3:].strip()  # 移除[X]和空格
            if '->' in content:
                parts = content.split('->')
                source_file = parts[0].strip()
                target_file = parts[1].strip()
                file_mappings.append((source_file, target_file))
    
    return file_mappings

def migrate_files(file_mappings, source_base, target_base):
    """迁移文件"""
    migrated_count = 0
    skipped_count = 0
    error_count = 0
    
    for source_file, target_file in file_mappings:
        source_path = os.path.join(source_base, source_file)
        target_path = os.path.join(target_base, target_file)
        
        # 检查源文件是否存在
        if not os.path.exists(source_path):
            print(f"[ERROR] 源文件不存在: {source_path}")
            error_count += 1
            continue
        
        # 检查目标文件是否已存在
        if os.path.exists(target_path):
            print(f"[SKIP] 目标文件已存在: {target_path}")
            skipped_count += 1
            continue
        
        # 创建目标目录
        target_dir = os.path.dirname(target_path)
        os.makedirs(target_dir, exist_ok=True)
        
        try:
            # 复制文件
            shutil.copy2(source_path, target_path)
            print(f"[SUCCESS] 已迁移: {source_file} -> {target_file}")
            migrated_count += 1
        except Exception as e:
            print(f"[ERROR] 迁移失败: {source_file} -> {e}")
            error_count += 1
    
    return migrated_count, skipped_count, error_count

def main():
    # 基础路径
    result_file_path = 'translation_check_result.txt'
    source_base = 'docs/examples'
    target_base = 'examples_chinese'
    
    print("=== 开始迁移翻译文件 ===")
    
    # 解析检查结果文件
    print("正在解析检查结果文件...")
    file_mappings = parse_check_result_file(result_file_path)
    print(f"找到 {len(file_mappings)} 个需要迁移的文件")
    
    if not file_mappings:
        print("没有找到需要迁移的文件")
        return
    
    # 迁移文件
    print("\n开始迁移文件...")
    migrated, skipped, errors = migrate_files(file_mappings, source_base, target_base)
    
    # 统计结果
    print(f"\n=== 迁移完成 ===")
    print(f"成功迁移: {migrated} 个文件")
    print(f"跳过已存在: {skipped} 个文件")
    print(f"错误: {errors} 个文件")
    print(f"总计: {migrated + skipped + errors} 个文件")

if __name__ == '__main__':
    main()