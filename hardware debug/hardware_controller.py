from mc38 import MC38

from time import sleep

class HardwareController:
    def __init__(self):
        self.mc38_2 = MC38(17)
        
    def monitor_door(self):
        while True:
            if self.mc38_2.is_closed():
                print("The door is closed.")
            else:
                print("The door is open.")
            sleep(1)
            

if __name__ == "__main__":
    door_controller = HardwareController()
    door_controller.monitor_door()
