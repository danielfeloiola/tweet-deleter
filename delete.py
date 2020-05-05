##############################################################
# Deletando velharias do Twitter
# Deleting old junk from twitter
#
# Deleta tweets com base no arquivo tweets.js
# Delete tweets using the tweets.js file
# https://twitter.com/settings/your_twitter_data
##############################################################

#importanto as bibliotecas
import tweepy
import os
import json

# pegas as chaves
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []

# retira dos dados do arquivo tweets.js
with open('tweet.js', 'r', encoding='UTF-8') as fp:
    js_file = fp.read()
    contents = json.loads(js_file)
    tweets.extend(contents)

# itera pelos tweets e apaga todos
for tweet in tweets:
    try:
        api.destroy_status(tweet['tweet']['id_str'])
        print("SUCCESS: " + tweet['tweet']['id_str'])
    except:
        print("failed to delete " + tweet['tweet']['id_str'])
        pass
