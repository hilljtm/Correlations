#%%
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


quandl.ApiConfig.api_key = 'W6U4YhAz2q7bigp7tQge'


gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05', end_date='2019-05-10')
btc = quandl.get("BITFINEX/BTCUSD", start_date='2016-01-05', end_date='2019-05-10')
df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc, columns=['High'])

