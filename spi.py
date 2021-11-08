""" create udev rule:
SUBSYSTEM=="spidev", GROUP="spiuser", MODE="0660"
"""
import atexit
import spidev

class Spi:
    def __init__(self, device):
        bus = 0
        self.spi = spidev.SpiDev()
        atexit.register(self.spi.close)
        self.spi.open(bus, device)
        # spi write goes up to 50MHz, read only 20MHz
        self.spi.max_speed_hz = 20_000_000
        self.spi.mode = 1

    def transceive(self, data):
        return self.spi.xfer2(data)
