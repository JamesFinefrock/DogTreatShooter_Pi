import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(0)


#time.sleep(2)
#p.ChangeDutyCycle(25)
#time.sleep(2)
#p.ChangeDutyCycle(0)
#time.sleep(2)
  

GPIO.cleanup()
