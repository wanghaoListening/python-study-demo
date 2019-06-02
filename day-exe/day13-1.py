"""
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图
像压缩和图像处理等各种操作。可以使用下面的命令来安装Pillow。

"""

#Pillow中最为重要的是Image类，读取和处理图像都要通过这个类来完成

from PIL import Image

image = Image.open('/Users/admin/xy.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()

