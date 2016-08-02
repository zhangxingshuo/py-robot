# Python Robotic Control
Python platform for remote control of robotics systems and cameras. 

## Setup
### Arduino
It is assumed that an Arduino UNO board is being used, with continuous servos connected to pins 9 and 10. Note that this robot is fully tethered, so a USB extension may be required. 

### iCreate
The iCreate robot is a Raspberry Pi running Raspbian Jessie with the iCreate connected to the Raspberry Pi through a USB serial interface. The Raspberry Pi should also have access to WiFi through a WiFi adapter. 

## Usage
### Arduino Robot
Upload the file `PythonRobot.ino` to the Arduino. Check the serial port in the Arduino IDE. With the Arduino on and running, run 

`python arduino.py`

in CLI. This will open a blank window. Click on the window. The WASD keys will control the robot.

### iCreate
Start the script `CreateServer.py` on the Raspberry Pi. If an error is thrown, check the IP address with `ifconfig` and edit the script accordingly. 

On the client computer, run

`python CreateClient.py`

in CLI. This will open a blank window. Click on the window. The WASD keys will control the robot. 

## Cameras
### USB Web Camera
The script

`python cam.py`

will read a video stream from a USB webcam.

### Video Streaming from Raspberry Pi
For a camera module connected to the Raspberry Pi, refer to [this tutorial](http://petrkout.com/electronics/low-latency-0-4-s-video-streaming-from-raspberry-pi-mjpeg-streamer-opencv/) to install mjpg-streamer on the Raspberry Pi. With the stream open, run

`python PiCam.py`

on the client computer, and the video stream should show up. 

## Credits
Harvey Mudd College Computer Science REU 2016

Ciante Jones: cjjones@hmc.edu

Chi-Yen Lee: johlee@hmc.edu

Andy Zhang: axzhang@hmc.edu

Professor Zach Dodds: zdodds@hmc.edu
