# IMPORT NECCESSARY LIB
import os
import time

from tweet import tweet
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# PATH = "C:\Program Files (x86)\chromedriver.exe"    # Replace with your chromedriver path 
# driver = webdriver.Chrome(PATH)
path = os.getcwd()

def scrape_artstation_user(user_url, driver, WebDriverWait, By,EC):
    driver.get(f"https://www.artstation.com/{user_url}")
    gallery = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.gallery")))
    artworks = gallery.find_elements(By.CSS_SELECTOR, 'div.project > a.project-image')[:3]

    latest_artwork = None
    for artwork in artworks: 
        artwork.get_attribute('href')
        # print(video.text)
        tweeted = False
        if latest_artwork != None:
            break
        with open(path +"/tweeted_artworks.txt") as f:
            for line in f:
                if line.strip() == artwork.get_attribute('href'):
                    tweeted = True
                    break
                    
        if tweeted:
            continue
    
        with open(path +"/tweeted_artworks.txt", "a") as file:
            file.write(artwork.get_attribute('href') + '\n')
        latest_artwork = artwork.get_attribute('href')
        print(latest_artwork)
        break

    if latest_artwork == None:
        print('No Latest artwork......')
    else:
        driver.get(latest_artwork)
        time.sleep(5)
        artwork_author_name = driver.find_element(By.CSS_SELECTOR, "div.project-author > h3.project-author-name > a").text
        artwork_title = driver.find_element(By.CSS_SELECTOR, "div.project-sidebar-inner > h1.h3").text
        artwork_img = driver.find_element(By.CSS_SELECTOR, "div.asset-image > picture.d-block > img.img").get_attribute('src')
        artwork_url = driver.current_url

        # print(artwork_author_name)
        # print(artwork_title)
        # print(artwork_url)
        # print(artwork_img)
        tweet_title = '📢--- New Official Artwork Spotted ---📢'

        text = f"{tweet_title}\n\n🎨Artist: {artwork_author_name}\n\n📜 \"{artwork_title}\"\n\nSource: {artwork_url}"
        print(text)
        print('Tweeting in a moment.............')
        tweet(text, artwork_img)

        time.sleep(5)
        driver.quit()
    time.sleep(5)
    driver.quit()
        