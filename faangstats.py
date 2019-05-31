# %%
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from app import faang
import os
import sys
sys.path.append("path to file")
mpl.rcParams['figure.dpi'] = 300
sns.set_style('whitegrid', {"axes.facecolor": ".9"})


df = pd.read_csv("faangfinal.csv", index_col='Date', parse_dates=['Date'])

df1 = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])


df3 = df.merge(df1, on=['Date'])
df3.corr(method='pearson')


def corr(x, y, **kwargs):
    coef = np.corrcoef(x, y)[0][1]
    label = r'$\rho$ = ' + str(round(coef, 2))

    ax = plt.gca()
    ax.annotate(label, xy=(0.2, 0.95), size=10, xycoords=ax.transAxes)


grid = sns.PairGrid(data=df3, vars=['FAANG', 'BTC'], size=4)

grid = grid.map_upper(plt.scatter, color='darkred')
grid = grid.map_upper(corr)
grid = grid.map_lower(sns.kdeplot, cmap='Blues')
grid = grid.map_diag(plt.hist, bins=10, edgecolor='k', color='darkred')

plt.savefig('faangcorco.png', facecolor='w',
           edgecolor='w', bbox_inches='tight')
