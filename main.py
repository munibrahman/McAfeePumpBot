from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Settings

import json

settings = Settings

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    # TODO: Right now ALL tweets mentioning mcafee are being broadcasted, make sure you only pass new tweets from
    # mcafee himself
    def on_data(self, data):
        j = json.loads(data)
        print(j["text"])
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(follow=[settings.MCAFEE_TWITTER_ID])

# TODO: Take the input tweet and split it into a list of strings.
# Compare those strings against the database and buy the coins needed.
# def decipher(tweet):
#     print(tweet)
