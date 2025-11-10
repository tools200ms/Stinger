
from src.serial._base import Serial

from machine import UART, Pin


class UART(Serial):
    def __init__(self, tx_pin_no: int, rx_pin_no: int, bps: int):
        self.__uart = UART(0, baudrate=bps, tx=Pin(tx_pin_no), rx=Pin(rx_pin_no))

    def read(self):
        return self.__uart.read()

    def write(self, text):
        self.__uart.write(text)

