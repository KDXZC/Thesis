import RPi.GPIO as GPIO
import time

class InfraredSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        
    def object_detected(self):
        if (GPIO.input(self.pin)):
            time.sleep(0.5)
            if GPIO.input(self.pin):
                GPIO.cleanup(self.pin)
                GPIO.setup(self.pin, GPIO.IN)
                return True
        return False
        
        