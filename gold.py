#%%
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


quandl.ApiConfig.api_key = config.api_key

gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')
btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date='2016-01-05')
df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc)

horizontal_stack = pd.concat([df1, df], axis=1)
print(horizontal_stack) 
