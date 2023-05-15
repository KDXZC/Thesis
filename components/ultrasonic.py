import RPi.GPIO as GPIO
import time
from time import sleep

class Ultrasonic:
    def __init__(self, trigger_pin, echo_pin):
        
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.trigger_pin, GPIO.OUT)
            GPIO.setup(self.echo_pin, GPIO.IN)
            GPIO.output(self.trigger_pin, GPIO.LOW)
            time.sleep(2)
        except Exception as e:
            print("Error initializing Ultrasonic sensor:", e)
            GPIO.cleanup()
            raise e

    def distance(self):
        timeout = 0.1
        StartTime = time.time()
        StopTime = time.time()
        GPIO.output(self.trigger_pin, True)
        GPIO.output(self.trigger_pin, False)
        
        
        loop_start_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            StartTime = time.time()
            if time.time() - loop_start_time > timeout:
                break

        loop_start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            StopTime = time.time()
            if time.time() - loop_start_time > timeout:
                break
        
        TimeElasped = StopTime - StartTime
        distance = (TimeElasped * 34300) / 2
        distance = round(distance, 2)

        return distance
        

    def detect(self):
        distance = self.distance()
        print("distance :", distance)
        if distance < 10:
            return True
        else:
            return False

    def cleanup(self):
        GPIO.cleanup()
        
if __name__ == '__main__':
    ultrasonic1 = Ultrasonic(trigger_pin = 11, echo_pin = 12)
    ultrasonic2 = Ultrasonic(trigger_pin = 5, echo_pin = 6)
    ultrasonic3 = Ultrasonic(trigger_pin = 13, echo_pin = 19)
    while True:
        print(ultrasonic3.distance())
        sleep(1)