'''
After a lot of confusion on how the driver (smakn tb6600) works it turns out its
very simple; the DIR+ pin is set high or low to control direction, the PUL+ pin is sent a
pulse for every step needed and the PUL- and DIR- can simply be tied to logic ground
This is likely typical operation for this type of industrial step driver.
'''
import RPi.GPIO as GPIO
import time

DIR=20
PUL=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)


GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)


def turn_pins_off():
    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(PUL, GPIO.LOW)

def step(steps, delay):
    turn_pins_off()
    if steps<0:
        GPIO.output(DIR, GPIO.HIGH)
        steps=abs(steps)
    for i in range(0,steps):
        GPIO.output(PUL, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        time.sleep(delay)

        
