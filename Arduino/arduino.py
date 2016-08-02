'''
Arduino Control
===============

Provides a framework using pygame and pyserial
for serial control of an Arduino Robot.

Control using the WASD keys.
'''

import serial
import struct
import random
import time
import pygame
import sys

class Arduino():
    """
    Represents an Arduino robot connected by USB.
    Allows user to send commands to the robot through a serial connection.
    """

    def __init__(self, user_port='/dev/ttyACM0', user_baud=115200, user_timeout=1):
        """
        Constructor for class Arduino
        """

        self.connected = False
        self.ser = serial.Serial(user_port, user_baud, timeout=user_timeout)

        # valid commands: forward, backward, pivot right, pivot left, brake
        self.validCommands = ['f','b','r','l','s']

        # connect to the serial port
        self.connect()


    def sendCommand(self, command):
        """
        Writes command to serial port to be read.
        Note that both command and the duration of the command must be encoded to bytes.
        """

        self.ser.write(bytes(command.encode('utf-8')))

        # check if command is valid
        assert command in self.validCommands, "%r is not a valid command" % command

        # wait for Arduino to finish executing the command.
        while self.ser.read() == command:
            self.ser.read()


    def connect(self):
        """
        Connect to Arduino through serial connection.
        Wait until response from Arduino.
        """

        print("Connecting to port", self.ser.port)

        while not self.connected:
            serin = self.ser.read()
            self.connected = True
        print("Connected!")

        # self.calibrate()


    def disconnect(self):
        """
        Disconnect in case of emergency.
        """

        self.connected = False
        self.ser.close()

if __name__ == '__main__':
    pygame.init()
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Arduino Control')
    robot = Arduino()
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