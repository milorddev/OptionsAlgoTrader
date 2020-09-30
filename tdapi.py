from tda import auth, client
import json
import pathlib
import config

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

def getWatchlists():
    watchlists = c.get_watchlists_for_single_account(config.account_id)
    return [(x['name'], x['watchlistId']) for x in watchlists.json()]

def display(x):
    try:
        print(json.dumps(x.json(), indent=4))
    except AttributeError:
        print(json.dumps(x, indent=4))

display(getWatchlists())
# display(c.get_watchlist(config.account_id, 583743568))


