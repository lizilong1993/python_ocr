import os, sys
from joblib import Parallel, delayed
import multiprocessing
# 导入easyocr
import easyocr

# 读取文件夹中的文件
path = './images/' #待读取文件的文件夹绝对地址
files = os.listdir(path) #获得文件夹中所有文件的名称列表

# 创建reader对象
reader = easyocr.Reader(['ch_sim','en']) 

myocr = open('result.txt', mode = 'a',encoding='utf-8')

for name in files:
    # 读取图像
    result = reader.readtext(f'./images/{name}')
    # 结果
    for i in range(len(result)):
        text = result[i]
        print(text[1], file=myocr)
myocr.close()

# # 并行处理会导致输出文本顺序不对
# def ocr(name):
#     # 读取图像
#     result = reader.readtext(f'./images/{name}')
#     # 保存结果 
#     for i in range(len(result)):
#         text = result[i]
#         print(text[1], file=myocr)


# num_cores = multiprocessing.cpu_count()
# results = Parallel(n_jobs=num_cores, prefer="threads")(delayed(ocr)(name) for name in files)
# myocr.close()