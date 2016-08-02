import socket
# import pygame 
import cv2 
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="134.173.27.40"
# host = '134.173.43.35'
port = 5000
print("Connecting...")
s.connect((host,port))
print("Connected!!")

def ts(message):
   s.send(str(message).encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)

# pygame.init()
# size = [800, 600]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Create Control')
img = np.zeros((500,500, 3), np.uint8)
filename = 'commands.txt'
file = open(filename, 'w')


while 1:
# r = input('Enter Command: ')
   # if not r:
   #  r= input('Enter Command: ')
   # for event in pygame.event.get():
   #      if event.type == pygamge.QUIT:
   #          sys.exit(0)
   #      elif event.type == pygame.KEYDOWN:
   #          if event.key == pygame.K_w:
   #              r = 'f'
   #          elif event.key == pygame.K_a:
   #              r = 'l'
   #          elif event.key == pygame.K_d:
   #              r = 'r'
   #          elif event.key == pygame.K_s:
   #              r = 'b'
   #      else:
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