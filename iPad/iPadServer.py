# coding: utf-8
import socket
import motion
import photos
import time

def Main(socket):   
    print('Server Started')
    
    s.listen(1)
    c, addr = s.accept()
    print('Connection From: ' + str(addr))
    
    motion.start_updates()
    while True:
        xaccel, yaccel, zaccel= motion.get_gravity()
        xrot, yrot, zrot= motion.get_attitude()
        message= str(xaccel)[:6] + ',' + str(yaccel)[:6] + ',' + str(zaccel)[:6] + ','+ str(xrot)[:6] + ',' + str(yrot)[:6] + ',' + str(zrot)[:6]
        print(message)
        try:
            c.send(str(message))
            time.sleep(0.05)
        except:
            break
    c.close()
    Main(socket)
        
if __name__=='__main__':
    host= '134.173.29.21'
    port= 5001
    
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    Main(s)