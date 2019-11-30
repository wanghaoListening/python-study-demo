
import os
import cv2
import numpy as np


kmeans_cluster_path = "/Users/didi/Desktop/kmeans-cluster/"

slic_cluster_path = "/Users/didi/Desktop/slic-cluster/"

label_img_path = "/Users/didi/Desktop/car-images/"



def ap_function(kmeans, gt):
    row = kmeans.shape[0]
    column = kmeans.shape[1]
    u = 0
    p = 0
    for i in range(row):
        for j in range(column):
            if kmeans[i][j] != 0 and gt[i][j] != 0:
                u += 1
            if kmeans[i][j] != 0 and gt[i][j] == 0:
                p += 1
    return u / (p + u)


# iou算法
def iou_function(kmeans, gt):
    row = kmeans.shape[0]
    column = kmeans.shape[1]
    u = 0
    p = 0
    for i in range(row):
        for j in range(column):
            if kmeans[i][j] != 0 and gt[i][j] != 0:
                u += 1
            if kmeans[i][j] != 0 or gt[i][j] != 0:
                p += 1
    return u/p


def _simple_iou_score(gt_image, pre_image):

    u = 0
    p = 0

    for i in range(len(gt_image)):
        if gt_image[i] !=0:
            u += gt_image[i]

    for i in range(len(pre_image)):
        if pre_image[i] !=0:
            p += pre_image[i]

    return u / (p + u)


def _simple_ap_score(gt_image, pre_image):
    u = 0
    p = 0

    for i in range(len(gt_image)):
        if gt_image[i] != 0:
            u += gt_image[i]

    for i in range(len(pre_image)):
        if pre_image[i] != 0:
            p += pre_image[i]

    return u / p


def _cal_iou_score(gt_image, pre_image):
    intersection = np.logical_and(gt_image, pre_image)
    union = np.logical_or(gt_image, pre_image)
    iou_score = np.sum(intersection) / np.sum(union)
    return iou_score



def _read_file_float(full_name):
    img = cv2.imread(full_name, 0)
    rows, cols = img.shape[:]
    data = img.reshape((rows * cols, 1))
    return np.float32(data)


def _open_compare_file(filename):
    str_list = filename.split(".")
    label_data = _read_file_float(label_img_path+str_list[0]+"/"+'label_viz.png')
    kmeans_data = _read_file_float(kmeans_cluster_path+filename)
    slic_data = _read_file_float(slic_cluster_path+filename)
    kmeans_iou_score = _simple_ap_score(label_data, kmeans_data)
    slic_iou_score = _simple_ap_score(label_data, slic_data)
    print('filename:%s kmeans_ap_score:%s vs slic_ap_score:%s' %(filename, kmeans_iou_score, slic_iou_score))


if __name__ == '__main__':
    files = os.listdir(kmeans_cluster_path)
    for file in files:
        _open_compare_file(file)



