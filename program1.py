import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
import sys


pin1 = 35
in_pin = 37

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(in_pin, GPIO.IN)

while True:
   if GPIO.input(in_pin):
      GPIO.output(pin1, GPIO.HIGH) # Turn on
   else:
      GPIO.output(pin1, GPIO.LOW)  # Turn off

GPIO.cleanup()
