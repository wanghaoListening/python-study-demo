# coding: utf-8

from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import cv2 as cv

# load the image and convert it to a floating point data type
image = img_as_float(cv.imread("/Users/didi/Desktop/car-images/1.jpeg"))

fig = plt.figure()
# loop over the number of segments`
for numSegments, i in ((100, 1), (200, 2), (300, 3)):
	# apply SLIC and extract (approximately) the supplied number
	# of segments
	segments = slic(image, n_segments=numSegments, sigma=5)

	# show the output of SLIC
	ax = fig.add_subplot(3, 1, i)
	ax.set_title("Superpixels -- %d segments" % (numSegments))
	ax.imshow(mark_boundaries(image, segments))
	plt.axis("off")

# show the plots
plt.show()