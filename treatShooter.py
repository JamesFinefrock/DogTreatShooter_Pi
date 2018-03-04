import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)


time.sleep(2)
p.changeDutyCycle(50)
time.sleep(2)
p.changeDutyCycle(7.5)
  

GPIO.cleanup()
