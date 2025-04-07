import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("elephant.jpg")

#the following are low pass kernels (blur)

#box filter
box = cv2.blur(img, (3, 3))

#Gaussian kernel
Gaussian = cv2.GaussianBlur(img, (3, 3), 0)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(box),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(Gaussian),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()