

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

ldr_count = 0
no_of_units = 0

for i in range(0,5):
    print GPIO.input(4)
    #ldr_count  = ldr_count + 1

#if ldr_count == 3200:
#   no_of_units = no_of_units + 1
    
