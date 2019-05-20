#%%
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import seaborn as sns


quandl.ApiConfig.api_key = config.api_key

gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')
btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date='2016-01-05')
df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc)


# horizontal_stack = pd.concat([df1, df], axis=1) --> not sure this is even needed

plt.subplot(2, 1, 1)
plt.plot(gold.index, gold)

#TODO find out how to make graphs match, solve the NaN issue
plt.xticks(gold.index[0::85], [])


plt.title('Gold vs BTC')
plt.ylabel('Gold')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

plt.xlabel('year')
plt.ylabel('BTC')
plt.savefig('gold_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
