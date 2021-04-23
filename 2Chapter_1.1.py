import cv2

cap = cv2.VideoCapture("Resources/test.mp4")
""" VideoCapture function reads the 
video specified in the arguements """

while True:
    """ As a video is a series of photos
    we have use a while loop to display the 
    video """

    success, img = cap.read()
    """here all the series of images are
    being read and stored in img"""


    cv2.imshow("Video",img)
    """Now all the series of images are
    projected on the screen as a video"""

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        """Here if the video is too long and the 
        user wants to break the loop and wants to close 
        the output stream Q button on the keyboard can 
        be pressed to stop it."""
        break