
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# args
iter_max = 1e4
debug = False

if (len(sys.argv) > 1): iterCount = int(sys.argv[1])
if (len(sys.argv) > 2): debug = True
if (debug): print (f'Number of loop iterations before termination: {iter_max}')

led_out = 11 # GPIO 17
switch_in = 13 # GPIO 27

GPIO.setup(led_out, GPIO.OUT)
GPIO.setup(switch_in, GPIO.IN)

with open('data.txt', 'w') as f:

    on = False
    for iter in range(ITER_COUNT):
        output_time = datetime.fromtimestamp()

        if debug:
            print(f'SYSTEM TIME: {output_time} -- ITER: {iter} -- LED State: {on})

        if GPIO.input(switch_in):
            if time is not None:
                if time - time.time() < 0.01:
                    on = False # turn off LED for one second

                    # add to file after state of LED is changed
                    f.write(f'TIME: {time.time():1.00f} \t NEW LED STATE: {on}\n')
                    
                    time = time.time() # reset time
                
            else:
                on = True

                # add to file after state of LED is changed
                f.write(f'TIME: {time.time():1.00f} \t NEW LED STATE: {on}\n')

                time = time.time() # switch was just activated
            

        else:
            time = None # deactivate time in case it was set
            on = False

            # add to file after state of LED is changed
            f.write(f'TIME: {time.time():1.00f} \t NEW LED STATE: {on}\n')


GPIO.cleanup()

