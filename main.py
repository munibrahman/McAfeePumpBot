from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Settings

import json
import tweepy
import re

from binance.client import Client

import binancebot

api_key = Settings.BINANCE_API_KEY
api_secret = Settings.BINANCE_API_SECRET


client = Client(api_key, api_secret)


settings = Settings

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

currencies = json.loads(open('data.json').read())

binancebot

BTC_to_gamble = 0.5


def buy_currency(currency):
    ticker = currency + 'BTC'
    quantity = int(BTC_to_gamble / float(client.get_orderbook_ticker(symbol=ticker)['askPrice']))
    order = client.create_order(
        symbol=ticker,
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=quantity)

    print(order)


# Take the input tweet and split it into a list of strings.
# Compare those strings against the database and buy the coins needed.
def decipher(json_tweet):
    print(json_tweet)
    if "created_at" in json_tweet:
        # This ensures that the tweet is ONLY by McAfee and not someone else tweeting at him
        if json_tweet["user"]["id"] == int(Settings.MCAFEE_TWITTER_ID):
            # We also want to make sure that he isn't favouring/retweeting someone else's tweet
            if not "retweeted_status" in json_tweet:
                # Get the full, extended tweet with all of the words.
                extended_tweet = api.get_status(json_tweet["id"], tweet_mode='extended')._json['full_text']
                print(extended_tweet)
                # Removes any sort of symbols using regex
                removed_punctuation = re.sub(r'[^\w]', ' ', extended_tweet)
                # Splits all of the words into a list of strings
                listOfWords = removed_punctuation.split()
                print(listOfWords)

                #  Compare each word in the tweet against the listed currencies on binance, if we find anything, BUY
                for eachWord in listOfWords:
                    for eachCurrency in currencies:
                        if eachWord.lower() == eachCurrency.lower() or eachWord.lower() == currencies[eachCurrency].lower():
                            print(eachCurrency)
                            print('BUY')
                            buy_currency(eachCurrency)
                            continue


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    # TODO: Right now ALL tweets mentioning mcafee are being broadcasted, make sure you only pass new tweets from
    # mcafee himself
    def on_data(self, data):
        print('\n' + data + '\n')
        json_tweet = json.loads(data)
        decipher(json_tweet)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(follow=[settings.MCAFEE_TWITTER_ID])




