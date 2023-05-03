import RPi.GPIO as GPIO

class LED:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_number, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin_number, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin_number, GPIO.LOW)

    def toggle(self):
        state = GPIO.input(self.pin_number)
        if state == GPIO.HIGH:
            self.off()
        else:
            self.on()

    def cleanup(self):
        GPIO.cleanup()
