import RPi.GPIO as GPIO
from time import sleep

class Relay:
    def __init__(self, pin):
        self.pin = pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print("Relay turned on")

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        print("Relay turned off")


if __name__ == '__main__':
    relay = Relay(21)
    #relay = Relay(23)
    #relay = Relay(24)
    
#     while True:
#         relay.turn_on()
#         sleep(5)
#         relay.turn_off()
#         sleep(1)
    relay.turn_on()
    sleep(3)
    relay.turn_off()
    
    GPIO.cleanup()
        
