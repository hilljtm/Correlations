# %%
import config
import seaborn as sns
import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
plt.style.use('seaborn')


df = pd.read_csv("faangfinal.csv", index_col='Date', parse_dates=['Date'])


btc = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date="2016-01-05")
df1 = pd.DataFrame(btc)
df1.columns = ['Price']


faang = df.merge(df1, on=['Date'])
faang.describe()
#faang[['Price_x', 'Price_y']].cov()
#faang.describe()



#fig, ax = plt.subplots()
#plt.xticks(rotation=90)
#plt.tight_layout()
#
#
#plt.subplot(2, 1, 1)
#plt.plot(df)
#
## change y ticks so faang graph isnt flat
#
#plt.title('FAANG vs BTC')
#plt.ylabel('FAANG')
#plt.subplot(2, 1, 2)
#plt.plot(btc.index, btc)
#
#fig.autofmt_xdate()
#plt.xlabel('year')
#plt.ylabel('BTC')
#plt.savefig('faang_btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
#plt.show()