import cv2
import matplotlib.pyplot as plt
im = cv2.imread('house.jpeg')
dst = cv2.GaussianBlur(im,(101,101),cv2.BORDER_DEFAULT)
plt.imshow(dst)
plt.show()