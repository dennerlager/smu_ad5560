from spi import Spi
from gpio import Input

class Interface:
    def __init__(self):
        self.spi = Spi()
        self.busyb = Input('busyb')

    def transceive(self, bytestream):
        for _ in range(100):
            if self.busyb.read():
                break
        else:
            raise RuntimeError('spi busy')
        return self.spi.transceive(bytestream)
