import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

try:
  while 1:
    GPIO.output(21,1)
    time.sleep(1)
    GPIO.output(21,0)
    time.sleep(1)
 
finally:
  GPIO.cleanup()


# 횟수 지정 버전 
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(21,GPIO.OUT)


# for i in range(1,3):

#    GPIO.output(21,True)

#    time.sleep(2)


#    GPIO.output(21,False)


#    time.sleep(2)



# GPIO.cleanup() 

# print("cleanup")

# time.sleep(2)
