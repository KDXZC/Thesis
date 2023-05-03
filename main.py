import json

from mqtt import MQTTClient
from request_handler import RequestHandler
from components.mc38 import MC38

request_handler = RequestHandler()

sub_pickup_topic = "backend/request_pickup"
pub_pickup_topic = "controller/pickup_status"

def custom_message_handler(client, userdata, msg):
    
        # payload decoding
        #message = msg.payload.decode()
        
        # topic
        topic = msg.topic
        print("Main : Received payload on Topic =", topic)
        
        # payload decoding
        payload = json.loads(msg.payload)
        print("Main : Received JSON payload =", payload)
        
        if (topic == sub_pickup_topic) :
            # request pick up from 'slot manager'
            result_payload = request_handler.request_pickup(payload)
            pass
        elif (topic == "") :
            pass
        
        """
        if message == "1":
            print(f"Received message: {message} on topic {msg.topic}")
            
            if msg.topic == "backend/door1":
                print("This is a message for backend/door1")
                #sensor code here
                relay1 = Relay(18)
                while True:
                    relay1.turn_on()
                
            elif msg.topic == "backend/door2":
                print("This is a message for backend/door2")
                #sensor code here
                relay2 = Relay(23)
                mc382 = MC38(17)
                ultrasonic2 = Ultrasonic(trigger_pin = 5, echo_pin = 6)
                
                while True:
                    #distance = ultrasonic2.distance()
                    relay2.turn_on()
                    print(ultrasonic2.detect())
                    print(mc382.is_closed())
                    #print(distance)
                    if ultrasonic2.detect() == False and mc382.is_closed():
                        print("In Condition")
                        relay2.turn_off()
                        break
                    sleep(1)
                
            elif msg.topic == "backend/door3":
                print("This is a message for backend/door3")
                #sensor code here
                relay3 = Relay(24)
                relay3.turn_on()
        """
        

def main():
    broker = "172.20.10.2"
    port = 1883
    username = "myhome"
    password = "myraspi"
    
    #topic1 = "backend/door1"
    #topic2 = "backend/door2"
    #topic3 = "backend/door3"
    
    mqtt_client = MQTTClient(broker, port, sub_pickup_topic, username, password, custom_message_handler)
    mqtt_client.start()
    
    #mqtt_client1 = MQTTClient(broker, port, topic1, username, password, custom_message_handler)
    #mqtt_client2 = MQTTClient(broker, port, topic2, username, password, custom_message_handler)
    #mqtt_client3 = MQTTClient(broker, port, topic3, username, password, custom_message_handler)
    
    #mqtt_client1.start()
    #mqtt_client2.start()
    #mqtt_client3.start()
    
    while True:
        pass

#     mc382 = MC38(27)
#     while True:
#         if mc382.is_closed():
#             print("Door is close!")
#         else:
#             print("Door is open!")
         
    
    
    #except KeyboardInterrupt:
        #mqtt_client.stop()
        #mqtt_client2.stop()
        #mqtt_client3.stop()
    
#     relay1 = Relay(18)
#     relay2 = Relay(23)
#     relay3 = Relay(24)
#     
#     mc381 = MC38(17)
#     mc382 = MC38(27)
#     mc383 = MC38(22)
#     
#     sensor1 = Ultrasonic(trigger_pin = 11, echo_pin = 12)
#     sensor2 = Ultrasonic(trigger_pin = 5, echo_pin = 6)
#     sensor3 = Ultrasonic(trigger_pin = 13, echo_pin = 19)

#      while True:
#         
# ##Ultrasonic Sensor
#          distance = sensor1.distance()
#          print(distance)
#
#          if(sensor1.detect()):
#              print("Object detected within 5 cm!")
#          else:
#              print("No object detected")
#          sleep(0.5)
#         
#         distance = sensor2.distance()
#         print(distance)
# 
#         if(sensor2.detect()):
#             print("Object detected within 5 cm!")
#         else:
#             print("No object detected")
#         sleep(0.5)
#         
#         distance = sensor3.distance()
#         print(distance)
# 
#         if(sensor3.detect()):
#             print("Object detected within 5 cm!")
#         else:
#             print("No object detected")
#         sleep(0.5)
        
##Relay
#          relay1.turn_on()
#          sleep(1)
#          relay1.turn_off()
#          sleep(1)
#          
#          relay2.turn_on()
#          sleep(1)
#          relay2.turn_off()
#          sleep(1)
#          
#          relay3.turn_on()
#          sleep(1)
#          relay3.turn_off()
#          sleep(1)
         
##MC38         
#          if mc381.is_closed():
#              print("Door is close!")
#          else:
#              print("Door is open!")
#              
#          if mc382.is_closed():
#              print("Door is close!")
#          else:
#              print("Door is open!")
#              
#          if mc383.is_closed():
#              print("Door is close!")
#          else:
#              print("Door is open!")
            
        
if __name__ == '__main__':
    main()