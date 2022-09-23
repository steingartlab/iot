import time
import json
import random
import time
import socketpool
import wifi
from adafruit_minimqtt.adafruit_minimqtt import MQTT

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Connecting to %s" % secrets["SSID"])
wifi.radio.connect(secrets["SSID"], secrets["PASSWORD"])
print("Connected to %s!" % secrets["SSID"])

### Feeds ###


# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    client.publish("hello", "world")
    # Subscribe to all changes on the onoff_feed.


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

mqtt_client = MQTT(broker=secrets["MQTT"],
                   port=secrets["PORT"],
                   socket_pool=pool)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

if __name__ == '__main__':
    while True:
        out = {'val': random.random()}
        mqtt_client.publish(secrets['TOPIC'], json.dumps(out))
        time.sleep(6)
