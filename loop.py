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

# https://stackoverflow.com/questions/41510945/interactive-brokers-obtain-historical-data-of-opt-midpoint-and-trades
# https://groups.io/g/twsapi/topic/data_for_expired_contracts_no/4042776?p=

class TestApp(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        self.data = []  # Initialize variable to store candle
        self.contract = Contract()
        self.df = pd.DataFrame()

    def nextValidId(self, orderId: int):
        # we can start now
        self.start()

    def start(self):
        self.historicalDataOperations_req()
        print("Executing requests ... finished")

    def historicalDataOperations_req(self):
        path = 'position.txt'
        with open(path) as g:
            position = g.read()
        chain = [30, 31, 32, 33]
        strike_position = int(position)
        strike = chain[strike_position]
        counter = str(strike_position + 1)
        with open(path, "w") as h:
            h.write(counter)
        self.contract.symbol = "TQQQ"
        self.contract.secType = "OPT"
        self.contract.exchange = "SMART"
        self.contract.currency = "USD"
        self.contract.lastTradeDateOrContractMonth = "20220610"
        self.contract.strike = strike
        self.contract.right = "C"
        self.contract.multiplier = "100"

        # https://interactivebrokers.github.io/tws-api/historical_bars.html

        self.reqHistoricalData(4103, self.contract, '',
                               "1 D", "1 hour", "MIDPOINT", 1, 1, False, [])

        # self.reqHistoricalData(4104, self.contract, '',
        #                        "2 D", "1 hour", "BID", 1, 1, False, [])
        #

        # https://interactivebrokers.github.io/tws-api/historical_bars.html

    def historicalData(self, reqId: int, bar: BarData):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)

        self.data.append([reqId, bar])
        self.df = pd.DataFrame(self.data)
        # print(df)
        self.df.to_csv('history4.csv')


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.disconnect()

def main():
    app = TestApp()
    app.connect("127.0.0.1", port=7497, clientId=102)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
    app.run()


if __name__ == "__main__":
    main()

