import pandas as pd
from sqlalchemy import create_engine

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

# Create dataframe
df = pd.DataFrame(data=[[111,'Thomas','35','United Kingdom'],
		[222,'Ben',42,'Australia'],
		[333,'Harry',28,'India']],
		columns=['id','name','age','country'])

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=host, db=db, user=username, pw=word))

# Convert dataframe to sql table
df.to_sql('new_users5', engine, index=False)



