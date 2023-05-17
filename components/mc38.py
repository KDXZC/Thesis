import RPi.GPIO as GPIO
from time import sleep

class MC38:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def is_closed(self):
        return GPIO.input(self.pin) == GPIO.LOW
    
    def __del__(self):
        GPIO.cleanup()

if __name__ == '__main__':
    #mc38 = MC38(17)
    #mc38 = MC38(25)
    mc38 = MC38(22)
    while True:
        print(mc38.is_closed())
        sleep(1)
