# region imports
from AlgorithmImports import *
# endregion

class CalmMagentaAlpaca(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 10, 28)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.sma = self.SMA(self.spy, 30 ,Resolution.Daily)
        closing_prices = self.History(self.spy, 30, Resolution.Daily)["close"]
        for time, price in closing_price.loc[self.spy].items():
            self.sma.Update(time,price)

    def OnData(self, data: Slice):
        if not self.sma.IsReady:
            return
        
        hist = self.History(self.spy, timedelta(365), Resolution.Daily)
        low = min(hist["low"])
        high = max(hist["high"])
        price = self.Securities[self.spy]

#18:15