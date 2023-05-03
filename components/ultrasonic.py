import RPi.GPIO as GPIO
import time

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
        """
        GPIO.output(GPIO_TRIGGER, True)
        #time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        # Measure time taken for echo to return
        start_time = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start_time = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            end_time = time.time()

        # Calculate distance in cm
        duration = end_time - start_time
        distance = duration * 17150
        distance = round(distance, 2)
        
        return distance
        """
        
        
        timeout = 0.1
        StartTime = time.time()
        StopTime = time.time()
        GPIO.output(self.trigger_pin, True)
        #time.sleep(0.00001)
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