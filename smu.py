from contextlib import contextmanager

from memory import Memory
from gpio import Input, Output
from interface import Interface

class Smu:
    """
    osd dac:
    vref*(dac_code/2**16)

    dutgnd dac:
    vref*(dac_code/2**16)

    offset and gain register:
    x2 = [x1*(m + 1)/2**n] + (c – 2**(n – 1))
    x2 is the data-word loaded to the resistor string DAC
    x1 is the 16-bit data-word written to the DAC input register
    m is the code in the gain register (default code = 2**16 – 1)
    n is the DAC resolution (n = 16)
    c is the code in the offset register (default code = 2 15 )

    xorsense: sense resistor
    m1_amp_gain: gain of m1 amp (either 10 or 20)
    The 20 gain setting is intended for use with a 5 V reference

    spiAdc(miso, sclk)

    alarm leds
    kelvin alarm
    dutgnd sense alarm (kelvin alarm for gnd)
    clamp alarm
    system force/sense switches:
    system force/sense switches allow easy connection of a central
    or system parametric measurement unit (pmu) for calibration
    or additional measurement purposes.
    """

    def __init__(self):
        self.interface = Interface()
        self.memory = Memory()
        self.resetb = Output('resetb')
        self.hwInhibitb = Output('hw_inhibitb')
        self.adcConvert = Output('adcconvert')
        self.clampEnable = Output('clen')
        self.clampAlarmb = Input('clalmb')
        self.kelvinAlarmb = Input('kelalb')
        self.temperatureAlarmb = Input('tempalb')

    def readRegister(self, registername):
        address = self.memory.registers[registername]
        read = Command('read', address).toBytes()
        nop = Command('read', nop).toBytes()
        bytestream = self.interface.transceive(read + nop)
        response = Response(bytestream[-3])
        if not response.address == address:
            raise RuntimeError(f'received address 0x{response.address:02x}' +
                               f'does not match 0x{address:02x}')
        return response.data

    def writeRegister(self, registername, value):
        address = self.memory.registers[registername]
        self.interface.transceive(Command('write', address, data).toBytes())
        if not self.readRegister(registername) == value:
            raise RuntimeError(f'cannot write {registername} to 0x{value:02x}')

    def setBitInRegister(self, registername, bit):
        if not 0 <= bit <= 7:
            raise ValueError(f'bit cannot be {bit}')
        self.writeRegister(registername, self.readRegister(registername) | 2**bit)

    def clearBitInRegister(self, registername, bit):
        if not 0 <= bit <= 7:
            raise ValueError(f'bit cannot be {bit}')
        self.writeRegister(registername, self.readRegister(registername) &
                           (2**bit ^ 0xff))

    def forceVoltageMode(self):
        pass

    def forceCurrentMode(self):
        pass

    def setVoltage_V(self, voltage_V):
        """
        vout = (5.125*vref*(dac_code/2**16) -
                5.125*vref*(offset_dac_code/2**16) +
                dut_gnd)
        """

    def setCurrent_mA(self, current_mA):
        pass

    def setVoltageCompliance_V(self, voltage_V):
        """
        vclh, vcll = (5.125*vref*(dac_code/2**16) -
              5.125*vref*(offset_dac_code/2**16) +
              dut_gnd)
        """

    def setCurrentCompliance_mA(self, current_mA):
        """
        icll, iclh = ((5.125*vref*((dac_code-32768)/2**16)) /
                     (rsense*m1_amp_gain))
        """

    def measureVoltage_V(self):
        pass

    def measureCurrent_mA(self):
        pass

    def outputOn(self):
        pass

    def outputOff(self):
        pass

    @contextmanager
    def keepOutputOnDuring(self):
        """Use this function context manager like:
        with Smu().keepOutputOnDuring():
            self.do_something"""
        self.outputOn()
        try:
            yield
        finally:
            self.outputOff()
