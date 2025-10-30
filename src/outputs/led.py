import time

from machine import Pin


class LED():
    def __init__(self, pin_no):
        pin = Pin(pin_no, Pin.OUT)
        self.pin = pin

    def set(self, duration=1.0):
        self.pin.value(1)
        time.sleep(duration)
        self.pin.value(0)
