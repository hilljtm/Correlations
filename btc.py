#%%
import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt



#send get request 
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi*3


plt.scatter(x, y, s=area, alpha=0.5)
plt.title('scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

