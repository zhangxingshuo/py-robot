'''
iPad Client-side Odometric Retrieval
====================================

Retrieves odometry data in the form of accelerometer
and gyroscope vectors from an iPad over a WiFi connection. 

See https://github.com/zhangxingshuo/py-robot for 
documentation.

Usage:
------
	With the iPad server running, start the client computer.
	In CLI, run

	"python iPadClient.py"

	and the data from the iPad should appear. 
'''

import socket
import sys
import cv2
import numpy as np

def Main():
	# host IP address -- change as needed
	host= "134.173.24.116"
	port= 5003

	print('Waiting for Connection....')
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	print('Connected!')

	img = np.zeros((640, 480, 3), np.uint8)
	while True:
		data= s.recv(1024).decode('utf-8')
		print(len(data.split(',')))
		print ('Received from server: ' + str(data))
		k = cv2.waitKey(1)
		cv2.imshow('control', img)
		if k == ord('q'):
			break
	s.close()

if __name__=='__main__':
	Main()

