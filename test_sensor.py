# Inpired by VL53L4CD APi documentation from: Copyright (c) 2022 Carter Nelson for Adafruit Industries

# Simple demo of the VL53L4CD distance sensor.
# Will print the sensed range/distance every second.

import board
import adafruit_vl53l4cd
import busio


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
    #i2c = busio.I2C(board.SCL, board.SDA)  # use secondary I2C bus

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