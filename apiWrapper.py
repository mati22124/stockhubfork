#  Polygon APi: v0vxDEvhtQxoknyARHwpKwebnq1q3pJ4
#  Realtime Stock Market Data Api: HOCIIJZHZ3J9TL7M

# RapidAPI key: 8b597321fdmsh82efd0634f640b2p18f629jsn450b4a8c3609

import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AMD,IBM,AAPL"}

headers = {
	"x-rapidapi-key": "8b597321fdmsh82efd0634f640b2p18f629jsn450b4a8c3609",
	"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

x = response.json()

for i in x["quoteResponse"]["result"]:
    print(i["symbol"])
    print(i["regularMarketPrice"])
