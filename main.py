import json
import time
from umqtt.simple import MQTTClient
from settings import read_client, queue_topic, mq_host
from led import red, green, blue


def sub_cb(topic, msg):
    value = json.loads(msg)["value"]
    colour = json.loads(msg)["colour"]
    print("colour is {}, value is {}".format(colour, value))
    if colour == "red":
        red(value)
    elif colour == "green":
        green(value)
    elif colour == "blue":
        blue(value)


while True:
    c = MQTTClient(read_client, mq_host, port=1883, ssl=False)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(str.encode(queue_topic))
    while True:
        if True:
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(1)

    c.disconnect()
