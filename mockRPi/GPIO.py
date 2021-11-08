'''gpio mock for testing'''

BOARD = None
IN = None
OUT = None
HIGH = None
LOW = None
PUD_UP = None
PUD_DOWN = None

def setmode(mode):
    pass

def setup(channel, mode, initial=LOW, pull_up_down=None):
    pass

def input(channel):
    return False

def output(channel, state):
    pass

def cleanup(channel):
    pass
