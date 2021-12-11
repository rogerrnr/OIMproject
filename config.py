from dotenv import load_dotenv
import os

load_dotenv()

# Twitter Secrets
consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
bearer_token = os.environ["TWITTER_BEARER"]

# Twilio Secrets
accountSID = os.environ["accountSID"]
authToken = os.environ["authToken"]
myTwilioNumber = os.environ["myTwilioNumber"]

# Program Config

# Twitter accounts to poll for stock tweets
twitter_accounts = ["charliebilello", "hmeisler", "kimblecharting", "the_chart_life"]

# How frequently the program should poll those accounts, in seconds
polling_interval_seconds = 5
