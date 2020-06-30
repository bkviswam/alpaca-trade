import requests, json
from config.config import *

ACCOUNT_URL = "{}/v2/account".format(PBASE_URL)
ORDERS_URL = "{}/v2/orders".format(PBASE_URL)
HEADERS = {'APCA-API-KEY-ID': PAPI_KEY, 'APCA-API-SECRET-KEY': PAPI_SECRET}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


#response_account = get_account()
#print(response_account)

#buy
response_create_order_buy = create_order('MRNA',500, 'buy', 'market', 'day')
print(response_create_order_buy)

#sell
#response_create_order_sell = create_order('AXP', 50, 'sell', 'market', 'day')
#print(response_create_order_sell)