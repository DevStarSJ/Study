# -*- coding: utf-8 -*-
import tweepy
from secret import *
from weather import Weather # 추가

class TwitterAPI:

    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    weather = Weather() # 추가
    twitter.tweet(weather.get_text()) # 수정
