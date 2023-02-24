# SPDX-FileCopyrightText: Copyright (c) 2022 Carter Nelson for Adafruit Industries

# Simple demo of the VL53L4CD distance sensor.
# Will print the sensed range/distance every second.

import board
import adafruit_vl53l4cd
print("Hello")
print("--------------------")
i2c = board.I2C()  # uses board.SCL and board.SDA
vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)

# OPTIONAL: can set non-default values
vl53.inter_measurement = 0
vl53.timing_budget = 200



vl53.start_ranging()

for i in range(10):
    while not vl53.data_ready:
        pass
    vl53.clear_interrupt()
    print("Distance: {} cm".format(vl53.distance))

print("--------------------")
print("Goodbye")