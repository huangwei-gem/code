import os
import shutil

source_dir = r'C:\Users\35796\Documents\code\crawler\downloaded_videos'
target_dir = r'F:\downloaded_videos'

if not os.path.exists(source_dir):
    print(f"错误：源文件夹不存在: {source_dir}")
    exit(1)

if not os.path.exists(target_dir):
    print(f"错误：目标文件夹不存在: {target_dir}")
    exit(1)

source_files = set(os.listdir(source_dir))
target_files = set(os.listdir(target_dir))

missing_files = source_files - target_files

print(f"源文件夹文件数量: {len(source_files)}")
print(f"目标文件夹文件数量: {len(target_files)}")
print(f"需要复制的文件数量: {len(missing_files)}")

if not missing_files:
    print("所有文件已同步，无需复制。")
else:
    print("\n开始复制文件...")
    for filename in missing_files:
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)
        try:
            shutil.copy2(source_path, target_path)
            print(f"已复制: {filename}")
        except Exception as e:
            print(f"复制失败 {filename}: {e}")
    print("\n文件同步完成！")
