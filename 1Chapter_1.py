import cv2

img = cv2.imread("Resources/lena.png")
"""imread function reads the image
   file provided and stores it into the
   variable img"""


cv2.imshow("Output", img)
"""imshow function displays the output
    i.e the image file provided in the 
    variable 
    It has 2 arguements 
    1. Window name
    2. The Variable to print"""


cv2.waitKey(0)
"""waitKey function holds the output for 
the number of miliseconds provided in as arguement
Use 0 for holding until you exit"""