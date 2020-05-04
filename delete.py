##############################
# Acessando a API do Twitter
# E deletando velharias
##############################

#importanto as bibliotecas
import tweepy
import os

# pegas as chaves
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# pega o usuario do env
user = os.getenv('USER')

# authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# cria um usuario
me = api.get_user(user)._json

# pega a timeline do usuário
timeline = api.user_timeline(me, count=20)

# passa pelos tweets e deleta todos
for tweet in timeline:
    print("deletando: " + tweet.text)
    api.destroy_status(tweet.id)
