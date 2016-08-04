'''
IP Camera Video Stream
======================

Provides framework built in OpenCV to retrieve video
stream from a wireless IP camera. In this example, the
script reads a stream from mjpg-streamer.

Credit: http://www.virtualroadside.com/blog/index.php/2015/04/03/better-python-interface-to-mjpg-streamer-using-opencv/

Usage:
------
    Start the video stream on the Raspberry Pi with mjpg-streamer. To set this up, see
    http://petrkout.com/electronics/low-latency-0-4-s-video-streaming-from-raspberry-pi-mjpeg-streamer-opencv/

    Next, run in CLI

    "python PiCam.py"

    and the video stream should appear. 
'''

import re
from urllib.request import urlopen
import cv2
import numpy as np

# mjpg-streamer URL
url = 'http://134.173.27.40:8080/?action=stream'
stream = urlopen(url)
    
# Read the boundary message and discard
stream.readline()

sz = 0
rdbuffer = None

clen_re = re.compile(b'Content-Length: (\d+)\\r\\n')

# Read each frame
indexOfImage = 0
while True:
      
    stream.readline()                    # content type
    
    try:                                 # content length
        m = clen_re.match(stream.readline())
        clen = int(m.group(1))
        indexOfImage += 1
    except:
        break
    
    stream.readline()                    # timestamp
    stream.readline()                    # empty line
    
    # Reallocate buffer if necessary
    if clen > sz:
        sz = clen*2
        rdbuffer = bytearray(sz)
        rdview = memoryview(rdbuffer)
    
    # Read frame into the preallocated buffer
    stream.readinto(rdview[:clen])
    
    stream.readline() # endline
    stream.readline() # boundary
        
    # This line will need to be different when using OpenCV 2.x

    img = cv2.imdecode(np.frombuffer(rdbuffer, count=clen, dtype=np.byte), flags=cv2.IMREAD_COLOR)
    
    # show image
    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(str(indexOfImage) + '.png', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()