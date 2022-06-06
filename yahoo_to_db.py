import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

# https://www.dataquest.io/blog/sql-insert-tutorial/

# bring the new data into pandas
# ingest pandas into staging area
# join pandas dataframe into existing table

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

ticker = "TQQQ"

df = yf.download(tickers=ticker, period='6mo', interval='1d')
df = df.reset_index()

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=host, db=db, user=username, pw=word))

# Convert dataframe to sql table
df.to_sql('yahoo1', engine, index=False)



