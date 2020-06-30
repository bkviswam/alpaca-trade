import requests
import json
import add_trailing_comma

STKWTS_URL = 'https://api.stocktwits.com/api/2/trending/symbols.json'

def get_trending_stocks():
    response = requests.get(STKWTS_URL)
    result = json.loads(response.content.decode('utf-8'))
    symbls = result['symbols']
    list = []
    for sym in symbls:
        list.append(sym['symbol'])
    return list

print(get_trending_stocks())