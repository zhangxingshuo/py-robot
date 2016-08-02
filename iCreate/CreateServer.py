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
	host = '134.173.27.40' 
        port = 5000

        s= socket.socket()
        s.bind((host,port))
        Main(s)

