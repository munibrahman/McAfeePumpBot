from binance.client import Client
import Settings
import json

api_key = Settings.BINANCE_API_KEY
api_secret = Settings.BINANCE_API_SECRET


client = Client(api_key, api_secret)

# I didn't know this endpoint existed, will use this endpoint next time.
# print(client.get_products())

# get all symbol prices
prices = client.get_all_tickers()

listBtc = []
# Filtering out results that don't contain BTC
for eachPrice in prices:
    if 'btc' in eachPrice['symbol'].lower():
        listBtc.append(eachPrice['symbol'])
        print(eachPrice['symbol'])

print(listBtc)

# This list will contain all the tickers without the tracker suffix of BTC
list_without_btc = []

for eachTicker in listBtc:
    eachNewTicker = eachTicker[:-3]
    list_without_btc.append(eachNewTicker)

print(list_without_btc)

# This file contains a list of almost all known currencies, pulled from github
allCurrencies = json.loads(open('cryptocurrencies.json').read())

# Data object will hold a key value pair of each tracker
# Key will be the shorthand ticker, value will hold the full name
# { BTC : 'Bitcoin'}
data = {}

for eachTicker in list_without_btc:
    for eachCurrency in allCurrencies:
        if eachCurrency == eachTicker:
            data[eachTicker] = allCurrencies[eachCurrency]
            continue


json_data = json.dumps(data)
print(json_data)

# Dump all this data into a file, so that it can be used by the twitter main.py script
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

