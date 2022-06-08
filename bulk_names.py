
# https://stackoverflow.com/questions/9070764/insert-auto-increment-primary-key-to-existing-table

# https://stackoverflow.com/questions/31997859/bulk-insert-a-pandas-dataframe-using-sqlalchemy

# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
import pandas as pd


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
# Base = declarative_base()

#Declaration of the class in order to write into the database. This structure is standard and should align with SQLAlchemy's doc.
 # class Current(Base):
 #    __tablename__ = 'tablename'
 #
 #    # id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
 #    Date = Column(String(500), primary_key=True)
 #    Type = Column(String(500))
 #    Value = Column(Numeric())
 #
 #    def __repr__(self):
 #        return "(Date='%s', Type='%s', Value='%s')" % (self.Date, self.Type, self.Value)

# Set up of the table in db and the file to import
fileToRead = 'names.csv'
tableToWriteTo = 'students'

# Panda to create a lovely dataframe
df_to_be_written = pd.read_csv(fileToRead)
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