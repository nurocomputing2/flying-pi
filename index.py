from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()
imput = input("rotate? y or n")
if imput = "y"
imput = input("how much?")
camera.rotation = imput
camera.start_preview()
sleep(10)
camera.stop_preview()
imput = input("Good?")
if imput = "y"
imput = input("Start recording?")
if imput = "y"
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
camrec = True
imput = input("Tell me when to stop(type stop)")
while camrec = True
 if imput = "stop"
  camrec = False
camera.stop_recording()
camera.stop_preview()

