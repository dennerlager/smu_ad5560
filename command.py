import struct

class Command:
    def __init__(self, commandName, address, data=0):
        self.commandName = commandName
        self.readWriteNotBit = {'read': 1, 'write': 0}[commandName]
        self.address = address
        self.data = data

    def toBytes(self):
        return struct.pack('BH',
                           ((self.readWriteNotBit << 7) | self.address),
                           self.data)

    def __repr__(self):
        return (f'{self.commandName}, ' +
                f'address: 0x{self.address:02x}, ' +
                f'data: 0x{self.data}:04x')
