#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sp_df = pd.read_csv("spindex.csv")
df = pd.DataFrame(sp_df)
df
