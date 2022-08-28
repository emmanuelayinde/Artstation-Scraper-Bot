# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper import scrape_artstation_user

# Replace with your chromedriver path
PATH = "C:\Program Files (x86)\chromedriver.exe"
# CONFIG FOR DEVELOPMENT ENV

users = ['angelobortolini', 'izzyh', 'kamuihax', 'carolinegariba', 'ramzykamen', 'onikaizer', 'tiffachiu', 'juyoungoh', 'sulamoon', 'resolvent',
         'nicolasaviori', 'patriartis', 'cortesdev', 'cryofowl', 'willmurai', 'jayaxer', 'angelicaalieva', 'greentaldarin', 'jasonkang', 'leossart', 'grafit']
i = 0


while True:
    driver = webdriver.Chrome(PATH)
    
    user_url = users[i]
    print(f'Scraping {user_url} profile in progress...........................')
    scrape_artstation_user(user_url, driver, WebDriverWait, By, EC)
    print('Done Scraping.......................')

    i = i + 1
    if i >= len(users):
        i = 0

    # Sleep for a minute
    time.sleep(60)
