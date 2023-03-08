import requests
import urllib.parse as parse

appId = "7f8ed9a7690e7c61f9618612e6fb419f126a6e0c"
statsDataID = "0003348238"

api_Url = f'http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId={appId}&statsDataId={statsDataID}'

print(api_Url)
res = requests.get(api_Url)

print(res.text)