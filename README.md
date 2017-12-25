# McAfee Twitter Crypto Pump and Dump bot

This script monitors John McAfee's tweets and then purchases coins listed on binance based on the mentioned coins in his tweets.

## A word of caution

This bot is simply for fun, don't expect it to make any money whatsoever. I haven't made any money either. It is simply for educational purposes, if you lose any money while using this bot, I will NOT be resposible.



## Getting Started

Download the project.

Open ```settings.py``` and input your API keys for twitter and binance.
Open ```main.py and``` enter the amount of bitcoin that you want to gamble with by changing the `BTC_to_gamble` var.

### Prerequisites


You must have python3 installed.


## Running the script

After everything is completed, run it by typing `$ python3 main.py`

If everything succeeds you should see no errors and only see a json object of numerous coin trackers on available on the exchange.

## Built With

* [python-binance](https://github.com/sammchardy/python-binance) - API for binance
* [tweepy](https://github.com/tweepy/tweepy) - Twitter for python!
* [Cryptocurrencies](https://github.com/crypti/cryptocurrencies) -  Get a list of all the cryptocurrency symbols and names.



## License

This project is licensed under the MIT License.

