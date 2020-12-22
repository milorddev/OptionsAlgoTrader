from stratbuilder import *

def GM_Vol():
    voldiff = volume() / average('volume', 261)
    return True if voldiff > 1.32 else False

def QBKO1():
    avglow = average('low', 161) * 1.618 * 1.618
    avghigh = average('high', 161) * 1.618 * 1.618
    AVGX   = avglow - (avghigh - avglow)
    return True if close() >= AVGX else False

def BRK1():
    hilinH = high() * 1.61843
    hilinL = low() * 1.61843
    avglow  = average('low', 161) * 1.618 * 1.618
    avghigh = average('high', 161) * 1.618 * 1.618
    AVGX   = avglow - (avghigh - avglow)
