import RPi.GPIO as GPIO
import argparse
import time

class Led:
    def __init__(self, color, blink_input):
        self.color = color
        self.blink_input = blink_input
        

    def gpio_setup(self):
        GPIO.setmode(GPIO.BCM)
        RED_PIN   = 17
        GREEN_PIN = 22
        BLUE_PIN  = 24

        GPIO.setwarnings(False)

    #     GPIO.setmode(GPIO.BOARD)
    #     GPIO.setup(11,GPIO.OUT)
    #     GPIO.setup(15,GPIO.OUT)
    #     GPIO.setup(18,GPIO.OUT)
    #     RED_PIN   = GPIO.PWM(11)
    #     GREEN_PIN = GPIO.PWM(15)
    #     BLUE_PIN  = GPIO.PWM(18)

    #     GPIO.setwarnings(False)

def led_on(self):

    GPIO.setmode(GPIO.BCM)

    RED_PIN   = 17
    GREEN_PIN = 22
    BLUE_PIN  = 24

    GPIO.setwarnings(False)

    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)

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
        print("----------------error")

def twinkle(self, color):
    if twinkle_input =="o":
        led_on(color)
        time.sleep(0.5)
        led_on("off")
        time.sleep(0.5)
    else:
        led_on(color)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Options")

    parser.add_argument('-l','--led', required = True, help = 'Choose the color (red/green/blue/off)')
    parser.add_argument('-t','--twinkle_input', required = True, help = 'Choose the twinkle (o/x)')
    
    args = parser.parse_args()
    
    color = args.led
    twinkle_input = args.twinkle_input

    while(True):
        twinkle(color, twinkle_input)

