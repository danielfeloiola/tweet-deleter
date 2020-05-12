##############################################################
# Deletando tweets semanalmente
# Deleting tweets weekly
#
# Requer uma chave da API / Needs an API key
##############################################################


#importanto as bibliotecas
import schedule
import time
import tweepy
import os

def delete():
    print("STARTING DELETION")
    print(time.now)

    # pegas as chaves
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # pega o usuario do env
    user = os.getenv('USER')

    # auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # pega a timeline do usuário
    timeline = api.user_timeline(user, count=300)

    # passa pelos tweets e deleta todos
    for tweet in timeline:
        print("deletando: " + tweet.text)
        api.destroy_status(tweet.id)

# repete a tarefa diariamente as 14:15
schedule.every().day.at("14:20").do(delete)

# roda permanentemente
while True:
    schedule.run_pending()
    time.sleep(60)
