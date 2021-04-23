import cv2
import numpy

#  Resizing an Image
img = cv2.imread("Resources/lambo.png")
print(img.shape)
imgResize = cv2.resize(img, (300, 200))
"""Resize Function is used to
resize the image to any size we want """

#Cropping an Image
imgCropped = img[0:200, 200:500]
""" we just use a matrix to crop an image 
int his matrix the height comes first then 
the width """

cv2.imshow("Image",img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)

