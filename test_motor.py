#Simple demo of the stepper motor, does a full rotation

import RPi.GPIO as GPIO
import time

print("Hello")

# Set constants
ControlPin = [11, 13, 15, 16] # Set the GPIO pins for the motor
num_steps = 512 # Set the number of step
delay = 0.001 # Set delay between steps

step_sequence = [[1,0,0,0],[1,1,0,0], # Counter-Clockwise
                 [0,1,0,0],[0,1,1,0],
                 [0,0,1,0],[0,0,1,1],
                 [0,0,0,1],[1,0,0,1]] 

''' 
step_sequence = [[0,1,1,1],[0,0,1,1], # Clockwise
                 [1,0,1,1],[1,0,0,1],
                 [1,1,0,1],[1,1,0,0],
                 [1,1,1,0],[0,1,1,0]] 


''' '''
step_sequence = [[1,0,0,1],[0,0,0,1], # Clockwise
                 [0,0,1,1],[0,0,1,0],
                 [0,1,1,0],[0,1,0,0],
                 [1,1,0,0],[1,0,0,0]]
'''
# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

# Run the motor
for i in range(num_steps):
    for step in range(8):
        for pin in range(1):
            GPIO.output(ControlPin[1], step_sequence[step][1])
            GPIO.output(ControlPin[2], step_sequence[step][2])
            GPIO.output(ControlPin[3], step_sequence[step][3])
            GPIO.output(ControlPin[4], step_sequence[step][4])
        
        time.sleep(delay)

# Clean up the GPIO pins 
GPIO.cleanup()
print("Goodbye")
