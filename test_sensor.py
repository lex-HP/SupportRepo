# SPDX-FileCopyrightText: Copyright (c) 2022 Carter Nelson for Adafruit Industries

# Simple demo of the VL53L4CD distance sensor.
# Will print the sensed range/distance every second.

import board
import adafruit_vl53l4cd
print("Hello")
print("--------------------")
i2c = board.I2C()  # uses board.SCL and board.SDA
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)

# OPTIONAL: can set non-default values
ToF.inter_measurement = 0
ToF.timing_budget = 200

ToF.start_ranging()
for i in range(10):
    while not ToF.data_ready:
        pass
    ToF.clear_interrupt()
    print("Distance: {} cm".format(ToF.distance))
    if ToF.distance <= 10 and ToF.distance != 0.0:
        flag = 1
        print("too close")
print("--------------------")
print("Goodbye")