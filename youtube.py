from apiclient.discovery import build
import random
from creds import YOUTUBE_API_KEY

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

service = build(API_SERVICE_NAME, API_VERSION, developerKey=YOUTUBE_API_KEY)

def random_word():
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    return random.choice(words)

def search_list(service, **kwargs):
    return service.search().list(**kwargs).execute()

def fuck_the_damn_pronunciations(item):
    title = item["snippet"]["title"].lower()
    return not ("pronouce" in title or 
                "pronunciation" in title or 
                "meaning" in title or 
                "definition" in title or
                "how to say" in title)

def get_random_youtube_id():
    word = random_word()
    result = search_list(service, 
                         part="snippet", 
                         maxResults=5, 
                         q=word,
                         type="video",
                         safeSearch="strict",
                         videoDefinition="high",
                         videoDuration="short",
                         videoDimension="2d")
    items = filter(fuck_the_damn_pronunciations, result["items"])
    try:
        return items[0]["id"]["videoId"]
    except IndexError:
        return get_random_youtube_id()
