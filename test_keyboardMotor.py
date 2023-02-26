#Stepper motor can now be controlled from keyboard

import RPi.GPIO as GPIO
import time
import keyboard

print('Press "a" to go clockwise, "d" to go counter-clockwise and space to quit\n')
while True:
    if keyboard.is_pressed('space'):
        print("Goodbye")
        break
    if keyboard.is_pressed("a"):
        print('"L|"')
    if keyboard.is_pressed("d"):
        print('"R|"')

'''
# Set constants
ControlPin = [11, 13, 15, 16] # Set the GPIO pins for the motor
num_steps = 512 # Set the number of step
delay = 0.001 # Set delay between steps
step_sequence = [[1,0,0,0],[1,1,0,0], # Set the step sequence for the motor
                 [0,1,0,0],[0,1,1,0],
                 [0,0,1,0],[0,0,1,1],
                 [0,0,0,1],[1,0,0,1]] 

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

# Run the motor
for i in range(num_steps):
    for step in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], step_sequence[step][pin])
        time.sleep(delay)

# Clean up the GPIO pins 
GPIO.cleanup()
'''