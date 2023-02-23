import RPi.GPIO as GPIO
import busio
import time
import adafruit_vl53l4cd
import board

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
#GPIO.setup(3, GPIO.OUT)  # SDA
#GPIO.setup(5, GPIO.OUT)  # SCL

# Initialize the I2C bus
i2c = board.I2C() #SCL, and SDA


# Initialize the VL53L4CD sensor
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)

# OPTIONAL: can set non-default values
ToF.inter_measurement = 0
ToF.timing_budget = 200

print("VL53L4CD Simple Test.")
print("--------------------")
model_id, module_type = ToF.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Timing Budget: {}".format(ToF.timing_budget))
print("Inter-Measurement: {}".format(ToF.inter_measurement))
print("--------------------")

ToF.start_ranging()

while True:
    while not ToF.data_ready:
        pass
    ToF.clear_interrupt()
    print("Distance: {} cm".format(ToF.distance))