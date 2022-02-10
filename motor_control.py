import RPi.GPIO as gp  
from time import sleep 
import time 
import argparse

class Bed:
    def __init__(self,user, type, dir, c_time):
        self.user = user
        self.type = type
        self.dir = dir
        self.c_time = c_time 
    
    def __str__(self):
        return "{}_bed / type: {}, direction: {}, time: {}".format(self.user, self.type, self.dir, self.c_time)

    def __repr__(self):
        return "{}_bed / type: {}, direction: {}, time: {}".format(self.user, self.type, self.dir, self.c_time)
    
    #gpio setting
    def gpio_setup(self):
        gp.setmode(gp.BOARD)
        gp.setup(12,gp.OUT)
        gp.setup(32,gp.OUT)
        gp.setup(11,gp.OUT)
        gp.setup(31,gp.OUT)

        pwm_up1 = gp.PWM(32,50)
        pwm_up2 = gp.PWM(31,50)
        pwm_down1 = gp.PWM(12,50)  
        pwm_down2 = gp.PWM(11,50) 

        if self.type == "head":
            pwm_down = pwm_down1
            pwm_up = pwm_up1

        elif self.type == "body":
            pwm_down = pwm_down2
            pwm_up = pwm_up2

        elif self.type == "both":
            pwm_down1.start(0)  
            pwm_up1.start(0)
            pwm_down2.start(0)  
            pwm_up2.start(0)
            return (pwm_up1, pwm_down1, pwm_up2, pwm_down2)
            
        else: 
            print("error")
            #self.led(1, "on")

        pwm_down.start(0)  
        pwm_up.start(0)

        return(pwm_up, pwm_down, 0, 0)



    #control according to direction,time
    def control(self):
        try:
            pwm_up, pwm_down, _ , _ = self.gpio_setup()
            #up
            if self.dir == "up":
                print("up")
                pwm = pwm_up

            elif self.dir == "down":
                print("down")
                pwm = pwm_down

            j = 0
            #led(2, "on")
            while True:
                pwm.ChangeDutyCycle(j)
                sleep(1)
                if j >= self.c_time:
                    break
                j += 1
            #self.led(3, "on")
            pwm.ChangeDutyCycle(0) 
            pwm.stop()
        except:
            print("error1")
            #self.led(1, "on")
            

    def control_both(self):
        try:
            pwm_up, pwm_down, pwm_up2, pwm_down2 = self.gpio_setup()
            if self.dir == "up":
                print("up")
                pwm = pwm_up
                pwm1 = pwm_up2

            elif self.dir == "down":
                print("down")
                pwm = pwm_down
                pwm1 = pwm_down2

            j = 0
            while True:
                pwm.ChangeDutyCycle(j)
                pwm1.ChangeDutyCycle(j)
                sleep(1)
                #self.led(2,"on")
                if j >= self.c_time:
                    break
                j += 1
            # self.led(3,"on")
            pwm.ChangeDutyCycle(0) 
            pwm1.ChangeDutyCycle(0) 
            pwm.stop()
            pwm1.stop()
        except:
            print("error2")
            # self.led(1, "on")
    
    def run(self):
        if self.type == "both":
            self.control_both()
        else: self.control()

        gp.cleanup()


if __name__=='__main__':
    
    try:
        parser = argparse.ArgumentParser(description="Options")

        parser.add_argument('-t','--type', required = True, help = 'Choose the type (head/body/both)')
        parser.add_argument('-d','--direction', required = True, help = 'Choose the direction(up/down)')
        parser.add_argument('-c','--c_time', required = True, type = int, help = 'How much?')
        
        args = parser.parse_args()
        
        type = args.type
        dir = args.direction
        c_time = args.c_time
    
        # type = input("Choose the type (head/body/both): ")
        # dir = input("Choose the direction(up/down): ")
        # c_time = int(input("How much?: "))

        user1 = Bed('sujin',type,dir,c_time)
        user1.run()

    except:
        print("ss")
