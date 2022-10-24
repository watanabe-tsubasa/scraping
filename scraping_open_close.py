from bs4 import BeautifulSoup
import urllib.parse
import requests
import pandas as pd

df = pd.DataFrame(columns=['stores', 'days'])

store_name = input('店名')
parsed_name = urllib.parse.quote(store_name)
page = 0

while True:
    page += 1    
    
    res = requests.get(f'https://kaiten-heiten.com/page/{page}/?s={parsed_name}')

    soup = BeautifulSoup(res.text, 'html.parser')

    title_text = soup.find('title').get_text()
    print(title_text)

    if title_text == 'ページが見つかりませんでした – 開店閉店.com':
        break

    # main_tag = soup.select_one('#main')
    # print(main_tag)

    days = soup.find_all('span', {'class': 'post_time'})
    for i in range(len(days)):
        days[i] = days[i].get_text()
    # print(days)

    stores = soup.find_all('h3', {'class': 'list-title post_ttl'})
    for i in range(len(stores)):
        stores[i] = stores[i].get_text()
    # print(stores)

    # with open(f'data/{store_name}.csv', 'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([stores, days])

    df_tmp = pd.DataFrame({'stores': stores, 'days': days})
    df = pd.concat([df,df_tmp])

df = df.reset_index(drop=True)    
df.to_excel(f'data/{store_name}.xlsx')