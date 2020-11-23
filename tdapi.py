from tda import auth, client
import json
import pathlib
import config
from datetime import datetime


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

def display(x):
    try:
        print(json.dumps(x.json(), indent=4))
    except AttributeError:
        print(json.dumps(x, indent=4))


