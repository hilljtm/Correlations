# %%
import json
import requests
import datetime
import pandas as pd

#using cryptocompare API to get historical btc data
url = 'https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10'
r = requests.get(url)
data = r.json()

