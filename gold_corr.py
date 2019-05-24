# %%
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from app import gold
mpl.rcParams['figure.dpi'] = 300
sns.set_style('whitegrid', {"axes.facecolor": ".9"})


gold = pd.read_csv("gold.csv", index_col='Date', parse_dates=['Date'])

btc = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])

gold = pd.DataFrame(data=gold)
btc = pd.DataFrame(data=btc)

# merging gold and btc files
gbdf = gold.merge(btc, on=['Date'])
gbdf.corr(method='pearson')
gbdf.corr()


# plotting correlation using seaborn

def corr(x, y, **kwargs):
    coef = np.corrcoef(x, y)[0][1]
    label = r'$\rho$ = ' + str(round(coef, 2))

    ax = plt.gca()
    ax.annotate(label, xy=(0.2, 0.95), size=10, xycoords=ax.transAxes)


grid = sns.PairGrid(data=gbdf, vars=['GOLD', 'BTC'], size=4)

grid = grid.map_upper(plt.scatter, color='darkred')
gird = grid.map_upper(corr)
grid = grid.map_lower(sns.kdeplot, cmap='Reds')
grid = grid.map_diag(plt.hist, bins=10, edgecolor='k', color='darkred')

plt.savefig('goldcorr.png', facecolor='w',
            edgecolor='w', bbox_inches='tight')
