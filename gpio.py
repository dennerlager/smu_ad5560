import abc
try:
    from RPi import GPIO as gpio
except ImportError:
    from mockRPi import GPIO as gpio

class Gpio(abc.ABC):
    def __init__(self, channel):
        gpio.setmode(gpio.BOARD)
        self.channel = channel
        self.setup()

    @abc.abstractmethod
    def setup(self):
        pass

    def __del__(self):
        gpio.cleanup(self.channel)

    def read(self):
        return gpio.input(self.channel)

class Output(Gpio):
    def setup(self):
        gpio.setup(self.channel, gpio.OUT, initial=gpio.LOW)

    def set(self):
        gpio.output(self.channel, gpio.HIGH)

    def clear(self):
        gpio.output(self.channel, gpio.LOW)

    def toggle(self):
        gpio.output(self.channel, not gpio.input(self.channel))

class Input(Gpio):
    def setup(self):
        gpio.setup(self.channel, gpio.IN)
