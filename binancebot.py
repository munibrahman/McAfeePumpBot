from binance.client import Client
import Settings

api_key = Settings.BINANCE_API_KEY
api_secret = Settings.BINANCE_API_SECRET


client = Client(api_key, api_secret)

# get all symbol prices
prices = client.get_all_tickers()

listBtc = []
# TODO: Get all the symbols from Binance, if all holdings in BTC then you only want to trade with BTC, otherwise filter
# eth values or bnb values
for eachPrice in prices:
    if 'btc' in eachPrice['symbol'].lower():
        listBtc.append(eachPrice)
        print(eachPrice['symbol'])
