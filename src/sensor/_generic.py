
from machine import Pin
import dht as dht_sensor

from ._base import Sensor


class DHT11 (Sensor):
    def __init__(self, pin_no):
        dht = dht_sensor.DHT11(Pin(pin_no))
        self.dht = dht

    def read(self):
        self.dht.measure()
        return self.dht.temperature(), self.dht.humidity()
