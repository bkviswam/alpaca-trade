import requests
import json
from config.config import STKWTS_URL

#parse the json and return the list of symbols
def get_trending_stocks():
    response = requests.get(STKWTS_URL)
    result = json.loads(response.content.decode('utf-8'))
    symbls = result['symbols']
    list = []
    for sym in symbls:
        list.append(sym['symbol'])
    return list

#print(get_trending_stocks())