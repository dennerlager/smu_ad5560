import struct

class Response:
    def __init__(self, bytestream):
        self.address, self.data = struct.unpack('BH', bytestream)
        self.address &= 0x7f

    def __repr__(self):
        return (f'address: 0x{self.address:02x}, ' +
                f'data: 0x{self.data:04x}')
