import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL343(i2c)

while True:
    acceleration = accelerometer.acceleration
    print("Acceleration: X = {:.2f}g, Y = {:.2f}g, Z = {:.2f}g".format(*acceleration))
    time.sleep(1)
