import tdapi
from stratbuilder import *

def setSymbol(sym):
    symbol = tdapi.getSymbolData(sym)
    makeSymbol(symbol)

# GM data
def strategy():
    avglow = average('low', 161) * 1.61843 * 1.61843
    avghigh = average('high', 161) * 1.61843 * 1.61843
    AVGX   = avglow - (avghigh - avglow)

    hilinH = high() * 1.61843

    avglowyest = average('low', 161, 1) * 1.61843 * 1.61843
    avghighyest = average('high', 161, 1) * 1.61843 * 1.61843
    hilinHyest = high(1) * 1.61843
    AVGXyest   = avglowyest - (avghighyest - avglowyest)

    if hilinHyest <= AVGXyest and hilinH >= AVGX:
        return {
            'condition': True,
            'limit': hilinH,
            'stop' : low() - (low() * 0.33)
        }
    else:
        return {
            'condition': False,
            'limit': hilinH,
            'stop' : low() - (low() * 0.33)
        }

def run(sym):
    setSymbol(sym)
    return strategy()