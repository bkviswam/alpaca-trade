from yahoo_fin import stock_info as si


def get_live_price(ticker):
    return si.get_live_price(ticker)


# get most active stocks on the day
# https://finance.yahoo.com/most-active
def get_day_most_active():
    return si.get_day_most_active()


# get biggest gainers
# https://finance.yahoo.com/gainers
def get_day_gainers():
    return si.get_day_gainers()


# get worst performers
# https://finance.yahoo.com/losers

def get_day_losers():
    return si.get_day_losers()


#tests
#print('AAPL', round(get_live_price('AAPL'), 2))
#print('AMZN', round(get_live_price('AMZN'), 2))
#print('BBY', round(get_live_price('BBY'), 2))
# print(si.get_top_crypto())


#print(si.get_day_most_active())
#print(si.get_day_gainers())
print(si.get_day_losers())

#print(si.get_data())