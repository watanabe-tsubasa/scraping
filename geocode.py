from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import requests
import time

df = pd.read_excel('data/イオン.xlsx')
df['lat'] = 0
df['lng'] = 0
address_list = df['住所'].tolist()

# print(df)

address = address_list[0]
parsed_address = urllib.parse.quote(address)

try_count = 0

for i, address in enumerate(address_list):
    try:
        parsed_address = urllib.parse.quote(address)
    except:
        continue

    while try_count < 3:
        res = requests.get(f'https://www.geocoding.jp/api/?q={parsed_address}')
        # print(res.content)
        time.sleep(5)
        try:
            soup = BeautifulSoup(res.content, 'lxml-xml')

            lat = soup.find('lat').get_text()
            lng = soup.find('lng').get_text()

            print(f'{i}: lat:{lat}, lng:{lng} ')

            df.at[i,'lat'] = lat
            df.at[i,'lng'] = lng
            break
        except:
            try_count += 1
            print(f'{i}:{try_count}')
    
    try_count = 0
    time.sleep(5)

df.to_excel('data/イオン_addCoodinate.xlsx')