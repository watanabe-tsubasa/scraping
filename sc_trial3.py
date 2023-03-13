import requests
from bs4 import BeautifulSoup

URL = 'https://stores.itoyokado.co.jp/070'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

div:BeautifulSoup = soup.select_one('#products > div')
division_names:BeautifulSoup = div.find_all('div', {"class": "Products-name"})
img_division:BeautifulSoup = div.find_all('img', {"class": "Products-productIcon"})

for name, img in zip(division_names, img_division):
        print(f'{name.get_text()}: {img["alt"]}')