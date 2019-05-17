#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import seaborn as sns

fig = plt.figure()
ax = plt.axis()

data = pd.read_csv("sp500.csv")
df = pd.DataFrame(data)

x = df['Date']
y = df['Price']

plt.rcParams["figure.figsize"] = [16,9]
plt.title("S&P500")
plt.xlabel('Date')
plt.ylabel('$Price')
plt.plot(x, y)

