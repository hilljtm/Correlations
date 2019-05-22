# %%
from app import faang
import os
import sys
sys.path.append("copy path")


df = pd.read_csv("faangfinal.csv", index_col='Date', parse_dates=['Date'])

df1 = pd.read_csv("btcprice.csv", index_col='Date', parse_dates=['Date'])

# Mean of faang
df.mean()

# Sum of faang
df.sum()

# Subtract mean from the sum and assign x to result
# TODO math isn't correct, need to find right formula
x = df.sub(df.mean(axis=1), axis=0)
print(x)


# Mean of BTC
df1.mean()

# Sum of BTC
df1.sum()

# Subtract mean from sum and assign y to result
y = df1.sub(df.mean(axis=1), axis=0)
print(y)

# Find the corr
y.corr()
x.corr()


# Find the standard deviation
# .std()

#f, ax = plt.subplots(figsize=(10, 8))
#corr = faang.corr()
#sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True, ax=ax)

#fig = plt.figure()
#ax = plt.subplot()
# ax.plot(label='Faang')
# ax.legend(loc='upper_center', bbox_to_anchor=(0.5, -0.05)#, shadow=True, ncol=2)
#plt.title('FAANG vs BTC mean')
# plt.plot(faang.mean)
# plt.show()
