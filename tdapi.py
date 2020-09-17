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

r = c.get_quote('MSFT')
print(json.dumps(r.json(), indent=4))