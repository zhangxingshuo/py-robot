'''
iCreate Control
===============

Provides framework using pygame and 
pyserial to control an iCreate through
a serial connection.

Control using the WASD keys.
'''

import struct
import serial
import sys
import glob
import pygame

def getSerialPorts():
    if sys.platform.startswith('win'):
        ports= ["COM" + str(i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    print ports
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except(OSError, serial.SerialException):
            pass

    return result

class Create(object):

    def __init__(self, user_port='/dev/ttyUSB0', user_baud=115200, user_timeout=1):
        self.connected = False
        print 'Trying ' + user_port + '...'
        try:
            self.ser = serial.Serial(user_port, baudrate=user_baud, timeout=user_timeout)
            print 'Connected!'
            self.connected = True
        except:
            print 'Could not connect to port ' + user_port

    def sendCommandRaw(self, command):
        try:
            if self.connected:
                self.ser.write(command)
            else:
                print "Not connected."
        except serial.SerialException:
            print "Lost connection."

        # print ' '.join([ str(ord(c)) for c in command ])

    def sendCommandASCII(self, command):
        cmd = ""
        for v in command.split():
            cmd += chr(int(v))
        self.sendCommandRaw(cmd)


    def sendCommand(self, command):
        if command == 'f':
            cmd = struct.pack('>Bhh', 145, 150, 150)
            self.sendCommandRaw(cmd)
        elif command == 's':
            cmd = struct.pack('>Bhh', 145, 0, 0)
            self.sendCommandRaw(cmd)
        elif command == 'l':
            cmd = struct.pack('>Bhh', 145, 128, -128)
            self.sendCommandRaw(cmd)
        elif command == 'r':
            cmd = struct.pack('>Bhh', 145, -128, 128)
            self.sendCommandRaw(cmd)
        elif command == 'b':
            cmd = struct.pack('>Bhh', 145, -256, -256)
            self.sendCommandRaw(cmd)
        elif command == 'RESET':
            self.sendCommandASCII('128') # PASSIVE
            self.sendCommandASCII('131') # SAFE

    def disconnect(self):
        self.connected = False
        self.ser.close()


if __name__ == '__main__':
    pygame.init()
    size = [640, 480]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Create Control')
    robot = Create()
    robot.sendCommandASCII('128')
    robot.sendCommandASCII('131')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    robot.sendCommand('l')
                elif event.key == pygame.K_d:
                    robot.sendCommand('r')
                elif event.key == pygame.K_w:
                    robot.sendCommand('f')
                elif event.key == pygame.K_s:
                    robot.sendCommand('b')
                elif event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.KEYUP:
                    robot.sendCommand('s') 
