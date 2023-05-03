from hardware_controller import HardwareController

class RequestHandler:
    def __init__(self):
        self.hardware_controller = HardwareController()
        pass

    def request_pickup(self, payload):
        #relay2 = Relay(23)
        #mc382 = MC38(17)
        #ultrasonic2 = Ultrasonic(trigger_pin = 5, echo_pin = 6)
                
        #distance = ultrasonic2.distance()
        requested_slot_code = payload.get('slot_code')
        print("Request Handler : requested to open slot =", requested_slot_code)
        self.hardware_controller.open_slot_door(requested_slot_code)
            
            
        """
        relay2.turn_on()
        print(ultrasonic2.detect())
        print(mc382.is_closed())
        #print(distance)
        if ultrasonic2.detect() == False and mc382.is_closed():
            print("In Condition")
            relay2.turn_off()
            break
        sleep(1)
        """
