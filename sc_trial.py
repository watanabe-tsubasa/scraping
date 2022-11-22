import requests

URL = 'https://node-red-railway-production-4f90.up.railway.app/api/v1'

data = {"name": "watanabe",
        "age": 33,
        "message": "hello node red"}

res = requests.post(URL, data=data)
print(res.text)