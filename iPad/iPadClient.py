import socket
import sys
import cv2
import numpy as np

def Main():
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
		cv2.imshow('control yo', img)
		if k == ord('q'):
			break
	s.close()

if __name__=='__main__':
	Main()

