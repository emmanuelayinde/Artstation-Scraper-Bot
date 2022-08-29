# IMPORT NECCESSARY LIB
import os
import time
from setup import format_description_text
from tweet import tweet

path = os.getcwd()
key = 'hearthstone'

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

    if latest_artwork != None:
        driver.get(latest_artwork)
        time.sleep(5)
        artwork_title = driver.find_element(By.CSS_SELECTOR, "div.project-sidebar-inner > h1.h3").text
        artwork_description = driver.find_element(By.CSS_SELECTOR, "read-more.project-description > div > p").text
        time.sleep(5)

        # print(artwork_description.lower().find(key))
        # print(artwork_description.lower())
        # print(artwork_title.lower().find(key))
        # print(artwork_title.lower())

        if artwork_title.lower().find(key) != -1 or artwork_description.lower().find(key) != -1:
            artwork_author_name = driver.find_element(By.CSS_SELECTOR, "div.project-author > h3.project-author-name > a").text
            artwork_img = driver.find_element(By.CSS_SELECTOR, "div.asset-image > picture.d-block > img.img").get_attribute('src')
            artwork_url = driver.current_url

            tweet_title = '📢--- New Official Artwork Spotted ---📢'
            t = f"{tweet_title}\n\n🎨 {artwork_author_name}\n\n🏷️ {artwork_title}\n\nSource: {artwork_url}"

            desc = format_description_text(artwork_description, len(t))
            text = f"{tweet_title}\n\n🎨 {artwork_author_name}\n\n🏷️ {artwork_title} \n\n📜 {desc}\n\nSource: {artwork_url}"
            print(text)
            print('Tweeting in a moment.............')
            tweet(text, artwork_img)

        else:
            print('Post does not contain "Hearthstone"')    

        time.sleep(5)
        driver.quit()
    else:    
        print('No Latest artwork.....................')

    time.sleep(5)
    driver.quit()
        