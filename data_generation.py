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
DowJones_df = yf.download('DJIA',start_date,str(yesterday))
Nasdaq_df = yf.download('^IXIC',start_date,str(yesterday))
diff = Nasdaq_df.index.difference(DowJones_df.index)
# Display Dow Jones missing values
print(diff)

DowJones = np.asarray(DowJones_df.Close).reshape(-1,1)
Nasdaq = np.asarray(Nasdaq_df.drop(diff).Close).reshape(-1,1)
Russell = np.asarray(yf.download('^RUT',start_date,str(yesterday)).drop(diff).Close).reshape(-1,1)
SP500 = np.asarray(yf.download('^GSPC',start_date,str(yesterday)).drop(diff).Close).reshape(-1,1)

# Ensure the data have the same shape
assert DowJones.shape == Nasdaq.shape == Russell.shape == SP500.shape

ts = np.concatenate((DowJones, Nasdaq, Russell, SP500), axis=1)

# Calculate the log returns
ratios = np.log(ts / np.roll(ts, -1, axis=0))[:-1]

# Put the returns in a dataframe
tsdf = pd.DataFrame(ratios, index = DowJones_df.index[:-1])
tsdf.to_csv("latest.csv")