def get_tweets(twitter_v2, query):
    """Gets text content of 10 latest tweets that match the Twitter API V2 query passed in.

    Args:
        twitter_v2 (tweepy.Client): Authenticated Tweepy Client for Twitter API V2
        query (string): [A V2 Twitter Query](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query). E.g. `from:twitter_username`

    Returns:
        list(string): text content of tweets. Max length of 10.
    """
    get_text = lambda tweet: tweet.text
    tweets = twitter_v2.search_recent_tweets(query).data
    return list(map(get_text, tweets))
