#!/usr/local/bin/python

import random
import twitter

from PIL import Image
from youtube import get_random_youtube_id
from slitscan import get_slit_scans

video_id = get_random_youtube_id()
images = get_slit_scans(video_id)
random.shuffle(images)

def save_image(i, image):
    image_name = "temp" + str(i) + ".png"
    Image.fromarray(image).save(image_name)
    return image_name

image_names = [save_image(i, image) for i, image in enumerate(images[:4])]
image_ids = twitter.upload_images(image_names)
twitter.tweet_images(image_ids)
