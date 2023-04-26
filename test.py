import requests
import re

res = requests.get('https://qiita.com/watanabe-tsubasa/items/8342595d641143b780f7.md')
encoded_content = res.content.decode(res.encoding)

regex = r'tags:\s*([\w\s-]+)'

m = re.search(regex, encoded_content)

if m:
    tag_list:list = m.group(1).strip().split(' ')
else:
    print('not match')

def detect_tag_followers(tag:str):
    tag_res_json = requests.get(f'https://qiita.com/api/v2/tags/{tag}').json()
    if tag_res_json['followers_count'] < 200:
        print(f'{tag}はフォロワー数が200を下回るタグですが利用しますか')
    
        
for tag in tag_list:
    detect_tag_followers(tag=tag)
    
print(f'記事のタグ数は{len(tag_list)}です。')