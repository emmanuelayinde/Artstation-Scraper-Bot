# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.scraper import scrape_artstation_user
from utils.users import get_all_users

# Replace with your chromedriver path
PATH = "C:\Program Files (x86)\chromedriver.exe"
# CONFIG FOR DEVELOPMENT ENV

users = get_all_users()

i = 0


while True:
    driver = webdriver.Chrome(PATH)
    
    user_url = users[i]
    print(user_url)
    print(len(users))


    print(f'Scraping {user_url} profile in progress...........................')
    scrape_artstation_user(user_url, driver, WebDriverWait, By, EC)
    print('Done Scraping.......................')

    i = i + 1
    if i >= len(users):
        i = 0

    # Sleep for a minute
    time.sleep(10)
