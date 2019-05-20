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

data = quandl.get("BITFINEX/BTCUSD", column_index='1', start_date="2016-01-01")
df = pd.DataFrame(data)


plt.rcParams["figure.figsize"] = [16, 9]
plt.title('BTC')
plt.xlabel('Date')
plt.ylabel('$Price')
plt.plot(df)
plt.savefig('btc.png', facecolor='w', edgecolor='w', bbox_inches='tight')
