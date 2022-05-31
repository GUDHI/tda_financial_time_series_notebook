# Import the yahoo! finance
import yfinance as yf
import numpy as np
import pandas as pd
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
# To get yesterday's date
start_date = '1988-01-01'

# Dealing with some missing values in Dow Jones index
df = yf.download('^DJI ^IXIC ^GSPC ^RUT',start_date,str(yesterday))
# Dealing with some missing values
df = df.Close.dropna(axis=0)
ts = np.asarray(df)

# Calculate the log returns
ratios = np.log(ts / np.roll(ts, -1, axis=0))[:-1]

# Put the returns in a dataframe
tsdf = pd.DataFrame(ratios, index = df.index[:-1])
tsdf.to_csv("latest.csv")