#Simple demo of the stepper motor, does a full rotation

import RPi.GPIO as GPIO
import time

print("Hello")

# Set constants
ControlPin = [18, 27, 22, 23] # Set the GPIO pins for the motor
num_steps = 512 # Set the number of step
delay = 0.0008 # Set delay between steps

step_sequence = [[1,0,0,0],[1,1,0,0], 
                 [0,1,0,0],[0,1,1,0],
                 [0,0,1,0],[0,0,1,1],
                 [0,0,0,1],[1,0,0,1]] 
inverted_sequence = [[1^bit for bit in step] for step in step_sequence]
step_sequence = inverted_sequence

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

# Run the motor
for i in range(num_steps):
    for step in range(8):
        for pin in range(1):
            GPIO.output(ControlPin[0], step_sequence[step][0])
            GPIO.output(ControlPin[2], step_sequence[step][2])
            GPIO.output(ControlPin[1], step_sequence[step][1])
            GPIO.output(ControlPin[3], step_sequence[step][3])
        
        time.sleep(delay)

# Clean up the GPIO pins 
GPIO.cleanup()
print("Goodbye")
