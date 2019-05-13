# %%
import quandl 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()

quandl.ApiConfig.api_key = 'API_KEY'
data = quandl.get("BITFINEX/BTCUSD", start_date="2016-01-01")
data = data[["Last"]] 
