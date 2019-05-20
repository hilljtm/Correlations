# %%
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import seaborn as sns
import config

style.use('seaborn')

quandl.ApiConfig.api_key = config.api_key

data = quandl.get_table('WIKI/PRICES', ticker=['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOG'], qopts={'columns': [
                        'ticker', 'date', 'adj_close']}, date={'gte': '2016-01-05', 'lte': '2018-03-27'}, paginate=True)
                        
btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date="2016-01-01")

new = data.set_index('date')


clean = new.pivot(columns='ticker')


fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.tight_layout()


plt.subplot(2, 1, 1)
plt.plot(clean.index, clean)

#change y ticks so faang graph isnt flat
plt.xticks(clean.index[0::85], [])


plt.title('FAANG vs BTC')
plt.ylabel('FAANG')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

fig.autofmt_xdate()
plt.xlabel('year')
plt.ylabel('BTC')
#plt.savefig('faang_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
