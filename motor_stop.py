import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

try:
  while 1:
    GPIO.output(21,0)
    
finally:
  GPIO.cleanup()
