# Importing Tweepy, as well as the keys and secrets from the other file.
import tweepy, time, sys
import keys_secrets.py

argFile = str(sys.argv[1])

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = api.tweepy.API(auth)

#Finds user with handle @hotinternetbabe
#Loops through tweets and likes them all
#Continuely checks for new tweets / likes them
