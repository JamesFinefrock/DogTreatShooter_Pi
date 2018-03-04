import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)

p = GPIO.PWM(13,50)
p.start(0)


time.sleep(1)
p.ChangeDutyCycle(5.5)
time.sleep(.5)
p.ChangeDutyCycle(0)
time.sleep(2)

p.stop()

GPIO.cleanup()
