# import os
# import json
#
# #存储txt的路径
# Labels_txt_Dir = r'/Users/shineber/Desktop/Master_Period/Contest/CAAI_drone_detection/result/final_labels/V2.txt'
# #读取txt，并获取（图片id、类别id、bbox、score）
# with open(Labels_txt_Dir, 'r') as file:
#     # 逐行读取文件
#     for line in file:
#         # 去除行尾的换行符，并分割字符串为列表
#         elements = line.strip().split()
#         # 检查是否确实有七个元素
#         if len(elements) == 7:
#             # 将字符串转换为相应的数据类型（例如，浮点数和整数）
#             image_id = int(elements[0])
#             category_id = int(elements[1])
#             x = round(float(elements[2]), 1)
#             x = float(elements[2])
#             y = float(elements[3])
#             width = float(elements[4])
#             height = float(elements[5])
#             score = float(elements[6])
#             #将这七个元素制作成字典
#             dic = {"image_id":,"category_id":,"bbox":,"score":}
#         else:
#             print(f"警告：行 '{line.strip()}' 不包含七个元素")
#     print(image_id, category_id, x, y, width, height, score)



# import json
# #存储txt的路径
# Labels_txt_Dir = r'/Users/shineber/Desktop/Master_Period/Contest/CAAI_drone_detection/result/final_labels/V2.txt'
# #定义一个data_list，存放json每个object
# data_list = []
# #定义一个标志，用于检测未识别到的图片
# image_id_list = []
# #读取txt，并获取（图片id、类别id、bbox、score）
# with open(Labels_txt_Dir, 'r') as file:
#     # 逐行读取文件
#     for line in file:
#         # 去除行尾的换行符，并分割字符串为列表
#         elements = line.strip().split()
#         # 检查是否确实有七个元素
#         if len(elements) == 7:
#             # 将字符串转换为相应的数据类型（例如，浮点数和整数）
#             image_id = int(elements[0])
#             category_id = int(elements[1])
#             x = round(float(elements[2]), 1)
#             y = round(float(elements[3]), 1)
#             width = round(float(elements[4]), 1)
#             height = round(float(elements[5]), 1)
#             score = round(float(elements[6]), 2)
#             #判断一下哪张image_id没有检测结果
#             image_id_list.append(image_id)
#             #制作字典,用于JSON生成
#             dic = {"image_id":image_id,"category_id":category_id,"bbox":[x,y,width,height],"score":score}
#             data_list.append(dic)
#         else:
#             print(f"警告：行 '{line.strip()}' 不包含七个元素")
# image_id_set = set(image_id_list)
#
# print("Read Done, Conver to Json Begin")
# json_string = json.dumps(data_list, indent=4)
# # 将JSON字符串写入文件
# with open('output.json', 'w') as file:
#     file.write(json_string)






















#################V2####################
# 假设labels.txt的格式是每行包含image_id, category_id, x, y, width, height, score
# 并且它们之间由空格分隔
# 初始化一个包含所有可能image_id的集合
all_possible_image_ids = set(range(1001))  # 从0到1000

# 初始化一个空列表来存储最终的字典
label_dicts = []

# 读取labels.txt文件并收集存在的image_id
Labels_txt_Dir = '/Users/shineber/Desktop/Master_Period/Contest/CAAI_drone_detection/result/final_labels/V3.txt'  # 替换为你的txt文件路径
existing_image_ids = set()

with open(Labels_txt_Dir, 'r') as file:
    for line in file:
        elements = line.strip().split()
        if len(elements) == 7:
            image_id = int(elements[0])
            existing_image_ids.add(image_id)

            # 提取其他信息并添加到字典中
            category_id = int(elements[1])
            x = round(float(elements[2]), 1)
            y = round(float(elements[3]), 1)
            width = round(float(elements[4]), 1)
            height = round(float(elements[5]), 1)
            score = round(float(elements[6]), 2)
            label_dicts.append({
                "image_id": image_id,
                "category_id": category_id,
                "bbox": [x, y, width, height],
                "score": score
            })

        # 找出不存在的image_id并添加到字典列表中
for image_id in all_possible_image_ids - existing_image_ids:
    label_dicts.append({
        "image_id": image_id,
        "category_id": None,
        "bbox": None,
        "score": None
    })

# 将最终的字典列表写入JSON文件
with open('output_V3.json', 'w') as file:
    import json

    json.dump(label_dicts, file, indent=4)

print("Done")
