"""Force-sensitive resistors (FSR) are a class of pressure sensors."""

import json
from time import sleep

from core import mqtt_client
from secrets import secrets

mqtt_client.connect()

def loop():
    payload = 
    mqtt_client.publish(secrets['TOPIC'], json.dumps(payload))
    sleep(10)


if __name__ == '__main__':
    loop()