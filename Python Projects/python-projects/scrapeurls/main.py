import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 
import pprint

def urls_scraper():
    baseurl = input("Enter a url: ")
    page = requests.get(baseurl)
    soup = BeautifulSoup(page.text, 'html.parser')

    urls_list = []
    urls_name = []

    for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
        # pprint.pprint(f"{link.string} --- {link.get(('href'))}")
        print('processing..')
        urls_name.append(link.string)
        urls_list.append(link.get('href'))
    df = pd.DataFrame(list(zip(urls_name, urls_list)), columns= ['Name','Link'])
    df.to_csv("urls_file.csv")
    print('done!')
urls_scraper()