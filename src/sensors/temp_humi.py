
from machine import Pin
from dht import DHT11

class TempHumi:
    def __init__(self, pin_no):
        dht = DHT11(Pin(pin_no))
        self.dht = dht

    def read(self):
        self.dht.measure()
        return self.dht.temperature(), self.dht.humidity()
