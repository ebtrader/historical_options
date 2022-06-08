# https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, func, DateTime, Float

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

meta = MetaData()

students = Table(
   'tqqq', meta,
    Column('id', Integer, nullable=False, autoincrement=True, primary_key = True),
    Column('datetime', DateTime),
    Column('open', Float),
    Column('high', Float),
    Column('low', Float),
    Column('close', Float),
    Column('ticker', String(10)),
    Column('strike', Integer),
    Column('expiration', DateTime),
   Column('time_created',DateTime(timezone=True), server_default=func.now())
)

meta.create_all(engine)
