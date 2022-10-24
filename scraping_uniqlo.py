from bs4 import BeautifulSoup
# import urllib.parse
import requests
import pandas as pd
import time

list_year = [2018, 2019, 2020, 2021, 2022]
df = pd.DataFrame(columns=['date', 'title', 'text'])

for year in list_year:
    res = requests.get(f'https://www.uniqlo.com/jp/ja/contents/corp/press-release/{year}/')
    print('sleep')
    time.sleep(2)

    # print(res.text)

    soup = BeautifulSoup(res.content, 'html.parser')

    title_text = soup.find('title').get_text()
    print(title_text)

    table = soup.select_one('#boxCompanyList')
    # print(table)
    # 日付リストの取得
    release_date = table.find_all('dt')
    date_list = []
    for dt in release_date:
        date_list.append(dt.get_text())
    # print(date_list)

    # タイトルリストの取得
    release_title = table.find_all('dd')
    title_list = []
    for dd in release_title:
        title_list.append(dd.get_text())
    # print(title_list)

    # リリースURLの取得
    release_url = table.find_all('a')
    url_list = []
    for a in release_url:
        end_url = a.get('href')
        url = f'https://www.uniqlo.com{end_url}'
        url_list.append(url)
    # print(url_list)

    # 取得したURLをそれぞれスクレイピングし、本文のリストを生成
    text_list = []
    for each_url in url_list:
        res_tmp = requests.get(each_url)
        print('sleep')
        time.sleep(2)

        soup_tmp = BeautifulSoup(res_tmp.content, 'html.parser')
        content = soup_tmp.select_one('#boxCompanyEntry')
        each_text = content.find_all('p')
        separated_text = []
        for p in each_text:
            separated_text.append(p.get_text())
        text = "".join(separated_text)
        text_list.append(text)
    # print(text_list)

    df_tmp = pd.DataFrame({'date': date_list, 'title': title_list, 'text': text_list})
    df = pd.concat([df, df_tmp])

df.to_excel('out/uniqlo_sc.xlsx')