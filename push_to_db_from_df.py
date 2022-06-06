import logging
import time
import pandas as pd
from ibapi.utils import iswrapper
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
# types
from ibapi.common import *  # @UnusedWildImport
from ibapi.contract import * # @UnusedWildImport
import time
from sqlalchemy import create_engine

# https://stackoverflow.com/questions/41510945/interactive-brokers-obtain-historical-data-of-opt-midpoint-and-trades
# https://groups.io/g/twsapi/topic/data_for_expired_contracts_no/4042776?p=

class TestApp(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        self.data = []  # Initialize variable to store candle
        self.contract = Contract()

    def nextValidId(self, orderId: int):
        # we can start now
        self.start()

    def start(self):
        self.historicalDataOperations_req()
        print("Executing requests ... finished")

    def historicalDataOperations_req(self):
        self.contract.symbol = "TQQQ"
        self.contract.secType = "OPT"
        self.contract.exchange = "SMART"
        self.contract.currency = "USD"
        self.contract.lastTradeDateOrContractMonth = "20220610"
        self.contract.strike = 32
        self.contract.right = "C"
        self.contract.multiplier = "100"

        # https://interactivebrokers.github.io/tws-api/historical_bars.html

        self.reqHistoricalData(4103, self.contract, '',
                               "2 D", "1 hour", "MIDPOINT", 1, 1, False, [])

        self.reqHistoricalData(4104, self.contract, '',
                               "2 D", "1 hour", "BID", 1, 1, False, [])


        # https://interactivebrokers.github.io/tws-api/historical_bars.html

    def historicalData(self, reqId: int, bar: BarData):

        print("HistoricalData. ReqId:", reqId, "BarData.", bar)

        self.data.append([reqId, bar])

        df = pd.DataFrame(self.data)
        # print(df)
        df.to_csv('history1.csv')

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.disconnect()

def main():
    app = TestApp()
    app.connect("127.0.0.1", port=7497, clientId=102)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
    app.run()
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

    df = pd.read_csv('history1.csv')

    # Convert dataframe to sql table
    df.to_sql('history1', engine, index=False)



if __name__ == "__main__":
    main()

