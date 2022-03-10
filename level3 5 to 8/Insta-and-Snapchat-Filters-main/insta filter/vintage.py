import cv2
import numpy as np
from matplotlib import pyplot as plt
im = cv2.imread('fruit.jpeg')

# arr = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])

# print(arr.shape)
# print(im.shape)
rows, cols = im.shape[:2]# (465, 640, 3) --> 3 is used for slicing and we r putting 465 in rows, 640 in cols
# Create a Gaussian filter
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage_im = np.copy(im)
# for each channel in the input image, we will apply the above filter
for i in range(3):
    vintage_im[:,:,i] = vintage_im[:,:,i] * filter
plt.imshow(vintage_im)
plt.show()