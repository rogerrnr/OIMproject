
from twitter import get_tweets
from config import bearer_token, consumer_key, consumer_secret
import tweepy

twitter = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret)

print(get_tweets(twitter, 'from:charliebilello'))