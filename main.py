# IMPORT NECCESSARY LIB
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.users import get_all_users
import chromedriver_autoinstaller
from utils.utils import get_page_source, scrape_artwork_data, get_data, supported, format


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

users = get_all_users()

driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)         

def main():
    print('Scraping.......................')
    url = 'https://www.artstation.com/?sort_by=latest&dimension=2d'
    r = get_page_source(driver, url)
    print("r:  ", r)
    artworks = scrape_artwork_data(r, url)
    data = []
    for artwork in artworks:
        sc = get_page_source(driver, artwork)
        d = get_data(sc, artwork)
        if d != None:
            data.append(d)
    print(data)
    print('Done Scraping.......................')
    
    for d in data:
        f = format(d['author'], d['title'], d['descriptdon'], d['url'])
        print(f)



if __name__ == "__main__":
    main()