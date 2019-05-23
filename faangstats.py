# %%
from app import faang
import os
import sys
sys.path.append("path to file")
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl 
import seaborn as sns
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
    ax.annotate(label, xy=(0.2, 0.95), size=20, xycoords=ax.transAxes)
    
grid = sns.PairGrid(data=df3, vars=['FAANG', 'BTC'], size=4)

grid = grid.map_upper(plt.scatter, color='darkred')
gird = grid.map_upper(corr)
grid = grid.map_lower(sns.kdeplot, cmap='Reds')
grid = grid.map_diag(plt.hist, bins=10, edgecolor='k', color='darkred')


plt.savefig('faangcorco.png', facecolor='w', edgecolor='w', bbox_inches='tight')
# Mean of faang
#df.mean()

# Sum of faang
#df.sum()
#df

# Subtract mean from the sum and assign x to result
# TODO math isn't correct, need to find right formula
#x = (df.mean() - df.sum())
#x


# Mean of BTC
#df1.mean()

# Sum of BTC
#df1.sum()

# Subtract mean from sum and assign y to result
#y = df1.sub(df.mean(axis=1), axis=0)
#print(y)

# Find the corr
#y.corr()
#x.corr()


# Find the standard deviation
# .std()
