import tweepy
import json
import re
import sys

consumer_key = 'kxJvgB8thUuotglZhDfvSYcTm'
consumer_skey = 'xlARFgVCmXxAObKcUj6etVlB6US32qx9WVF9hSK6rVChgr4QPG'
access_token = '198787753-Yycl6CCi2XXeb0qN4IHvhZw0VZ6xYOyqRcYxHTNw'
access_stoken = 'uMDKgkAqf0hvh6hlmeWqROGYEFCekD592GPbeCVg6lsaa'

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_skey)
    auth.set_access_token(access_token, access_stoken)
    return auth

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, *args, **kwargs):
        super(CustomStreamListener, self).__init__(*args, **kwargs)
        self.count = 0
        with open('restrict.word') as f:
            self.common = set(line.strip() for line in f)
        self.all_words = {}
        self.pattern = re.compile("[^\w]")
    
    def on_status(self, status):
        print('Got a Tweet')
        self.count += 1
        tweet = status.text
        tweet = self.pattern.sub(' ', tweet)
        words = tweet.split()
        for word in words:
            if len(word) > 2 and word != '' and word not in self.common:
                if word not in self.all_words:
                    self.all_words[word] = 1
                else:
                    self.all_words[word] += 1

if __name__ == '__main__':
    l = CustomStreamListener()
    try:
        auth = get_api()
        s = 'note7'
        twitterStreaming = tweepy.Stream(auth, l)
        twitterStreaming.filter(track=[s])
    except KeyboardInterrupt:
        print('-----total tweets-----')
        print(l.count)
        json_data =json.dumps(l.all_words, indent=4)
        with open('word_data.json', 'w') as f:
            print(json_data, file=f)
            print(s)
