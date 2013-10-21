from serial import Serial
from struct import pack
import json

ESCAPE = '\x13'
START = '\x37'

COMMAND_HELLO = '\x01'
COMMAND_LEDS = '\x02'
COMMAND_CLEAR = '\x03'


def escape(data):
    return data.replace(ESCAPE, ESCAPE + ESCAPE)

def command_hello():
    ret = ESCAPE + START + COMMAND_HELLO
    return ret

def command_leds(leds):
    packed = [pack('BBB', rgb[1], rgb[0], rgb[2]) for rgb in leds]
    ret = ESCAPE + START + COMMAND_LEDS + chr(len(packed))
    for led in packed:
        ret += escape(led)
    return ret

def command_clear():
    ret = ESCAPE + START + COMMAND_CLEAR
    return ret

s = Serial('/dev/ttyUSB0', 115200, timeout=0)

#---------------------------------------------------------------------------------------
# color stuff
#---------------------------------------------------------------------------------------

import math
def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
    
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v
