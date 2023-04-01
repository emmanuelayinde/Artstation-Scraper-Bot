import os
import json, time
from parsel import Selector
from utils.formatter import format_description_text
from utils.users import get_usernames

file_path = os.getcwd() + '/tweeted_artworks.txt' 

key_word = 'hearthstone'
not_key_words = ['fanart', 'fan art', 'fan-art']



def supported(title, desc, a = None):
    if a != None:
        users = get_usernames()
        if a not in users:
            print(f"User {a} not in list")
            return False

    for k in not_key_words:
        if title.lower().find(k) >= 0:
            print(title.lower().find(k))
            return False
        elif desc.lower().find(k) >= 0:
            print(desc.lower().find(k))
            return False

    if title.lower().find(key_word) >= 0:
        print(title.lower().find(key_word))
        return True
    elif desc.lower().find(key_word) >= 0:
        print(desc.lower().find(key_word))
        return True 
    else:
        return False    


def format(artwork_author, artwork_title, artwork_desc, artwork_url):
    intro = '📢 New Official Artwork Spotted 📢'
    t_len = f"{intro}\n\n🎨 {artwork_author}\n 🏷️ {artwork_title}\n📜 \n\n🌐 {artwork_url}"
    formatted_artwork_text = format_description_text(artwork_desc, len(t_len))
    text = f"{intro}\n\n🎨 {artwork_author}\n 🏷️ {artwork_title}\n📜 {formatted_artwork_text}\n\n🌐 {artwork_url}"

    return text


def tweeted(card):
    with open(file_path) as f:
        if card in f.read():
            print( f'artwork with the id "{card}" already tweeted... ')
            return True
    return False


def write_url(artwork_url):
    with open(file_path, "a") as file:
        file.write(artwork_url + '\n')

    return print(f'artwork_url "{artwork_url}" successfully written...')        


def get_data(selector, url):
    a_l = selector.xpath("//div[@class='project-author'][1]/div/a[1]/@href").get()
    a_n = selector.xpath("//div[@class='project-author'][1]/div/a[1]/text()").get()
    t = selector.xpath("//h1/text()").get()
    d = selector.xpath("//read-more/div/p/text()").get()
    m = selector.xpath("//project-asset/div/div/picture/img/@src")

    # if 'https://www.artstation.com' in a_l:
    #     u = a_l.split('https://www.artstation.com/')[1]
    # else:
    #     u = a_l.split('/')[1]

    # if supported(t, d, u):
    #     return {"title": t, "description": d, "author" : a_n, "imgs": m, "url": url}
    # else:
    #     return None

    return {"title": t, "description": d, "author" : a_n, "imgs": m, "url": url}


def get_page_source(driver, url):

	driver.get(url)
	
	old_height = driver.execute_script("""
		function getHeight() {
			return document.querySelector('.wrapper').scrollHeight;
		}
		return getHeight();
	""")
	
	while True:
		driver.execute_script("window.scrollTo(0, document.querySelector('.wrapper').scrollHeight)")
	
		time.sleep(1.5)
	
		new_height = driver.execute_script("""
			function getHeight() {
				return document.querySelector('.wrapper').scrollHeight;
			}
			return getHeight();
		""")
	
		if new_height == old_height:
			break
	
		old_height = new_height
	
	selector = Selector(driver.page_source)
	# driver.quit()
	
	return selector


def scrape_artwork_data(selector, url):
    urls = selector.xpath("//projects-list-item/a/@href").getall()[:5]

    a = []

    for url in urls:
        if tweeted(url):
            print(f"Artwork with the link '{url}' aleady tweeted")
            continue
        else: 
            print(url)
            a.append(url)
            write_url(url)
    return a           

