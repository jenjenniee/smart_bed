import RPi.GPIO as GPIO
import argparse

GPIO.setmode(GPIO.BCM)

RED_PIN   = 17
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

    elif color == "yello":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.HIGH)

    elif color == "white":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(BLUE_PIN, GPIO.HIGH)
    else:
        print("error")

def led_off():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

            

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Options")

    parser.add_argument('-l','--led', required = True, help = 'Choose the color (red/green/blue)')
    
    args = parser.parse_args()
    
    color = args.led
    led_on(color)

    gp.cleanup()
