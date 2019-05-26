# %%
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from app import spindex
mpl.rcParams['figure.dpi'] = 300
sns.set_style('whitegrid', {"axes.facecolor": ".9"})

sp = pd.read_csv("sp500.csv", index_col='Date', parse_dates=['Date'])

sbtc = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])

# merging sp and btc files
spbtc = sp.merge(sbtc, on=['Date'])
spbtc.corr(method='pearson')
spbtc.corr()


# plotting correlation using seaborn

def corr(x, y, **kwargs):
    coef = np.corrcoef(x, y)[0][1]
    label = r'$\rho$ = ' + str(round(coef, 2))

    ax = plt.gca()
    ax.annotate(label, xy=(0.2, 0.95), size=10, xycoords=ax.transAxes)


grid = sns.PairGrid(data=spbtc, vars=['SP500', 'BTC'], size=4)

grid = grid.map_upper(plt.scatter, color='darkred')
grid = grid.map_upper(corr)
grid = grid.map_lower(sns.kdeplot, cmap='Reds')
grid = grid.map_diag(plt.hist, bins=10, edgecolor='k', color='darkred')

plt.savefig('spincorr.png', facecolor='w',
            edgecolor='w', bbox_inches='tight')
