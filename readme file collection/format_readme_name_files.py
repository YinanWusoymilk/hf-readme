import os
import shutil

# 定义原始和目标文件夹路径
original_folder_path = r"C:\SMU-SCIS-Project\what makes a hugging face model popular\5 May new collection of data\03 - readme collection\readmes"
target_folder_path = r"C:\SMU-SCIS-Project\what makes a hugging face model popular\5 May new collection of data\03 - readme collection\format-readmes"

# 创建目标文件夹如果它不存在
if not os.path.exists(target_folder_path):
    os.makedirs(target_folder_path)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(original_folder_path):
    # 检查文件名是否含有_README
    if '_README' in filename:
        # 创建新文件名
        new_filename = filename.replace('_README', '')
        # 定义原始和新的文件路径
        original_file_path = os.path.join(original_folder_path, filename)
        new_file_path = os.path.join(target_folder_path, new_filename)
        # 移动并重命名文件
        shutil.move(original_file_path, new_file_path)

print("所有文件已经重命名并移动到新的目录。")
