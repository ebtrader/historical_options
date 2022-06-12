# https://www.geeksforgeeks.org/read-sql-database-table-into-a-pandas-dataframe-using-sqlalchemy/

# import the modules
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#
# # SQLAlchemy connectable
# cnx = create_engine('sqlite:///contacts.db').connect()
#
# # table named 'contacts' will be returned as a dataframe.
# df = pd.read_sql_table('contacts', cnx)
# print(df)

# Credentials to database connection
path = 'C:/Users/jsidd/PycharmProjects/text_files/host_name.txt'
with open(path) as g:
    host = g.read()

path1 = 'C:/Users/jsidd/PycharmProjects/text_files/db.txt'
with open(path1) as h:
    db = h.read()

path2 = 'C:/Users/jsidd/PycharmProjects/text_files/uname.txt'
with open(path2) as i:
    username = i.read()

path3 = 'C:/Users/jsidd/PycharmProjects/text_files/word.txt'
with open(path3) as j:
    word = j.read()

table_name='tqqq_raw'

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=host, db=db, user=username, pw=word, table=table_name))

conn = engine.connect()
df = pd.read_sql_table(table_name, conn)
# print(df)
df['1'] = df['1'].astype(str)                  # convert to string
df[['datetime', 'open','high','low','close','volume','average','bar']] = df['1'].str.split(',', expand=True)  # split on delimiter ","
df = df.iloc[: , :-3]                   # remove last 3 columns
df = df.iloc[: , 1:]                   # remove first n columns columns
df.drop("time_created", axis=1, inplace=True)
df.drop("1", axis=1, inplace=True)
df = df.rename(columns = {'0':'code'})

df = df.replace({'Date:':''}, regex=True)
df = df.replace({'Open:':''}, regex=True)
df = df.replace({'High:':''}, regex=True)
df = df.replace({'Low:':''}, regex=True)
df = df.replace({'Close:':''}, regex=True)

df['datetime'] = df['datetime'].str.strip()
df['datetime'] = df['datetime'].replace('  ', ' ', regex=True)
df['datetime'] = pd.to_datetime(df['datetime'])

# print(df)
# df.to_csv('test.csv', index=False)

tableToWriteTo = 'tqqq_bid_ask'

# The orient='records' is the key of this, it allows to align with the format mentioned in the doc to insert in bulks.
listToWrite = df.to_dict(orient='records')

metadata = sqlalchemy.schema.MetaData(bind=engine)
table = sqlalchemy.Table(tableToWriteTo, metadata, autoload=True)

# Open the session
Session = sessionmaker(bind=engine)
session = Session()

# Inser the dataframe into the database in one bulk
conn.execute(table.insert(), listToWrite)

# Commit the changes
session.commit()

# Close the session
session.close()