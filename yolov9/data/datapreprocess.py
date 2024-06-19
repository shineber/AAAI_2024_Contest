# import os
 
# # 设置目标文件夹路径
# folder_path = './images/val2017'
# # 设置输出文件路径
# output_file = 'val.txt'
 
# # 遍历文件夹并写入文件列表到txt
# with open(output_file, 'w') as file_list_txt:
#     for dirpath, dnames, fnames in os.walk(folder_path):
#         for file in fnames:
#             file_list_txt.write(os.path.join(dirpath, file) + '\n')


import os  
  
# 定义要遍历的目录  
dir = './images/val'  
  
# 定义保存文件名的文件  
filename = "val.txt"  
  
# 打开文件以写入文件名  
with open(filename, "w") as f:  
    # 遍历目录中的所有文件  
    sorted_list = sorted(os.listdir(dir), key=lambda x: x.lower())
    for filename in sorted_list:  
        # 获取文件的完整路径  
        filepath = os.path.join(dir, filename) 
        print(filepath)    
        # 判断文件是否是一个普通文件（而不是目录或特殊文件）
        if os.path.isfile(filepath):  
            # 将文件名写入文件  
            f.write(filepath + "\n")