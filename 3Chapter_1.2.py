import cv2

cap = cv2.VideoCapture(0)
""" here the video input is taken from 
the webcam"""

cap.set(3,640)  #setting the height width of the output window
cap.set(4,480)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break