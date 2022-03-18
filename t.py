import RPi.GPIO as GPIO
import time

RED_PIN   = 27
GREEN_PIN = 22
BLUE_PIN  = 24

GPIO.setwarnings(False)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def led(pin, t):
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(t) 

    GPIO.cleanup(pin)

led(27, 5) # 18번 핀에 끼운 LED를 5초동안 점등