#%%
from faang import *


#Find the mean 
#faang.mean()

#Find the corr
#faang.corr()

#Find the median 
#faang.median()

#Find the standard deviation
#faang.std()

fig = plt.figure()
ax = plt.subplot()
ax.plot(label='Faang')
ax.legend(loc='upper_center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.title('FAANG vs BTC mean')
plt.plot(faang)
plt.show()
