# https://www.geeksforgeeks.org/read-sql-database-table-into-a-pandas-dataframe-using-sqlalchemy/

# import the modules
import pandas as pd
from sqlalchemy import create_engine
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
df = pd.read_sql_table(table_name, conn, )
print(df)
