#testing to determine how different signals affect driver 
# (coil on off polarity) for the smakn tb6600 step motor driver
# .000001 seems to be the fastest delay it can drive at
import RPi.GPIO as GPIO
import time

pins=[12,16,20,21]
DIR_minus=pins[0]
DIR_plus=pins[1]
PUL_minus=pins[2]
PUL_plus=pins[3]

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_minus, GPIO.OUT)
GPIO.setup(DIR_plus, GPIO.OUT)
GPIO.setup(PUL_minus, GPIO.OUT)
GPIO.setup(PUL_plus, GPIO.OUT)


GPIO.setup(DIR_minus, GPIO.OUT)
GPIO.setup(DIR_plus, GPIO.OUT)
GPIO.setup(PUL_minus, GPIO.OUT)
GPIO.setup(PUL_plus, GPIO.OUT)

def turn_pins_off():
    GPIO.output(DIR_minus, GPIO.LOW)
    GPIO.output(DIR_plus, GPIO.LOW)
    GPIO.output(PUL_minus, GPIO.LOW)
    GPIO.output(PUL_plus, GPIO.LOW)
#sequence from old working file.
#this works, other only go one direction.
# doesn't really make sense; last two steps are the same?
# maybe I made an error recording polarities
step_seq=(
    (1, 0, 1, 0),# - +
    (0, 1, 1, 0),# + -
    (0, 1, 0, 1),# - -
    (1, 0, 0, 1),# - -
    )

#sequence determined from testing on driver 
step_seq1=(
    (0, 1, 1, 0),  
    (0, 0, 0, 0),
    (0, 0, 1, 1),
    (1, 1, 0, 0),
    )

#trying to get a working reverse sequence
step_seq2=(
    (0, 0, 1, 1),
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 0, 0),
    )

step_seq3=(
    (1, 1, 0, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 0),
    (0, 1, 1, 0),
    )
    
def generate_gpio_seq(seq,delay):
    for i in range(0,len(pins)):
        time.sleep(delay)
        if seq[i]:
            GPIO.output(pins[i], GPIO.HIGH)
            #print('pin '+str(pins[i])+' high')
        else:
            GPIO.output(pins[i], GPIO.LOW)
            #print('pin '+str(pins[i])+' low')

def stepF(delay):
    for i in range(0, len(step_seq)):
        #print(step_seq[i])
        generate_gpio_seq(step_seq[i],delay)
    pass
def stepZ(delay):
    for i in range(0, len(step_seq3)):
        #print(step_seq[i])
        generate_gpio_seq(step_seq2[i],delay)
    pass

def stepR(delay):
    for i in range(len(step_seq)-1,-1,-1):
        #print(step_seq[i])
        generate_gpio_seq(step_seq[i],delay)
    pass

# testing the idea that this step driver working completely different from the driver chips online and simply steps
# based on a pulse and a binary signal to the DIR
# so with this it you could set everything low and then send pulses to PUL+ and it would step
def pulse_step(steps, delay):
    turn_pins_off()
    if steps<0:
        GPIO.output(DIR_plus, GPIO.HIGH)
        steps=abs(steps)
    for i in range(0,steps):
        GPIO.output(PUL_plus, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PUL_plus, GPIO.LOW)
        time.sleep(delay)

        
#the test: start with shaft mark vertical
# set delay @ .000005 
# step forward 20000 steps. is position maintained?
# repeat going backward
