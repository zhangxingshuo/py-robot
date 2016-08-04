'''
iCreate Server-side Control
===========================

Starts a server on the Raspberry Pi that 
accepts a client over WiFi. The client can
then control the iCreate using the serial
connection control framework also provided
in this repository. 

See https://github.com/zhangxingshuo/py-robot
for documentation.

Usage:
------
        On the Raspberry Pi, start

        "python CreateServer.py"

        and a message should appear saying 
        "Server Started". You can now connect
        a client computer using the client-side
        framework provided in this repository.
'''

import socket
from create import Create

def Main(socket):
        print 'Server Started'

        s.listen(1)
        c, addr= s.accept()

        print 'Connection from: ' + str(addr)

	create = Create()
	create.sendCommandASCII('128') # Passive
	create.sendCommandASCII('131') # Safe

        while True:
                data= c.recv(1024)
                if not data:
                        break
                print 'From Connected User: ' + str(data)
		create.sendCommand(str(data))
                c.send(data)
        c.close()
	print 'Disconnected From Client'
	Main(socket)

if __name__=='__main__':
        # host IP address -- change as needed
	host = '134.173.27.40' 
        port = 5000

        s= socket.socket()
        s.bind((host,port))
        Main(s)

