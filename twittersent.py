import tweepy
from textblob import TextBlob

consumer_key = 'ucVkfDer70ELRO4cp15ur6V4X'
consumer_secret = 'd4QUIzpVcczKy6iusoxOlWLVXoRkMITK3J09YjxYItJpTpHwkv'

access_token = '1214363690-LNW6RmZVxpqCTnK0qAK2Wr64ZntFoUGhCJzF43w'
access_token_secret = '5U7NwxHvQq51gQ6vE8c3PaOnTQgRK3yg3mla2zbylAnFi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)