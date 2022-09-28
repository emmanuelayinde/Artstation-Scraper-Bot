# IMPORT NECCESSARY LIB
import os
import time
from utils.date import now
from utils.tweet import tweet
from utils.utils import check_if_supported, check_if_tweeted, format_artwork, write_artwork_url

path = os.getcwd()
key = 'hearthstone'
not_keys = ['fanart', 'fan art', 'fan-art']


def scrape_artstation_user(user_url, driver, WebDriverWait, By,EC):
    driver.get(f"https://www.artstation.com/{user_url}")
    time.sleep(15)
    gallery = driver.find_element(By.CSS_SELECTOR, 'div.gallery')
    artworks = gallery.find_elements(By.CSS_SELECTOR, 'div.project > a.project-image')[:2]

    latest_artwork = None
    for artwork in artworks: 
        artwork.get_attribute('href')
        # print(video.text)
        tweeted = False
        if latest_artwork != None:
            break

        tweeted = check_if_tweeted(artwork.get_attribute('href'))
                    
        if tweeted:
            continue
    
        write_artwork_url(artwork.get_attribute('href'))

        latest_artwork = artwork.get_attribute('href')
        print(latest_artwork, now())
        break

    if latest_artwork != None:
        driver.get(latest_artwork)
        time.sleep(20)
        artwork_title = driver.find_element(By.CSS_SELECTOR, "div.project-sidebar-inner > h1.h3").text
        # artwork_title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.project-sidebar-inner > h1.h3"))).text
        artwork_description = driver.find_element(By.CSS_SELECTOR, "read-more.project-description > div > p").text
        # artwork_description = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "read-more.project-description > div > p"  ))).text
        time.sleep(10)

       
        print(artwork_title , '...............................'  , artwork_description, now())
        supportted = check_if_supported(artwork_title, artwork_description)
        print(supportted)

        time.sleep(2)

        if supportted:
            artwork_author_name = driver.find_element(By.CSS_SELECTOR, "div.project-author > h3.project-author-name > a").text
            artwork_url = driver.current_url
            
            try:
                artwork_imgs = driver.find_elements(By.CSS_SELECTOR, "project-asset.asset > div.asset-container > div.asset-image > picture.d-block > img.img")
                for i in artwork_imgs:
                    print(i.get_attribute('src'), now())
                image_present = True
            except:
                image_present = False
                print('No image for the post', now())    


            text = format_artwork(artwork_author_name, artwork_title, artwork_description, artwork_url)
            print(text)
            print('Tweeting in a moment.............', now())
            if image_present:
                tweet(text, artwork_imgs)
            else:
                tweet(text, None)     

        else:
            print('Post does not contain "Hearthstone"', now())    

        time.sleep(5)
        driver.quit()
    else:    
        print('No Latest artwork.....................', now())

    time.sleep(5)
    driver.quit()
        