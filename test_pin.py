import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_pin = int(input("Give physical pin number: "))

for pin in GPIO_pin:
    GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)

# clean up GPIO
GPIO.cleanup()
