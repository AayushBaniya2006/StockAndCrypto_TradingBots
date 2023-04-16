# region imports
from AlgorithmImports import *
# endregion

class DeterminedSkyBlueDolphin(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 10, 13)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        spy = self.AddEquity("SPY", Resolution.Daily) 
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.spy = spy.Symbol

        self.SetBenchmark("SPY")
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage,AccountType.Margin)
        self.entryPrice = 0
        self.period = timedelta(15)
        self.nextEntryTime = self.Time


    def OnData(self, data: Slice):
        if not self.spy in data:
            return 
        price = data[self.spy].Close


        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy,1)
                self.Log("BUY SPY @" + str(price))
                self.entryPrice = price
        elif self.entryPrice * 1.2 < price or self.entryPrice * 0.9 >price:
            self.Liquidate()
            self.Log("SELL SPY @" + str(price))
            self.nextEntryTime = self.Time + self.period