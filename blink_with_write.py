import RPi.GPIO as GPIO
import time
from datetime import datetime
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# args
blink_time = 1.0
prgm_dur = 10
debug = False

if (len(sys.argv) > 1): blink_time = float(sys.argv[1])
if (len(sys.argv) > 2): prgm_dur = int(sys.argv[2])
if (len(sys.argv) > 3): debug = True

iterCount = int(prgm_dur / blink_time)

if (debug): print (f'Number of loop iterations before termination: {iterCount}')

led_out = 35 # GPIO 17
switch_in = 37 # GPIO 27

GPIO.setup(led_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch_in, GPIO.IN)

LED_ON = False

start_time = time.time()

with open('data.txt', 'w') as f:

   for i in range(iterCount):
 
      if GPIO.input(switch_in):

         LED_ON = not(LED_ON)
      else:
         LED_ON = False
         
      GPIO.output(led_out, LED_ON)

      f.write(f'{(time.time()-start_time):1.2f} \t  {LED_ON}\n')

      if debug:
         print(f'The LED is on: {LED_ON} \t Time since start: {(time.time()-start_time):1.2f} \t Number of iterations: {i}')

      time.sleep(blink_time)
      

GPIO.cleanup()

