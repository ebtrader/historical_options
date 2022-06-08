import pandas as pd
import os
from datetime import datetime

path = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area/'
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

file = path + dir_list[0]
df = pd.read_csv(file)
# df = df.reset_index(drop=True)    # remove index
df = df.iloc[: , 1:]              # remove first column
# print(df)

df[0] = df.astype(str)                  # convert to string
df = df[0].str.split(',', expand=True)  # split on delimiter ","
df = df.iloc[: , :-3]                   # remove last 3 columns

df = df.replace({'Date:':''}, regex=True)
df = df.replace({'Open:':''}, regex=True)
df = df.replace({'High:':''}, regex=True)
df = df.replace({'Low:':''}, regex=True)
df = df.replace({'Close:':''}, regex=True)
# df = df.replace({'Volume:':''}, regex=True)
# df = df.replace({'Average:':''}, regex=True)
# df = df.replace({'BarCount:':''}, regex=True)
print(df)

df.columns = ['datetime', 'open', 'high', 'low', 'close']
# df[['date', 'time']] = df['time'].str.split(' ', expand=True)
# df[['date', 'time']] = df['datetime'].str.split('|', expand=True).add_prefix(df['datetime'])
# df['time'] = df['time'].replace(' ', ',', regex=True)
df['datetime'] = df['datetime'].str.strip()
df['datetime'] = df['datetime'].replace('  ', ' ', regex=True)
# df['datetime'] = df['datetime'].replace('  ', '|', regex=True)
# df['datetime'] = df['datetime'].replace(' ', '', regex=True)
#df['datetime'] = df['datetime'].replace('|', ' ', regex=True)

# https://vertabelo.com/blog/what-datatype-should-you-use-to-represent-time-in-mysql-we-compare-datetime-timestamp-and-int/#:~:text=MySQL%20retrieves%20and%20displays%20DATETIME,microseconds%20(6%20digits)%20precision.

df.to_csv('test.csv')
print(df)

