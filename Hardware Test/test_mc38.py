import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_MAG = 27
GPIO.setup(GPIO_MAG, GPIO.IN)

while True:
    if GPIO.input(GPIO_MAG) == GPIO.HIGH:
        print("Door Closed")
    if GPIO.input(GPIO_MAG) == GPIO.LOW:
        print("Door Open")
    time.sleep(1)
    
GPIO.cleanup()