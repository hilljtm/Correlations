# %%
import seaborn as sns
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


quandl.ApiConfig.api_key = config.api_key

gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')
btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date='2016-01-05')
df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc)


joinedgbtc = pd.concat([df1, df], axis=1)
joinedgbtc.to_csv('joinedgbtc.csv')


def btcgcor():
    df2 = pd.read_csv('joinedgbtc.csv')
    df2['btc'].plot()
    #df2_corr = df2.corr()

# joinedgbtc()
