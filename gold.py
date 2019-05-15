#%%
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


quandl.ApiConfig.api_key = 'YOUR_KEY'
gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')
btc = quandl.get("BITFINEX/BTCUSD", start_date='2016-01-05')
btc = btc[['High']]


plt.subplot(2, 1, 1)
plt.plot(gold.index, gold)

plt.xticks(gold.index[0::80], [])


plt.title('Gold vs BTC')
plt.ylabel('% Gold')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

plt.xlabel('year')
plt.ylabel('% BTC')
plt.savefig('gold_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
