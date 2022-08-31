import os
import time
import requests
import tweepy
from dotenv import load_dotenv

load_dotenv()



# TWITTER API CREDENTIALS 
consumerKey = os.environ.get("CONSUMER_KEY")
consumerSecret = os.environ.get("CONSUMER_SECRET")
accessToken = os.environ.get("ACCESS_TOKEN")
accessTokenSecret = os.environ.get("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuth1UserHandler(
    consumerKey,
    consumerSecret,
    accessToken,
    accessTokenSecret
)
client = tweepy.API(auth)

# The app and the corresponding credentials must have the Write permission
def tweet(tweet, medias = None):
    if medias == None:
        response = client.update_status(
            text = tweet
        )
        print(f"https://twitter.com/user/status/{response.data['id']}")
    else:
        
        # tweet_image(media[0].get_attribute('src'), tweet)
        tweet_image(medias, tweet)
        print('Done tweeting..........')

def tweet_image(medias, message):
    # [0].get_attribute('src')
    medias_id_string = []
    for i, media in enumerate(medias):
        file = f'temp{i}.jpg'
        request = requests.get(media.get_attribute('src'), stream=True)
        if request.status_code == 200:
            with open(file, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            media_file = client.media_upload(filename = file)
            medias_id_string.append(media_file.media_id_string)
            # response = client.update_status(status = message, media_ids = [media_file.media_id_string])
            # os.remove(file)
        else:
            print("Unable to download image")
    response = client.update_status(status = message, media_ids = medias_id_string)   
    time.sleep(2)

    for i in range(len(medias)):
        os.remove(f'temp{i}.jpg')
             

# def reply_tweet(i, tweet_id, img_url ):
#     file = 'tweetimg.jpg'
#     request = requests.get(img_url, stream=True)
#     if request.status_code == 200:
#         with open(file, 'wb') as image:
#             for chunk in request:
#                 image.write(chunk)

#         media_file = client.media_upload(filename = file)
#         client.update_status(status = f'Image {i}', in_reply_to_tweet_id = tweet_id, auto_populate_reply_metadata = True, media_ids = [media_file.media_id_string])
#         # response = client.update_status(status = f'Image {i}', media_ids = [media_file.media_id_string])
#         os.remove(file)
#     else:
#         print("Unable to download image")
    