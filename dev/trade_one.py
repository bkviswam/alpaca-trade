import alpaca_trade_api as tradeapi
import threading
from config.config import *

#API_KEY = config.API_KEY
#API_SECRET=config.API_SECRET

#instantiate REST API
api = tradeapi.REST(PAPI_KEY, PAPI_SECRET, PBASE_URL, api_version='v2')

#obtain account information
account = api.get_account()
#print(account)


#tsla = api.alpha_vantage.historic_quotes('TSLA', adjusted=True, output_format='json', cadence='weekly')
#print(tsla)

conn = tradeapi.stream2.StreamConn(PAPI_KEY, PAPI_SECRET, PBASE_URL)

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account):
    print('account',account)


@conn.on(r'^trade_updates$')
async def on_trade_updates(conn, channel, trade):
    print('trade', trade)

def ws_start():
	conn.run(['account_updates', 'trade_updates'])


#start WebSocket in a thread
ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()