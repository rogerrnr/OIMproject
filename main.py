from twitter import get_tweets, filter_stock_tweets, notify_users
from config import (
    bearer_token,
    consumer_key,
    consumer_secret,
    twitter_accounts,
    polling_interval_seconds,
)
import time
import tweepy
from smsSender import txtself

twitter = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)

"""Cache for latest tweet id's per account handle. handle(string) -> id(string)"""
latest_tweets = {}


def poll_handle(handle):
    """Polls twitter handle for new tweets about stocks. Notifies users if such tweets are found.

    Args:
        handle (string): twitter account handle
    """
    tweets = get_tweets(
        twitter_v2=twitter,
        query=f"from:{handle}",
        since_id=latest_tweets.get(handle, None),
    )

    if len(tweets) <= 0:
        return

    # Updates most recent tweet for user. Necessary to avoid repeat notifications for same tweet
    latest_tweets[handle] = tweets[0].id
    for tweet in filter_stock_tweets(tweets):
        notify_users(account_handle=handle, tweet=tweet)


def main():
    """Main Program Loop"""

    for handle in twitter_accounts:
        poll_handle(handle)


while True:
    main()
    time.sleep(polling_interval_seconds)
