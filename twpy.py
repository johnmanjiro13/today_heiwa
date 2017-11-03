import tweepy
import os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], s.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)