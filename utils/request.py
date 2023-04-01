import requests
from parsel import Selector


def source_code():
    url = 'https://www.artstation.com/?sort_by=latest&dimension=2d'
    text = requests.get(url).text
    selector = Selector(text=text)
    print("Selector", selector)


