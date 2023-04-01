# IMPORT NECCESSARY LIB
import os
import time
from utils.date import now
from utils.tweet import tweet
from utils.utils import get_page_source, scrape_artwork_data, get_data

path = os.getcwd()
key = 'hearthstone'
not_keys = ['fanart', 'fan art', 'fan-art']


def scrape_artstation_user(driver):
    url = 'https://www.artstation.com/?sort_by=latest&dimension=2d'
   
    r = get_page_source(driver, url)
    print("r:  ", r)
    artworks = scrape_artwork_data(r, url)

    data = []

    for artwork in artworks:
        sc = get_page_source(driver, artwork)
        d = get_data(sc, artwork)
        data.append(d)

    print("data:    ", data)

   