import requests
from bs4 import BeautifulSoup

URL = 'https://www.aeon.info/news/'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

div:BeautifulSoup = soup.select_one('#wrap-container > main > div.news-list_container.section > div.news-list_cover.section')
a_list:BeautifulSoup = div.find_all('a')
span_list:BeautifulSoup = div.find_all('span')

for a, span in zip(a_list, span_list):
        print(a.get_text())
        print(span.get_text())