# %%

import quandl
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import requests



data = requests.get('https://www.quandl.com/api/v3/datasets/WGC/GOLD_DAILY_USD.csv?')
data.json