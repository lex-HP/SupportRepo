#Stepper motor can now be controlled from keyboard

import RPi.GPIO as GPIO
import time
import keyboard
import threading

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

def Motor_Control(direction):
    if direction == "Left":
        for i in range(num_steps):
            for step in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], step_sequence[step][pin])
                time.sleep(delay)
    elif direction == "Right":
        for i in range(num_steps):
            for step in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], step_sequence[7-step][pin])
                time.sleep(delay)
    else:
        pass

# Threading 
direction = "None"
motor_thread = threading.Thread(target=Motor_Control, args=(direction,))
motor_thread.start()

# keyboard listen
delay_control = 0.1
print('Press "a" to go clockwise, "d" to go counter-clockwise and space to quit\n')
while True:
    if keyboard.is_pressed('space'):
        print("Goodbye")
        break
    if keyboard.is_pressed("a"):
        direction = "Left"
        motor_thread._stop()
        motor_thread = threading.Thread(target = Motor_Control, args =(direction,))
        motor_thread.start()
        print('"L|"')
        time.sleep(delay_control)
    if keyboard.is_pressed("d"):
        direction = "Right"
        motor_thread._stop()
        motor_thread = threading.Thread(target = Motor_Control, args =(direction,))
        motor_thread.start()
        print('"R|"')
        time.sleep(delay_control)


GPIO.cleanup()
'''


# Run the motor
for i in range(num_steps):
    for step in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], step_sequence[step][pin])
        time.sleep(delay)

# Clean up the GPIO pins 

'''