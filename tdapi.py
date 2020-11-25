from tda import auth, client
import json
import pathlib
import config
from datetime import datetime
import requests


currentDir = pathlib.Path().absolute()

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path='{}\chromedriver'.format(currentDir)) as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

def getAccountInfo():
    account = c.get_account(config.account_id)
    return account

def getOpenPositions():
    account = c.get_account(config.account_id, fields=[
        c.Account.Fields.POSITIONS
    ])
    return account.json()['securitiesAccount']['positions']

def getOpenOrders():
    orders = c.get_orders_by_path(config.account_id)
    return orders

def getSymbolData(symbol, bars=None):
    def convertDate(candle):
        candle['datetime'] = datetime.fromtimestamp(
            int(candle['datetime']) / 1000.0
        )
        return candle

    period_type = c.PriceHistory.PeriodType.YEAR
    period = c.PriceHistory.Period.ONE_YEAR
    frequency_type = c.PriceHistory.FrequencyType.DAILY
    frequency = c.PriceHistory.Frequency.DAILY
    result = c.get_price_history(symbol.upper(),
        period_type=period_type,
        period=period,
        frequency_type=frequency_type,
        frequency=frequency
    ).json()['candles']
    converted_result = map(convertDate, result)
    return list(converted_result)

def getMoverList():
    result = []
    for symbol in ['$DJI', '$COMPX', '$SPX.X']:
        result.extend(
            c.get_movers(
            symbol,
            direction=c.Movers.Direction.UP,
            change=c.Movers.Change.PERCENT
            ).json()
        )
    return result

def getWatchlists():
    watchlists = c.get_watchlists_for_single_account(config.account_id)
    return [(x['name'], x['watchlistId']) for x in watchlists.json()]

def getScreenedList():
    r = requests.get('https://financialmodelingprep.com/api/v3/stock-screener?volumeMoreThan=1000000&apikey=e16bc46ed4ae615380404c8efe59b4ca')
    filtered = []
    quotelist = []
    for item in r.json():
        if item['price'] >= 1 and item['price'] <= 10:
            quotelist.append(item['symbol'])
    quotes = c.get_quotes(','.join(quotelist)).json()
    for key in quotes.keys():
        item = quotes[key]
        if item['lastPrice'] >= 1 and item['lastPrice'] <= 10:
            percentChange = item['netChange']/item['lastPrice']
            if percentChange >= 0.05:
                item['percentChange'] = percentChange
                filtered.append(item)
    return filtered

def display(x):
    try:
        print(json.dumps(x.json(), indent=4))
    except AttributeError:
        print(json.dumps(x, indent=4))

