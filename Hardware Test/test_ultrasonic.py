import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 13
GPIO_ECHO = 19
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Measure time taken for echo to return
    start_time = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO)==1:
        end_time = time.time()

    # Calculate distance in cm
    duration = end_time - start_time
    distance = duration * 17150
    distance = round(distance, 2)
    
    return distance

# Loop to continuously measure distance
while True:
    dist = distance()
    print("Distance: {} cm".format(dist))
    time.sleep(1)

# Clean up GPIO pins
GPIO.cleanup()
