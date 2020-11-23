import tdapi
from stratbuilder import *

symbol = tdapi.getSymbolData('goog')
makeSymbol(symbol)

# GM data
avglow = average('low', 161) * 1.61843 * 1.61843
avghigh = average('high', 161) * 1.61843 * 1.61843
AVGX   = avglow - (avghigh - avglow)

hilinH = high() * 1.61843

avglowyest = average('low', 161, 1) * 1.61843 * 1.61843
avghighyest = average('high', 161, 1) * 1.61843 * 1.61843
hilinHyest = high(1) * 1.61843
AVGXyest   = avglowyest - (avghighyest - avglowyest)

def pastSignal():
    if hilinHyest < AVGXyest and hilinH >= AVGX:
        return True
    else:
        return False

print(pastSignal())