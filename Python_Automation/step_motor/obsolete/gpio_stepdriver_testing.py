#testing to determine how different signals affect driver 
# (coil on off polarity) for the smakn tb6600 step motor driver

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


    
def generate_gpio_seq(seq):
    for i in range(0,len(pins)):
        if seq[i]:
            GPIO.output(pins[i], GPIO.HIGH)
            print('pin '+str(pins[i])+' high')
        else:
            GPIO.output(pins[i], GPIO.LOW)
            print('pin '+str(pins[i])+' low')


#generate all possible combos for 4 pins
def get_pin_combos():
    sequence=[]
    for i in range(0,16):
        sbin=bin(i)
        sbin=sbin[2:len(sbin)]
        while len(sbin)<4:
            sbin='0'+sbin
        sbin=[int(x) for x in sbin]
        sequence.append(sbin)
    return sequence

turn_pins_off()
combos=get_pin_combos()

f=open('driver_test.txt', 'a')
f.write('Testing pin combos and coil outputs on tb6600 step motor driver\n')


for i in range(0,len(combos)):
    print(combos[i])
    generate_gpio_seq(combos[i])
    try:
        coil_a=input("enter coil a voltage: ")
        coil_b=input("enter coil b voltage: ")
        f.write('\n'+str(combos[i])+' coil a:'+str(coil_a)+' coil b:'+str(coil_b))
    except:
        print('no write')
    
    
 
f.close()
turn_pins_off()
