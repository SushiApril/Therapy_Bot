import tweepy
import time
from keys import bearer_token
from keys import api_key
from keys import api_secret
from keys import access_token
from keys import access_token_secret
from chat import gen

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret )

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#client.create_tweet(text = "sleep in a well lit room")

#replies with this message
message = "Im here"
#bots id
client_id = client.get_me().data.id
#print("client id is", client_id)

start_id = 1

while True:
     response = client.get_users_mentions(client_id)
     #This is the content of the latest mention
     latest_tweet = response.data[0]  # Assuming the latest tweet is at index 0
     print(latest_tweet)
     tweet_id = response.meta['newest_id']
     if tweet_id != start_id:
          #Generate response for the tweet
          retweet_material = gen(str(latest_tweet))
          client.create_tweet(in_reply_to_tweet_id = tweet_id, text = retweet_material)
          start_id = tweet_id
     time.sleep(10)