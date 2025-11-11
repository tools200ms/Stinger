
import dht as dht_sensor
from ._base import Sensor

from machine import Pin


class Button (Sensor):
    def __init__(self, pin_no):
        self.__btn = Pin(pin_no, Pin.IN, Pin.PULL_UP)

    def add_handler(self, handler):
        self.__btn.irq(trigger=Pin.IRQ_FALLING, handler=handler)

    def read(self):
        self.__btn.value()

class DHT11 (Sensor):
    def __init__(self, pin_no):
        dht = dht_sensor.DHT11(Pin(pin_no))
        self.dht = dht

    def read(self):
        self.dht.measure()
        return self.dht.temperature(), self.dht.humidity()


