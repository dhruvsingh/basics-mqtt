# -*- coding: utf-8 -*-
"""Publisher.

Reference:
https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
"""
import time

import paho.mqtt.client as mqtt

host = 'localhost'


if __name__ == '__main__':
    c1 = mqtt.Client(client_id='c1')
    c1.connect(host, 1883, 60)

    while True:
        c1.publish("/test/hello", "hello")
        time.sleep(1)

    c1.disconnect()
