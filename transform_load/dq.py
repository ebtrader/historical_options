import pandas as pd
import os

counter = 0
path = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area/'
dq_path = 'C:/Users/jsidd/PycharmProjects/historical_options/data_quality/'
dir_list = os.listdir(path)

while counter < len(dir_list):
    for i in dir_list:
        print("Files and directories in '", path, "' :")

        # prints list of all files
        print(dir_list)

        list_position = counter
        filename = dir_list[list_position]
        file = path + filename
        df = pd.read_csv(file)
        # print(df)

        df = df.reset_index(drop=True)    # remove index
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
        # print(df)

        df.columns = ['datetime', 'open', 'high', 'low', 'close']
        df['open'] = pd.to_numeric(df['open'])
        df['high'] = pd.to_numeric(df['high'])
        df['low'] = pd.to_numeric(df['low'])
        df['close'] = pd.to_numeric(df['close'])

        # df[['date', 'time']] = df['time'].str.split(' ', expand=True)
        # df[['date', 'time']] = df['datetime'].str.split('|', expand=True).add_prefix(df['datetime'])
        # df['time'] = df['time'].replace(' ', ',', regex=True)
        df['datetime'] = df['datetime'].str.strip()
        df['datetime'] = df['datetime'].replace('  ', ' ', regex=True)
        df['datetime'] = pd.to_datetime(df['datetime'])
        # https://vertabelo.com/blog/what-datatype-should-you-use-to-represent-time-in-mysql-we-compare-datetime-timestamp-and-int/#:~:text=MySQL%20retrieves%20and%20displays%20DATETIME,microseconds%20(6%20digits)%20precision.

        # strip out Ticker Strike and Expiration
        filename = dir_list[list_position]
        ticker = filename.split('_')[0]
        strike = filename.split('_')[1]
        expiration = filename.split('_')[2]

        df['ticker'] = ticker
        df['strike'] = strike
        df['expiration'] = expiration
        df['expiration'] = pd.to_datetime(df['expiration'])

        filename_combo = ticker + '_' + strike + '_' + expiration + '_dq'
        filename_dq = '%s.csv' % filename_combo

        df.to_csv(dq_path + filename_dq, index=False)
        print(df)
        counter = counter + 1

#
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import pandas as pd
#
#
# # Set up of the engine to connect to the database
# # the urlquote is used for passing the password which might contain special characters such as "/"
# # Credentials to database connection
# path = 'C:/Users/jsidd/PycharmProjects/text_files/host_name.txt'
# with open(path) as g:
#     host = g.read()
#
# path1 = 'C:/Users/jsidd/PycharmProjects/text_files/db.txt'
# with open(path1) as h:
#     db = h.read()
#
# path2 = 'C:/Users/jsidd/PycharmProjects/text_files/uname.txt'
# with open(path2) as i:
#     username = i.read()
#
# path3 = 'C:/Users/jsidd/PycharmProjects/text_files/word.txt'
# with open(path3) as j:
#     word = j.read()
#
# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
#                 .format(host=host, db=db, user=username, pw=word))
#
# conn = engine.connect()
# # Set up of the table in db and the file to import
#
# tableToWriteTo = 'tqqq'
#
# # Panda to create a lovely dataframe
# df_to_be_written = df
# # The orient='records' is the key of this, it allows to align with the format mentioned in the doc to insert in bulks.
# listToWrite = df_to_be_written.to_dict(orient='records')
#
# metadata = sqlalchemy.schema.MetaData(bind=engine)
# table = sqlalchemy.Table(tableToWriteTo, metadata, autoload=True)
#
# # Open the session
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Inser the dataframe into the database in one bulk
# conn.execute(table.insert(), listToWrite)
#
# # Commit the changes
# session.commit()
#
# # Close the session
# session.close()
#
# # counter = counter + 1
