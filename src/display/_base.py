
class Display:
    pass

from machine import Pin, SPI


class SPIDisplay(Display):
    def __init__(self, spi_id=0, bps=10_000_000, polarity=0, phase=0,
                 bits=8, firstbit=SPI.MSB, sck_pin=18, mosi_pin=19, miso_pin=16):

        self.__spi = SPI(spi_id,
                 baudrate=bps,
                 polarity=polarity,
                 phase=phase,
                 bits=bits,
                 firstbit=firstbit,
                 sck=Pin(sck_pin),
                 mosi=Pin(mosi_pin),
                 miso=Pin(miso_pin))




