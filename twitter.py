from smsSender import txtself
from stock import extract_tickers


def get_tweets(twitter_v2, query, since_id=None):
    """Gets text content of 10 latest tweets that match the Twitter API V2 query passed in.

    Args:
        twitter_v2 (tweepy.Client): Authenticated Tweepy Client for Twitter API V2
        query (string): [A V2 Twitter Query](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query). E.g. `from:twitter_username`

    Returns:
        list(string): text content of tweets. Max length of 10. Sorted by most recent first
    """
    return twitter_v2.search_recent_tweets(query, since_id=since_id).data or []


def filter_stock_tweets(tweets):
    """Returns list of Tweet objects that have stock tickers

    Args:
        tweets (list(Tweet)): List of tweets to filter
    """
    tweet_has_tickers = lambda tweet: len(extract_tickers(tweet.text)) > 0
    return list(filter(tweet_has_tickers, tweets))


def notify_users(account_handle, tweet):
    """Notifies users of this program about this tweet of interest.

    Includes author of tweet and stock tickers mentioned in the tweet.

    Args:
        account_handle (string): twitter account handle of tweet author
        tweet (Tweet object): object with id(string) and text(string) properties
    """
    tickers = ", ".join(extract_tickers(tweet.text))
    link = f"https://twitter.com/elonmusk/status/{tweet.id}"
    message = f"New tweet about {tickers} from @{account_handle}! {link}"
    print(message)
    return txtself(message)
