import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter


img = cv2.imread("elephant.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtering = median_filter(gray, 1)

#approximation to (f - h_{blur} * f)
laplacian = cv2.Laplacian(filtering, cv2.CV_64F)

#observe the effect on detecting edges
gamma = 1.5
sharpened = gray - gamma * laplacian

cv2.imshow("sharpened", sharpened)
cv2.waitKey(0)