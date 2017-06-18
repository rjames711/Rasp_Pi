
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)


ledpin=21


for i in range(0,100):
    GPIO.output(ledpin, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(ledpin, GPIO.LOW)
    time.sleep(0.25)
