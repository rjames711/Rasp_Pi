#!/usr/bin/env python
 
# pulse.py
#pigpio scripts require that the pigpio daemon be running.
#sudo pigpiod
#They do not need to be run as root.
#./pulse.py
#Found on: http://elinux.org/RPi_GPIO_Code_Samples#WiringPi
# under the python, pigpio section.

import time

import pigpio
 
pi = pigpio.pi() # Connect to local Pi.
 
# set gpio modes
 
pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(23, pigpio.INPUT)
pi.set_mode(24, pigpio.OUTPUT)
 
 
# start 1500 us servo pulses on gpio4
 
pi.set_servo_pulsewidth(4, 1500)
 
# start 75% dutycycle PWM on gpio17
 
pi.set_PWM_dutycycle(17, 192) # 192/255 = 75%
 
start = time.time()
 
while (time.time() - start) < 60.0:
 
      pi.write(18, 1) # on
 
      time.sleep(0.5)
 
      pi.write(18, 0) # off
 
      time.sleep(0.5)
 
      # mirror gpio24 from gpio23
 
      pi.write(24, pi.read(23))
 
pi.set_servo_pulsewidth(4, 0) # stop servo pulses
 
pi.set_PWM_dutycycle(17, 0) # stop PWM
 
pi.stop() # terminate connection and release resources
