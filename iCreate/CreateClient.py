'''
iCreate Client-side Control
===========================

Provides socket framework to connect to
iCreate server running on Raspberry Pi over
WiFi connection. Allows wireless control of 
Raspberry Pi.

See https://github.com/zhangxingshuo/py-robot
for documentation.

Usage:
------
  Start the iCreate server on the Raspberry Pi
  connected to the iCreate. 

  In CLI, run

  "python CreateClient.py"

  and a window should appear. Control with WASD. 
'''

import socket
import cv2 
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host IP address -- change as needed
host ="134.173.27.40"
port = 5000

print("Connecting...")
s.connect((host,port))
print("Connected!!")

def ts(message):
   s.send(str(message).encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)

img = np.zeros((500,500, 3), np.uint8)
filename = 'commands.txt'
file = open(filename, 'w')


while True:
    cv2.imshow('control', img)
    file = open(filename, 'a')
    k = cv2.waitKey(0)
    if k == ord('w'):
        r = 'f'
        file.write('f\n')
    elif k == ord('a'):
        r = 'l'
        file.write('l\n')
    elif k == ord('s'):
        r = 'b'
        file.write('f\n')
    elif k == ord('d'):
        r = 'r'
        file.write('r\n')
    elif k == 32:
        r = 's'
        file.write('\\n f')
    elif k == ord('q'):
        break
    elif k == ord('r'): # RESET
        r = 'RESET'
    ts(r)

s.close()