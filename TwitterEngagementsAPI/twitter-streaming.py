#Import the necessary methods from tweepy library
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re

# Enter Twitter API Keys
access_token = "1267279674608148480-Zy6973pqyUFmnAd9CeG4FfmJLOrrHb"
access_token_secret = "kKiX0YnqDFpSi94a4CfPzIX7cykZRuoXyN7WcnGICAojG"
consumer_key = "wgqGwGufa7uIDZ7o8u2uGyUnr"
consumer_secret = "mlx8l8Q8BIajdZtNOp9usBojK7kaW4vBFBn4bl5GjbzrpGcRCD"

# Create tracklist with the words that will be searched for
tracklist = ['#menervasoftware']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            jdata = json.loads(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=tracklist)
