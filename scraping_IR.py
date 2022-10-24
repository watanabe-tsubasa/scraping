from bs4 import BeautifulSoup
# import urllib.parse
import requests
# import pandas as pd

# df = pd.DataFrame(columns=['stores', 'days'])

# html_num = input('html number:')
# access_URL = f'http://www.7andi.com/ir/disclose/release/{html_num}.html'

# res = requests.get(f'http://www.7andi.com/ir/disclose/release/{html_num}.html')
res = requests.get('http://www.7andi.com/ir/disclose/release/35737.html')

print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text()
print(title_text)

div = soup.find_all('div')
# table = soup.find('table', {'style': 'height: 1425px;'})
print(div)
#pbBlock1036654 > div > div > table > thead > tr > th:nth-child(2)

temp = soup.select_one('#pbBlock1036654 > div > div > table > thead > tr > th:nth-child(2)')
print(temp)
# main_tag = soup.select_one('#main')
# print(main_tag)

# days = soup.find_all('span', {'class': 'post_time'})
# for i in range(len(days)):
#     days[i] = days[i].get_text()
# # print(days)

# stores = soup.find_all('h3', {'class': 'list-title post_ttl'})
# for i in range(len(stores)):
#     stores[i] = stores[i].get_text()
# # print(stores)




# df_tmp = pd.DataFrame({'stores': stores, 'days': days})
# df = pd.concat([df,df_tmp])

# df = df.reset_index(drop=True)    
# df.to_excel(f'data/{store_name}.xlsx')