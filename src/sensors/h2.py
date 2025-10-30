from machine import ADC, Pin

class H2:
    def __init__(self, pin_no: int):
        adc = ADC(Pin(pin_no))
        self.adc = adc
    
    def readraw(self):
        return self.adc.read_u16()

    def read(self):
        voltage = self.readraw() * 3.3 / 65535
        h2_ppm = max(0, (voltage - 0.1) * 400)
        return h2_ppm
    
    def close(self):
        pass
