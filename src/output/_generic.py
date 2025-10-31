import time

from machine import PWM, Pin

from ._base import Output


class Buzzer(Output):
    def __init__(self, pin_no):
        buzzer = PWM(Pin(pin_no))
        self.buzzer = buzzer

    def set(self, frequency=1000, duration=1.0):
        """Generate a beep on the buzzer."""
        self.buzzer.freq(frequency)  # Set frequency
        self.buzzer.duty_u16(32768)  # 50% duty cycle (range 0–65535)
        self.sleep(duration)  # Wait while tone plays
        self.buzzer.duty_u16(0)  # Turn off the buzzer


class LED(Output):
    def __init__(self, pin_no):
        pin = Pin(pin_no, Pin.OUT)
        self.pin = pin

    def set(self, duration=1.0):
        self.pin.value(1)
        time.sleep(duration)
        self.pin.value(0)

