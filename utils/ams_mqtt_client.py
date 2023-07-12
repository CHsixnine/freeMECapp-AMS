import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

class AMS_MQTT_CLIENT():
    def __init__(self, BROKER_IP):
        self.client = mqtt.Client()
        self.BROKER_IP = BROKER_IP
        self.client.connect(BROKER_IP, 1883, 60)

    def recv(self, topic):
        self.topic = topic
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever()

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+ msg.payload.decode('utf-8'))
        pass

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe(self.topic)