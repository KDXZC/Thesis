import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic, username, password, message_handler=None):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = message_handler if message_handler else self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
        #if msg.payload.decode() in ['0', '1']:
            #self.send_message(self.topic, msg.payload.decode())

    def connect(self):
        self.client.connect(self.broker, self.port, 60)

    def start(self):
        self.connect()
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def send_message(self, topic, message):
        self.client.publish(topic, message)