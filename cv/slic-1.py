# coding: utf-8

# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
# import argparse
import cv2
import os

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())

# load the image and apply SLIC and extract (approximately)
# the supplied number of segments



def save_slic_cluster(filename):
    image = cv2.imread('/Users/didi/Desktop/car-images/'+filename)
    segments = slic(img_as_float(image), n_segments=2, sigma=10)

    # show the output of SLIC
    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
    plt.axis("off")
    plt.savefig("/Users/didi/Desktop/slic-cluster/"+filename)


if __name__ == '__main__':
    files = os.listdir("/Users/didi/Desktop/car-images/")
    for file in files:
        if file.endswith("jpg") or file.endswith("jpeg"):
            save_slic_cluster(file)

