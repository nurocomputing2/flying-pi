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

