import RPi.GPIO as GPIO
import time

# set up GPIO mode and pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO_pins = [11, 13, 15, 16]

# set up GPIO pins as output
for pin in GPIO_pins:
    GPIO.setup(pin, GPIO.OUT)

# turn on each pin in sequence for 1 second
for pin in GPIO_pins:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)

# clean up GPIO
GPIO.cleanup()
