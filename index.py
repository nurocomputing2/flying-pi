from picamera import PiCamera #get the PiCamera code
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera() #defines he PiCamera

camera.start_preview() # start the preview to check how the cam records
sleep(10)
camera.stop_preview
print("starting recording in 10 secconds")
sleep(10)
camera.start_preview()
camera.start_recording('/home/pi/Desktop/image%s.h264' % i) # where the video is saved
camrecording = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
while True:
  if (GPIO.input(17)):
   camrecording = False
   camera.stop_recording()
   camera.stop_preview()

