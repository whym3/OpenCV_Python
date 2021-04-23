# Joining Images

import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow("output", hor)
cv2.imshow("VerOutput", ver)

cv2.waitKey(0)