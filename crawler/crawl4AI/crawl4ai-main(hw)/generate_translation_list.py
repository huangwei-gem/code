import os
import json

# 定义源目录和目标目录
source_dir = "docs/examples"
target_dir = "docs/examples_chinese"

# 初始化待处理清单
todo_list = {
    "未翻译文件": [],
    "待重命名文件夹": [],
    "待重命名.py 文件": []
}

# 遍历源目录结构
def traverse_directory(current_path):
    # 获取当前相对路径
    relative_path = os.path.relpath(current_path, source_dir)
    
    # 检查目标目录中是否存在对应文件夹
    target_path = os.path.join(target_dir, relative_path)
    if not os.path.exists(target_path):
        # 如果目标文件夹不存在，添加到待重命名文件夹列表
        todo_list["待重命名文件夹"].append(relative_path)
        # 创建目标文件夹
        os.makedirs(target_path, exist_ok=True)
    
    # 遍历当前目录中的文件和子目录
    for item in os.listdir(current_path):
        item_path = os.path.join(current_path, item)
        item_relative_path = os.path.join(relative_path, item)
        
        if os.path.isdir(item_path):
            # 递归处理子目录
            traverse_directory(item_path)
        else:
            # 处理文件
            target_item_path = os.path.join(target_dir, item_relative_path)
            if not os.path.exists(target_item_path):
                # 如果目标文件不存在，添加到未翻译文件列表
                todo_list["未翻译文件"].append(item_relative_path)
            
            # 检查是否为 .py 文件，需要重命名
            if item.endswith(".py"):
                todo_list["待重命名.py 文件"].append(item_relative_path)

# 执行遍历
traverse_directory(source_dir)

# 生成待处理清单文件
with open("translation_todo_list.json", "w", encoding="utf-8") as f:
    json.dump(todo_list, f, ensure_ascii=False, indent=4)

print("待处理清单已生成：translation_todo_list.json")
print("\n待处理清单内容：")
for category, items in todo_list.items():
    print(f"\n{category} ({len(items)} 个):")
    for item in items:
        print(f"  - {item}")
