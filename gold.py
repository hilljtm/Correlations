#%%
import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


quandl.ApiConfig.api_key = 'W6U4YhAz2q7bigp7tQge'
data = quandl.get("WGC/GOLD_DAILY_USD", start_date="2016-01-01")

g = sns.relplot(kind='line', data=data)
g.fig.autofmt_xdate()
plt.plot()

#saving figure into a bytes object and you can expose it after