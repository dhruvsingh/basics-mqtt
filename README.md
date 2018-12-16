# basics-mqtt
MQTT basics with paho-mqtt 

Problem statement

Simple "Hello World" MQTT PUB/SUB app.

- Subscriber should listen to the topic "/test" (subscriber listens to two topics here, the ones that publishers publish to)
- First publisher, with "/test /hello" sends "hello" every 1 second (feel free to use time.sleep(1))
- Second publisher, with the "/test /world" sends "world" every 2 second


Steps to run:

1. Create a Py3 virtual environment, activate the same; do this on 3 terminals.
2. On each terminal:  
  2.1 `python subscriber.py`  
  2.2 `python publisher1.py`  
  2.3 `python publisher2.py`  
3. On the first terminal you'll be able to see *hello* twice and *world* printed once on the terminal.
