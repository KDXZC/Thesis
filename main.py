import json

from mqtt import MQTTClient
from request_handler import RequestHandler
from components.mc38 import MC38

request_handler = RequestHandler()

sub_open_door_topic = "server/request_open"
sub_close_door_topic = "server/request_close"
pub_door_topic = "controller/door_status"

sub_check_plant_topic = "server/check_plant"
pub_plant_topic = "controller/plant_status"

sub_pickup_topic = "server/request_pickup"
pub_pickup_topic = "controller/pickup_status"

def custom_message_handler(client, userdata, msg):
        
        # topic
        topic = msg.topic
        print("Main : Received payload on Topic =", topic)
        
        # payload decoding
        payload = json.loads(msg.payload)
        print("Main : Received JSON payload =", payload)
        
        slot_code = payload.get('slot_code')
        plant_id = payload.get('plant_id')
        
        if (topic == sub_pickup_topic) :
            result_payload = request_handler.request_pickup(slot_code)
            
            # TODO: pub_pickup_topic: success
            payload = {
                "slot_code": slot_code,
                "plant_id": plant_id,
                "status": "success"
            }
            message = json.dumps(payload)
            client.publish(pub_pickup_topic, message)
        
        elif (topic == sub_open_door_topic) :
            result = request_handler.request_open(slot_code)
            
            # TODO: pub_door_topic: opened
            payload = {
                "slot_code": slot_code,
                "plant_id": plant_id,
                "status": "opened"
            }
            message = json.dumps(payload)
            client.publish(pub_door_topic, message)
        
        elif (topic == sub_close_door_topic) :
            result = request_handler.request_close(slot_code)
            
            # TODO: pub_door_topic: closed
            payload = {
                "slot_code": slot_code,
                "plant_id": plant_id,
                "status": "closed"
            }
            message = json.dumps(payload)
            client.publish(pub_door_topic, message)
        
        elif (topic == sub_check_plant_topic) :
            result = request_handler.request_check_plant(slot_code)
            
            # TODO: pub_plant_topic: true / false
            payload = {
                "slot_code": slot_code,
                "plant_id": plant_id,
                "plant_detected": result
            }
            message = json.dumps(payload)
            client.publish(pub_plant_topic, message)
            
        

def main():
    #broker = "172.20.10.2"
    broker = "localhost"
    port = 1883
    username = "myhome"
    password = "myraspi"
    
    mqtt_client = MQTTClient(broker, port, '#', username, password, custom_message_handler)
    mqtt_client.start()
    
    
    while True:
        pass

            
        
if __name__ == '__main__':
    main()