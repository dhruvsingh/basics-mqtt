# -*- coding: utf-8 -*-
"""Publisher.

Reference:
https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
"""
import time

import paho.mqtt.client as mqtt

host = 'localhost'


if __name__ == '__main__':
    c2 = mqtt.Client(client_id='c2')
    c2.connect(host, 1883, 60)

    while True:
        c2.publish("/test/world", "world")
        time.sleep(2)

    c2.disconnect()
