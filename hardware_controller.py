from components.led import LED
from components.mc38 import MC38
from components.relay import Relay
from components.ultrasonic import Ultrasonic
import RPi.GPIO as GPIO

from time import sleep

class HardwareController:
    def __init__(self):
        #relay1 = Relay(18)
        self.relay2 = Relay(23)
        #relay3 = Relay(24)
        
        #mc38_1 = MC38(17)
        self.mc38_2 = MC38(17)
        #mc38_3 = MC38(22)
        
        #ultrasonic1 = Ultrasonic(trigger_pin = 11, echo_pin = 12)
        self.ultrasonic2 = Ultrasonic(trigger_pin = 13, echo_pin = 19)
        #ultrasonic3 = Ultrasonic(trigger_pin = 13, echo_pin = 19)
        
    def open_slot_door(self, slot_code):
        slot_state = 0
        print("slot_state :", slot_state)
        
        if (slot_code == "A01"):
            pass
        elif (slot_code == "A02"):
            self.relay2.turn_on()
            print("Hardware Controller : relay2 turned off --> door unlocked")
            while True:
                print(self.mc38_2.is_closed())
                if (slot_state == 0):
                    print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed() == False):
                        slot_state = 1
                        print("slot_state :", slot_state)

                if (slot_state == 1):
                    print("-------")
                    print("Hardware Controller : ultrasonic2 object detected? =", self.ultrasonic2.detect())
                    if (self.ultrasonic2.detect() == False):
                        slot_state = 2
                        print("slot_state :", slot_state)

                if (slot_state == 2):
                    print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed()):
                        self.relay2.turn_off()
                        print("Hardware Controller : relay2 turned off --> door locked")
                        break

                sleep(1)
                print("slot_state after sleep :", slot_state)
    
    """
    def open_slot_door(self, slot_code):
        # slot_state = 0 --> before open the door
        # slot_state = 1 --> after open the door
        
        #self.relay2.turn_on()
        slot_state = 0
        print("slot_state :", slot_state)
        
        if (slot_code == "A01"):
            pass
        elif (slot_code == "A02"):
            self.relay2.turn_on()
            print("Hardware Controller : relay2 turned on --> door unlocked")
            
            while True:
                if (slot_state == 0):
                    # change state when the door is opened
                    #print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed() == False):
                        slot_state = 1
                        print("slot_state :", slot_state)
                        
                if (slot_state == 1):
                    # change state when the plant is pick up
                    print("-------")
                    print("Hardware Controller : ultrasonic2 object detected? =", self.ultrasonic2.detect())
                    if (self.ultrasonic2.detect() == False):
                        slot_state = 2
                        print("slot_state :", slot_state)
                        
                if (slot_state == 2):
                    # lock the door when it's closed
                    print("Hardware Controller : mc38_2 closed? =", self.mc38_2.is_closed())
                    if (self.mc38_2.is_closed()):
                        self.relay2.turn_on()
                        print("Hardware Controller : relay2 turned off --> door locked")
                        break
                sleep(1)
                print("slot_state after sleep :", slot_state)
            
            
            if ultrasonic2.detect() == False and mc382.is_closed():
                print("In Condition")
                relay2.turn_off()
                break
            sleep(1)
            
            
        elif (slot_code == "A03") :
            pass
        """

if __name__ == "__main__":
    door_controller = HardwareController()
    door_controller.monitor_door()
