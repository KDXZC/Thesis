import RPi.GPIO as GPIO

from components.led import LED
from components.mc38 import MC38
from components.relay import Relay
from components.ultrasonic import Ultrasonic
from mqtt import MQTTClient
from time import sleep

class HardwareController:
    def __init__(self):
        GPIO.cleanup()
        
        self.relay1 = Relay(21)
        self.relay2 = Relay(23)
        self.relay3 = Relay(24)
        
        self.mc38_1 = MC38(17)
        self.mc38_2 = MC38(25)
        self.mc38_3 = MC38(22)
        
        self.ultrasonic1 = Ultrasonic(trigger_pin = 11, echo_pin = 12)
        self.ultrasonic2 = Ultrasonic(trigger_pin = 5, echo_pin = 6)
        self.ultrasonic3 = Ultrasonic(trigger_pin = 13, echo_pin = 19)
        
    def request_open_door(self, slot_code):
        if (slot_code == "A01"):
            self.relay1.turn_on()
            print("Hardware Controller : relay1 turned on --> door unlocked")
            return True

        elif (slot_code == "A02"):
            self.relay2.turn_on()
            print("Hardware Controller : relay2 turned on --> door unlocked")
            return True
            
        elif (slot_code == "A03"):
            self.relay3.turn_on()
            print("Hardware Controller : relay3 turned on --> door unlocked")
            return True
            
    def request_close_door(self, slot_code):
        if (slot_code == "A01"):
            self.relay1.turn_off()
            print("Hardware Controller : relay1 turned off --> door locked")
            return True

        elif (slot_code == "A02"):
            self.relay2.turn_off()
            print("Hardware Controller : relay2 turned off --> door locked")
            return True
            
        elif (slot_code == "A03"):
            self.relay3.turn_off()
            print("Hardware Controller : relay3 turned off --> door locked")
            return True
            
    def request_check_plant(self, slot_code):
        if (slot_code == "A01"):
            print("Hardware Controller : ultrasonic1 object detected? =", self.ultrasonic1.detect())
            return self.ultrasonic1.detect()

        elif (slot_code == "A02"):
            print("Hardware Controller : ultrasonic2 object detected? =", self.ultrasonic2.detect())
            return self.ultrasonic2.detect()
            
        elif (slot_code == "A03"):
            print("Hardware Controller : ultrasonic3 object detected? =", self.ultrasonic3.detect())
            return self.ultrasonic3.detect()
    
    def request_pickup(self, slot_code):
        slot_state1 = 0
        slot_state2 = 0
        slot_state3 = 0
        print("slot_state1 :", slot_state1)
        print("slot_state2 :", slot_state2)
        print("slot_state3 :", slot_state3)
        
        if (slot_code == "A01"):
            self.relay1.turn_on()
            print("Hardware Controller : relay1 turned on --> door unlocked")
            while True:
                print(self.mc38_1.is_closed())
                if (slot_state1 == 0):
                    print("Hardware Controller : mc38_1 closed? =", self.mc38_1.is_closed())
                    if (self.mc38_1.is_closed() == False):
                        slot_state1 = 1
                        print("slot_state :", slot_state1)

                if (slot_state1 == 1):
                    print("-------")
                    print("Hardware Controller : ultrasonic1 object detected? =", self.ultrasonic1.detect())
                    if (self.ultrasonic1.detect() == False):
                        slot_state1 = 2
                        print("slot_state :", slot_state1)

                if (slot_state1 == 2):
                    print("Hardware Controller : mc38_1 closed? =", self.mc38_1.is_closed())
                    if (self.mc38_1.is_closed()):
                        self.relay1.turn_off()
                        print("Hardware Controller : relay1 turned off --> door locked")
                        break

                sleep(1)
                print("slot_state after sleep :", slot_state1)
        
        elif (slot_code == "A02"):
            self.relay2.turn_on()
            print("Hardware Controller : relay2 turned on --> door unlocked")
            while True:
                print(self.mc38_2.is_closed())
                if (slot_state2 == 0):
                    print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed() == False):
                        slot_state2 = 1
                        print("slot_state :", slot_state2)

                if (slot_state2 == 1):
                    print("-------")
                    print("Hardware Controller : ultrasonic2 object detected? =", self.ultrasonic2.detect())
                    if (self.ultrasonic2.detect() == False):
                        slot_state2 = 2
                        print("slot_state :", slot_state2)

                if (slot_state2 == 2):
                    print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed()):
                        self.relay2.turn_off()
                        print("Hardware Controller : relay2 turned off --> door locked")
                        break

                sleep(1)
                print("slot_state after sleep :", slot_state2)
    
        elif (slot_code == "A03") :
            self.relay3.turn_on()
            print("Hardware Controller : relay3 turned on --> door unlocked")
            while True:
                print(self.mc38_3.is_closed())
                if (slot_state3 == 0):
                    print("Hardware Controller : mc38_3 closed? =", self.mc38_3.is_closed())
                    if (self.mc38_3.is_closed() == False):
                        slot_state3 = 1
                        print("slot_state :", slot_state3)

                if (slot_state3 == 1):
                    print("-------")
                    print("Hardware Controller : ultrasonic2 object detected? =", self.ultrasonic3.detect())
                    if (self.ultrasonic3.detect() == False):
                        slot_state3 = 2
                        print("slot_state :", slot_state3)

                if (slot_state3 == 2):
                    print("Hardware Controller : mc38_3 closed? =", self.mc38_3.is_closed())
                    if (self.mc38_3.is_closed()):
                        self.relay3.turn_off()
                        print("Hardware Controller : relay3 turned off --> door locked")
                        break

                sleep(1)
                print("slot_state after sleep :", slot_state3)

