# -*- coding: utf-8 -*-

"""
Subscriber.

Reference:
https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
"""

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    """On client connect."""
    print("Connected with result code " + str(rc))
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    """On sending a message."""
    if msg.payload.decode() == "Hello world!":
        print("Yes!")
        client.disconnect()

client = mqtt.Client()
client.connect("THE_IP_ADDRESS_OF_OUR_BROKER", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
