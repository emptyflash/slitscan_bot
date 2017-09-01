import tweepy
from creds import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def upload_images(images):
    return [api.media_upload(i).media_id_string for i in images]

def tweet_images(image_ids):
    api.update_status(status="", media_ids=image_ids)
