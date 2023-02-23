import RPi.GPIO as GPIO
import time
import adafruit_vl53l4cd

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)  # SDA
GPIO.setup(5, GPIO.OUT)  # SCL

# Initialize the I2C bus
i2c = adafruit_vl53l4cd.I2C()
i2c.init_gpio()

# Initialize the VL53L4CD sensor
vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)

# OPTIONAL: can set non-default values
vl53.inter_measurement = 0
vl53.timing_budget = 200

print("VL53L4CD Simple Test.")
print("--------------------")
model_id, module_type = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Timing Budget: {}".format(vl53.timing_budget))
print("Inter-Measurement: {}".format(vl53.inter_measurement))
print("--------------------")

vl53.start_ranging()

while True:
    while not vl53.data_ready:
        pass
    vl53.clear_interrupt()
    print("Distance: {} cm".format(vl53.distance))
