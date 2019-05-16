# %%
import config
import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

#using quandl API, returning only last price
quandl.ApiConfig.api_key = config.api_key
data = quandl.get("BITFINEX/BTCUSD", start_date="2016-01-01")
data = data[["Last"]]
pd.DataFrame(data, columns=['Last'])
plt.rcParams["figure.figsize"] = [16,9]
plt.plot(data)


