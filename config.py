from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
bearer_token = os.environ["TWITTER_BEARER"]

twitter_accounts = ["charliebilello"]
polling_interval_seconds = 5
