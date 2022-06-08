import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os

# Set up of the engine to connect to the database
# the urlquote is used for passing the password which might contain special characters such as "/"
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

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                .format(host=host, db=db, user=username, pw=word))

conn = engine.connect()
# Set up of the table in db and the file to import

tableToWriteTo = 'tqqq'

# Panda to create a lovely dataframe
dq_path = 'C:/Users/jsidd/PycharmProjects/historical_options/data_quality/'
file = 'TQQQ_31_20220610_dq.csv'
filename = dq_path + file
df_to_be_written = pd.read_csv(filename)
print(df_to_be_written)

# The orient='records' is the key of this, it allows to align with the format mentioned in the doc to insert in bulks.
listToWrite = df_to_be_written.to_dict(orient='records')

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
#
