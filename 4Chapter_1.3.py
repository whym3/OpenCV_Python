import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7,7), 0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("GrayImg", imgGray)
cv2.imshow("BlurImg", imgBlur)
cv2.imshow("CannyImg",imgCanny)
cv2.imshow("DialationImg",imgDialation)

cv2.waitKey(0)
