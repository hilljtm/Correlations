# %%
import seaborn as sns
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
plt.style.use('seaborn')


quandl.ApiConfig.api_key = config.api_key

# quandl api get request, saving into csv file
gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')
gold.to_csv('gold.csv')

# reading csv file
gold = pd.read_csv("gold.csv", index_col='Date', parse_dates=['Date'])

btc = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])

df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc)


# setting matplotlib plot
fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.tight_layout()


plt.subplot(2, 1, 1)
plt.plot(gold.index, gold)


plt.xticks(gold.index[0::85], [])


plt.title('Gold vs BTC')
plt.ylabel('Gold')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

plt.xlabel('year')
plt.ylabel('BTC')
plt.savefig('gold_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
