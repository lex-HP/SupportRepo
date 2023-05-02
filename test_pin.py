import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_pin = int(input("Give physical pin number: "))

GPIO.setup(pin, GPIO.OUT)
start_time = time.time()

while (time.time() - start_time) < 5:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)

# clean up GPIO
GPIO.cleanup()
