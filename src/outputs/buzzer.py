from machine import PWM, Pin


class Buzzer(object):
    def __init__(self, pin_no):
        buzzer = PWM(Pin(pin_no))
        self.buzzer = buzzer

    def set(self, frequency=1000, duration=1.0):
        """Generate a beep on the buzzer."""
        self.buzzer.freq(frequency)  # Set frequency
        self.buzzer.duty_u16(32768)  # 50% duty cycle (range 0–65535)
        self.sleep(duration)  # Wait while tone plays
        self.buzzer.duty_u16(0)  # Turn off the buzzer

