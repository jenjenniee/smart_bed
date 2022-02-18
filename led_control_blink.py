import RPi.GPIO as GPIO
import argparse
import time

GPIO.setmode(GPIO.BCM)

RED_PIN   = 27
GREEN_PIN = 22
BLUE_PIN  = 24

GPIO.setwarnings(False)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def led_on(color):
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    if color == "red":
        GPIO.output(RED_PIN, GPIO.HIGH)

    elif color == "green":
        GPIO.output(GREEN_PIN, GPIO.HIGH)

    elif color == "blue":
        GPIO.output(BLUE_PIN, GPIO.HIGH)

    elif color == "yellow":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.HIGH)

    elif color == "white":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(BLUE_PIN, GPIO.HIGH)

    elif color == "off":
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)
    else:
        print("error")

def blink(color,blink):
    if blink =="o":
        led_on(color)
        time.sleep(0.5)
        led_on("off")
        time.sleep(0.5)
    else:
        led_on(color)

            

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Options")

    parser.add_argument('-l','--led', required = True, help = 'Choose the color (red/green/blue/off)')
    parser.add_argument('-t','--blink', required = True, help = 'Choose the blink (o/x)')
    
    args = parser.parse_args()
    
    color = args.led
    blink = args.blink

    while(True):
        blink(color,blink)
