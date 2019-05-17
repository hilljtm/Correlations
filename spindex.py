#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import seaborn



df = pd.read_csv("sp500.csv")

x = df['Date']
y = df['Price']

plt.plot(x, y)
plt.grid(color='gray', linestyle='solid')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

