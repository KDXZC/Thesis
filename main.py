import json

from mqtt import MQTTClient
from request_handler import RequestHandler
from components.mc38 import MC38

request_handler = RequestHandler()

sub_pickup_topic = "server/request_pickup"
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
        

def main():
    #broker = "172.20.10.2"
    broker = "localhost"
    port = 1883
    username = "myhome"
    password = "myraspi"
    
    mqtt_client = MQTTClient(broker, port, sub_pickup_topic, username, password, custom_message_handler)
    mqtt_client.start()
    
    
    while True:
        pass

            
        
if __name__ == '__main__':
    main()