import cv2
import numpy as np 

robotVid = cv2.VideoCapture('robot.mov')

ret, frame = robotVid.read()

while ret is not None:
    cv2.imshow('Video', frame)
    ret, frame = robotVid.read()
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()