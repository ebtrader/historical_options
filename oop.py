from mid_and_bid import TestApp
import pandas as pd
from sqlalchemy import create_engine

class Pull:

    def duck(self):
        app = TestApp()
        app.connect("127.0.0.1", port=7497, clientId=102)
        print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
        app.run()

    def gazelle(self):
        path = 'C:/Users/jsidd/PycharmProjects/text_files/host_name.txt'
        with open(path) as g:
            host = g.read()

        # Credentials to database connection
        path1 = 'C:/Users/jsidd/PycharmProjects/text_files/db.txt'
        with open(path1) as h:
            db = h.read()

        path2 = 'C:/Users/jsidd/PycharmProjects/text_files/uname.txt'
        with open(path2) as i:
            username = i.read()

        path3 = 'C:/Users/jsidd/PycharmProjects/text_files/word.txt'
        with open(path3) as j:
            word = j.read()

        # Create SQLAlchemy engine to connect to MySQL Database
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                               .format(host=host, db=db, user=username, pw=word))

        df = pd.read_csv('history2.csv')

        # Convert dataframe to sql table
        df.to_sql('history2', engine, index=False)

def main():
    app1 = Pull()
    app1.duck()
    app1.gazelle()

if __name__ == "__main__":
    main()
