# from page: https://www.raspberrypi.org/forums/viewtopic.php?f=49&t=55580
# seems to work
import RPi.GPIO as GPIO
import time

# Variables
#rob: modifed speed. was .0055
#delay = 0.0002
steps = 500

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Stepper:
    #Control pins. note, should probably be refactored as instance variables.


    def __init__(self, steps_per_rev):
        #Set instance variables
        self.position=0
        self.steps_per_rev=steps_per_rev
        self.delay=1
        self.coil_A_1_pin = 12 #mapped to DIR - on st-660 driver
        self.coil_A_2_pin = 16 #mapped to DIR + on st-660 driver
        self.coil_B_1_pin = 20 #mapped to PUL - on st-660 driver
        self.coil_B_2_pin = 21 #mapped to Pul + on st-660 driver
        #SET PIN STATES
        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
        self.end_position=0

    def reset_end(self):
        self.end_position=self.position
        
    def reset_home(self):
        self.position=0

    def go_to_position(self, new_position,rpm):
        displacement = new_position - self.position
        self.step_degrees(displacement,rpm)
        
    def step_degrees(self, degrees,rpm):
        self.set_rpm(rpm)
        steps = degrees*self.steps_per_rev/360
        if steps>0:
            self.stepF(steps)
        else:
            self.stepR(-steps)
        self.position+=degrees

    def set_rpm(self, rpm):
        rpm=rpm*1.0 # convert to float
        # 4 delays per step
        # 4*steps_per_rev
        delays_per_rev = self.steps_per_rev*4
        delays_per_min = delays_per_rev*rpm
        self.delay= 60/delays_per_min

    # loop through step sequence based on number of steps
    def stepF(self,steps):
        for i in range(0, steps):
            self.setStep(1,0,1,0)
            time.sleep(self.delay)
            self.setStep(0,1,1,0)
            time.sleep(self.delay)
            self.setStep(0,1,0,1)
            time.sleep(self.delay)
            self.setStep(1,0,0,1)
            time.sleep(self.delay)

    # Reverse previous step sequence to reverse motor direction
    def stepR(self,steps):
        for i in range(0, steps):
            self.setStep(1,0,0,1)
            time.sleep(self.delay)
            self.setStep(0,1,0,1)
            time.sleep(self.delay)
            self.setStep(0,1,1,0)
            time.sleep(self.delay)
            self.setStep(1,0,1,0)            
            time.sleep(self.delay)
            
    def setStep(self,w1, w2, w3, w4):
      GPIO.output(self.coil_A_1_pin, w1)
      GPIO.output(self.coil_A_2_pin, w2)
      GPIO.output(self.coil_B_1_pin, w3)
      GPIO.output(self.coil_B_2_pin, w4)

            
a=''

            
if __name__ == "__main__":
    print " running stepper"
    a=Stepper(3060)
    
else:
    print "importing stepper"
    



