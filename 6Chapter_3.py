# Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
""" Using numpy library to make a matrix"""

# print(img.shape)   # it prints the shape/size of the image

# img[:] = 255, 0, 0
""" It specifies the color of the image """

# Drawing Shapes
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (255, 0, 0), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 3)

# Inserting text on the Image
cv2.putText(img, "Hello", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 4)


cv2.imshow("Output", img)
cv2.waitKey(0)
