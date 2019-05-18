#%%
import config
import quandl 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import seaborn as sns

quandl.ApiConfig.api_key = config.api_key


btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date='2016-01-05')
df1 = pd.DataFrame(btc)
data = pd.read_csv("sp500.csv", index_col=0)
sp = pd.DataFrame(data)

#Not sure I even need to concat these
#newspindex = pd.merge(df1, sp, left_index=True, right_index=True, how='left')
#newspindex.index.names = ['Date']

fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.tight_layout()

plt.subplot(2, 1, 1)
plt.plot(sp.index, sp)
plt.xticks(sp.index[0::80], [])


plt.title('S&P500 vs BTC')
plt.ylabel('% S&P500')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

plt.xlabel('year')
plt.ylabel('% BTC')
plt.savefig('sp500_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
