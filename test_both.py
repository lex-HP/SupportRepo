# Inpired by VL53L4CD APi documentation from: Copyright (c) 2022 Carter Nelson for Adafruit Industries

# Simple demo of the VL53L4CD distance sensor.
# Will print the sensed range/distance every second.

import board
import adafruit_vl53l4cd

import RPi.GPIO as GPIO
import time

print("Hello")

# Set constants
ControlPin = [11, 13, 15, 16] # Set the GPIO pins for the motor
num_steps = 256 # Set the number of step
delay = 0.001 # Set delay between steps

step_sequence = [[1,0,0,0],[1,1,0,0], # Counter-Clockwise
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
        for pin in range(1):
            GPIO.output(ControlPin[0], step_sequence[step][0])
            GPIO.output(ControlPin[2], step_sequence[step][2])
            GPIO.output(ControlPin[1], step_sequence[step][1])
            GPIO.output(ControlPin[3], step_sequence[step][3])
        
        time.sleep(delay)

# Clean up the GPIO pins 
GPIO.cleanup()



def run_sensor():
    # set constants
    min_distance = 5 # in cm
    timing_budget = 50
    inter_measurement = 0

    # start script
    print("Hello")
    print("--------------------")
    flag = 0

    i2c = board.I2C()  # uses board.SCL and board.SDA
    ToF = adafruit_vl53l4cd.VL53L4CD(i2c)
    ToF.inter_measurement = inter_measurement
    ToF.timing_budget = timing_budget

    ToF.start_ranging()  # start measurments
    for i in range(100):
        while not ToF.data_ready:
            pass
        ToF.clear_interrupt()
        print("Distance: {} cm".format(ToF.distance))
        if ToF.distance <= min_distance and ToF.distance != 0.0:
            flag = 1
            print("too close")

    print("--------------------")
    print("Goodbye")
    return 1

if __name__ == "__main__":
    run_sensor()

print("Goodbye")