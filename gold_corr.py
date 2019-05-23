# %%
import seaborn as sns
import config
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


quandl.ApiConfig.api_key = config.api_key

gold = quandl.get("WGC/GOLD_DAILY_USD", start_date='2016-01-05')


btc = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Dates'])
df1 = pd.DataFrame(data=gold)
df = pd.DataFrame(data=btc)

#Export gold to csv, clean NaN columns, merge btc and gold
gbdf = pd.merge

def corr(x, y, **kwargs):
    coef = np.corrcoef(x, y)[0][1]
    label = r'$\rho$ = ' + str(round(coef, 2))

    ax = plt.gca()
    ax.annotate(label, xy=(0.2, 0.95), size=10, xycoords=ax.transAxes)


grid = sns.PairGrid(data=df, vars=['GOLD', 'BTC'], size=4)

grid = grid.map_upper(plt.scatter, color='darkred')
gird = grid.map_upper(corr)
grid = grid.map_lower(sns.kdeplot, cmap='Reds')
grid = grid.map_diag(plt.hist, bins=10, edgecolor='k', color='darkred')

