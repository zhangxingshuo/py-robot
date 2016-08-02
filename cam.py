'''
Video Camera
============

Simple video capture program.

Usage:
------
    cam.py [<video source>]

    Press 's' to save an image.

    Press ESC to exit. 
'''

import cv2
import numpy as np
from datetime import datetime

class Cam(object):

    def __init__(self, src):
        self.cam = cv2.VideoCapture(src)
        ret, self.frame = self.cam.read()
        cv2.namedWindow('Camera')

    def save(self):
        filename = 'cam_img/frame_' + str(datetime.now()).replace('/','-')[:19] + '.jpg'
        cv2.imwrite(filename, self.frame)

    def run(self):
        while True:
            ret, self.frame = self.cam.read()
            cv2.imshow('Camera', self.frame)
            k = 0xFF & cv2.waitKey(5)
            if k == 27:
                break
            if k == ord('s'):
                self.save()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    import sys
    try:
        src = sys.argv[1]
    except:
        src = 0
    print(__doc__)

    Cam(src).run()