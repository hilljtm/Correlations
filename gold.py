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

plt.subplot(2, 1, 1)
plt.plot(df1.index, df1)

plt.xticks(df1.index[0::36], [])


plt.title('Gold vs BTC')
plt.ylabel('% Gold')
plt.subplot(2, 1, 2)
plt.plot(df.index, df)
plt.yticks(df.index[0::100], [])

plt.xlabel('year')
plt.ylabel('% BTC')
#plt.savefig('gold_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
