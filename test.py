import requests
import re

res = requests.get('https://qiita.com/watanabe-tsubasa/private/a275452b1c88993d5690.md')
encoded_content = res.content.decode(res.encoding)

# regex = r'tags:\s*([\w\s-]+)\n'
regex = r'tags:\s*([\w\s#-]+)\n'


m = re.search(regex, encoded_content)

if m:
    tag_list:list = m.group(1).strip().split(' ')
else:
    print('not match')

def validate_tag_info(tag:str):

    if '#' in tag:
        print('Qiitaではタグ名に # は不要なので修正してください')
    else:
        try:
            tag_follower_count = requests.get(f'https://qiita.com/api/v2/tags/{tag}').json()['followers_count']
        except:
            tag_follower_count = 0
        if tag_follower_count < 200:
            print(f'{tag}はフォロワー数が200を下回るタグですが利用しますか')
        
for tag in tag_list:
    print(tag)
    validate_tag_info(tag=tag)
    
print(f'記事のタグ数は{len(tag_list)}です。')
if len(tag_list) < 5:
    print('タグはできる限り5つつけましょう')

    
# syntax_list = re.findall(r'```(\w*)\n', encoded_content)

pattern = r"```(?P<lang>\w+)?\n(?P<code>.*?)\n```"
matches = re.findall(pattern, encoded_content, re.DOTALL)
for i, match in enumerate(matches):
    lang = match[0]
    if lang == '':
        print(f'{i + 1}番目のコードブロックには言語が指定されていません。\nシンタックスハイライトが有効になるよう、適切なコードを指定しましょう。')
    else:
        print(f'{i + 1}番目のコードブロックに指定されているシンタックスハイライトは{lang}です。')
        if lang != 'javascript' and 'js':
            print('正しいかを確認しましょう。')
        if lang == 'java':
            print('特にJavaとJavaScriptは、ハムとハムスター位違いますよ。注意しましょう。')   