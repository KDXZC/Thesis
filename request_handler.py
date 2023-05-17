from hardware_controller import HardwareController

class RequestHandler:
    def __init__(self):
        self.hardware_controller = HardwareController()
        pass

    def request_pickup(self, slot_code):
        print("Request Handler : requested to pickup slot =", slot_code)
        self.hardware_controller.request_pickup(slot_code)
            
    def request_open(self, slot_code):
        print("Request Handler : requested to open slot =", slot_code)
        return self.hardware_controller.request_open_door(slot_code)
        
    def request_close(self, slot_code):
        print("Request Handler : requested to close slot =", slot_code)
        return self.hardware_controller.request_close_door(slot_code)
        
    def request_check_plant(self, slot_code):
        print("Request Handler : requested to check plant =", slot_code)
        return self.hardware_controller.request_check_plant(slot_code)
