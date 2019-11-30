# coding: utf-8
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def _simple_iou_score(gt_image, pre_image):
   intersection = np.logical_and(gt_image, pre_image)
   union = np.logical_or(gt_image, pre_image)
   iou_score = np.sum(intersection) / np.sum(union)
   return iou_score

#读取原始图像灰度颜色
img = cv2.imread('/Users/didi/Desktop/car-images/1.jpeg', 0)
print(img.shape)
print(matplotlib.matplotlib_fname())
#获取图像高度、宽度
rows, cols = img.shape[:]

#图像二维像素转换为一维
data = img.reshape((rows * cols, 1))
data = np.float32(data)



#定义中心 (type,max_iter,epsilon)
criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

#设置标签
flags = cv2.KMEANS_RANDOM_CENTERS

#K-Means聚类 聚集成4类
compactness, labels, centers = cv2.kmeans(data, 4, None, criteria, 10, flags)

#生成最终图像
dst = labels.reshape((img.shape[0], img.shape[1]))




#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示图像
titles = [u'origin-image', u'cluster-image']
images = [img, dst]
for i in range(2):
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray'),
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()




