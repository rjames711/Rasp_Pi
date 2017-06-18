# from : https://learn.sparkfun.com/tutorials/raspberry-gpio
#
#
#
#
#
#
#
#
#


#language:Python
# External module imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dir_pin=20
pulse_pin=21
steps_per_rev=200*15
GPIO.setup(pulse_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT) 

def step_degrees(degrees):
    pass


def step(direction):
    if direction:
        GPIO.output(dir_pin, GPIO.HIGH)
    else:
        GPIO.output(dir_pin, GPIO.LOW)

    GPIO.output(pulse_pin, GPIO.HIGH)
    time.sleep(0.020)
    GPIO.output(pulse_pin, GPIO.LOW)

    
