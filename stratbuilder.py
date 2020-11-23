symbol = []

def makeSymbol(sym):
    global symbol
    symbol = sym

def average(ohlc, bars, offset=0):
    if len(symbol) < bars + offset:
        return 'not enough datapoints'
    if offset > 0:
        snippet = [x[ohlc] for x in symbol[-(bars+offset):-offset]]
    else:
        snippet = [x[ohlc] for x in symbol[-bars:]]
    return sum(snippet) / len(snippet)


def high(bars=1):
    return symbol[-bars]['high']

def low(bars=1):
    return symbol[-bars]['low']

def open(bars=1):
    return symbol[-bars]['open']

def close(bars=1):
    return symbol[-bars]['close']

def volume(bars=1):
    return symbol[-bars]['volume']

