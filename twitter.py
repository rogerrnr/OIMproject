def get_tweets(twitter_v2, query):
  get_text = lambda tweet: tweet.text
  tweets = twitter_v2.search_recent_tweets(query).data
  return list(map(get_text, tweets))