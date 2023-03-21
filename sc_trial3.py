import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://www.itoyokado.co.jp/store/result.html'

res_base = requests.get(URL)
soup_base = BeautifulSoup(res_base.content, 'html.parser')

url_names = soup_base.find_all('a', {"class": "-arrow"})

url_list = []
for url in url_names:
    # print(url)
    url_list.append(url["href"])
    
print(url_list)

res = requests.get(url_list[0])
# print(res.text)
soup = BeautifulSoup(res.content, 'html.parser')
div:BeautifulSoup = soup.select_one('#products > div')
division_names:BeautifulSoup = div.find_all('div', {"class": "Products-name"})

columns = []
for name in division_names:
    columns.append(name.get_text())

df_result = pd.DataFrame(columns=columns)

for i, url in enumerate(url_list):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # title = soup.title.string.split('|')[0]
    try:
        title = soup.find("h1").text
        # div:BeautifulSoup = soup.select_one('#products > div')
        div:BeautifulSoup = soup.select_one('#products > div')
        img_division:BeautifulSoup = div.find_all('img', {"class": "Products-productIcon"})

        list = []
        for img in img_division:
            list.append(img["alt"])
            
        df_result.loc[title] = list
        
        print(title)
        if i <= 4:
            print(df_result)
    except:
        continue

df_result.to_excel('./result.xlsx')