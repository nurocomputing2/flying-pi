from picamera import PiCamera #get the PiCamera code
from time import sleep
import RPi.GPIO as GPIO
import os

camera = PiCamera() #defines he PiCamera

camera.start_preview() # start the preview to check how the cam records
sleep(10)
camera.stop_preview
print("starting recording in 10 secconds")
sleep(10)
camera.start_preview()
camera.start_recording('/home/pi/Desktop/image%s.h264' % i) # where the video is saved
camrecording = True
GPIO.setmode(GPIO.BCM) #setting up gpio "stop button" From here 
GPIO.setwarnings(False)

button = 4 #Defines the button GPIO pin

GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP) #To here

while True:     #checks if button is pressed by constentle checking
  button_state = GPIO.input(button)
  if button_state == GPIO.HIGH:
    print (" >>Recording...")
  else:
    print (" Stopping...>>")
    camrecording = False #May be used in later parts - currently does nothing.
   camera.stop_recording() #stops and saves the recording
   camera.stop_preview()
    sleep(0.5) #Avoids "bouncing" (de-bouncing)
    print(" >>Restarting...")
    os.system("poweroff") #restarts/ reboots the raspberry pi
