# imports

import tweepy
import secrets

# variables

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token_key, secrets.access_token_secret)

api = tweepy.API(auth)

# Hand-made function library

def getFirstsTweets(username):
    if not userExists(username):
        return []
    tweets = api.user_timeline(screen_name = username, count = 3)
    L = []
    for t in tweets:
        L.append(t.text)
    return L

def getFollowers(username):
    L = []
    i = 0
    for f in tweepy.Cursor(api.followers, screen_name = username, count = 50).items():
        L.append(f.screen_name)
        i+=1
        if i > 49:
            return L
    return L

def getFollowings(username):
    L = []
    i = 0
    for f in tweepy.Cursor(api.friends, screen_name = username, count = 50).items():
        L.append(f.screen_name)
        i+=1
        if i > 49:
            return L
    return L

def userExists(username):
    try:
        user = api.get_user(username)
        return not user.protected
    except Exception:
        return False
