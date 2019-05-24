# %%
import seaborn as sns
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
plt.style.use('seaborn')

quandl.ApiConfig.api_key = config.api_key

btc = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])

sp = pd.read_csv("sp500.csv", index_col='Date', parse_dates=['Date'])

sp = pd.DataFrame(sp)
btc = pd.DataFrame(btc)

# setting matplotlib plot
fig, ax = plt.subplots()
myFmt = mdates.DateFormatter('%d')
ax.xaxis.set_major_formatter(myFmt)
ax.xaxis_date()
plt.xticks(rotation=90)
plt.tight_layout()


plt.subplot(2, 1, 1)
plt.plot(sp.index, sp)
plt.xticks(sp.index[0::80], [])


plt.title('S&P500 vs BTC')
plt.ylabel('S&P500')
plt.subplot(2, 1, 2)
plt.plot(btc.index, btc)

fig.autofmt_xdate()
plt.xlabel('')
plt.ylabel('BTC')
plt.savefig('sp500_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
plt.show()
