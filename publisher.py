# -*- coding: utf-8 -*-
"""Publisher.

Reference:
https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
"""

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish("topic/test", "Hello world!")
client.disconnect()
