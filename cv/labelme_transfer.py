import os
from glob import glob
# 将保存的 json 文件转换为 image 以及 label 图像
json_files = glob(os.path.join(r"/Users/didi/Desktop/car-images/", "*.json"))
for json_file in json_files:
    os.system(f"labelme_json_to_dataset {json_file} -o {''.join(json_file.split('.')[:-1])}")