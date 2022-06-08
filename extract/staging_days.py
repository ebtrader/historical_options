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
import os

# https://stackoverflow.com/questions/41510945/interactive-brokers-obtain-historical-data-of-opt-midpoint-and-trades
# https://groups.io/g/twsapi/topic/data_for_expired_contracts_no/4042776?p=

CHAIN = [16,17,18,19,20,21,21.5,22,22.5,23,23.5,24,24.5,25,26,27,28,29,30,31,32,33,33.5,34,34.5,35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,45.5,46,47,48,49,50,51,55]
PATH = '../position.txt'
STAGING = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area/'
TICKER = 'TQQQ'

class TestApp(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        self.data = []  # Initialize variable to store candle
        self.contract = Contract()
        self.df = pd.DataFrame()
        self.strike = 0
        self.expiration = 0
        self.chain = CHAIN
        self.path = PATH
        self.staging = STAGING
        self.ticker = TICKER

    def nextValidId(self, orderId: int):
        # we can start now
        self.start()

    def start(self):
        self.historicalDataOperations_req()
        print("Executing requests ... finished")

    def historicalDataOperations_req(self):
        self.expiration = '20220610'
        self.path = '../position.txt'
        with open(self.path) as g:
            position = g.read()
        # self.chain = [30, 31, 32, 33]
        strike_position = int(position)
        self.strike = self.chain[strike_position]
        counter = str(strike_position + 1)
        with open(self.path, "w") as h:
            h.write(counter)
        self.contract.symbol = self.ticker
        self.contract.secType = "OPT"
        self.contract.exchange = "SMART"
        self.contract.currency = "USD"
        self.contract.lastTradeDateOrContractMonth = self.expiration
        self.contract.strike = self.strike
        self.contract.right = "C"
        self.contract.multiplier = "100"

        # https://interactivebrokers.github.io/tws-api/historical_bars.html

        self.reqHistoricalData(4103, self.contract, '',
                               "8 D", "5 mins", "MIDPOINT", 1, 1, False, [])

        # self.reqHistoricalData(4104, self.contract, '',
        #                        "2 D", "1 hour", "BID", 1, 1, False, [])
        #

        # https://interactivebrokers.github.io/tws-api/historical_bars.html

    def historicalData(self, reqId: int, bar: BarData):
        # print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        self.data.append([reqId, bar])
        self.df = pd.DataFrame(self.data)
        # print(df)
        # https://www.adamsmith.haus/python/answers/how-to-create-a-filename-using-variables-in-python
        filename_combo = str(self.ticker) + '_' + str(self.strike) + '_' + str(self.expiration) + '_'
        filename = '%s.csv' % filename_combo
        self.df.to_csv(self.staging + filename, index=False)
        # https://stackoverflow.com/questions/22872952/set-file-path-for-to-csv-in-pandas


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        # print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.disconnect()

def main():
    counter1 = 0
    initial_value = str(0)
    while counter1 < len(CHAIN):
        if counter1 == len(CHAIN) - 1:
            app = TestApp()
            app.connect("127.0.0.1", port=7497, clientId=102)
            print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
            app.run()
            counter1 = counter1 + 1
            with open(PATH, "w") as i:
                i.write(initial_value)
        else:
            app = TestApp()
            app.connect("127.0.0.1", port=7497, clientId=102)
            print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
            app.run()
            counter1 = counter1 + 1


if __name__ == "__main__":
    main()

