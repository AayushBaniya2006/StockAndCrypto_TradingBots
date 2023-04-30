# region imports
from AlgorithmImports import *
# endregion

class CalmMagentaAlpaca(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 10, 28)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("TSLA", Resolution.Daily).Symbol
        self.sma = self.SMA(self.spy, 30 ,Resolution.Daily)
        closing_prices = self.History(self.spy, 30, Resolution.Daily)["close"]
        for time, price in closing_prices.loc[self.spy].items():
            self.sma.Update(time,price)

    def OnData(self, data: Slice):
        if not self.sma.IsReady:
            return
        
        #inefficent, sliding door could fix this however not too big of a deal
        hist = self.History(self.spy, timedelta(252), Resolution.Daily)
        high = max(hist["high"])
        low = min(hist["low"])
        price = self.Securities[self.spy].Price


#the point of this is too see if there is a breakout (primarily in a bullish market), this will be done via the 5% increase in comparison to the past year
# the then seeing if the SMA is below the current price is to see if there is an uptrend happening.         
        if price*1.05 >= high and self.sma.Current.Value < price:
            if not self.Portfolio[self.spy].IsLong:
                self.SetHoldings(self.spy,1)
#exact oppisite of what was previously said
        elif price*.095<=low and self.sma.Current.Value > price:
            if not self.Portfolio[self.spy].IsShort:
                self.SetHoldings(self.spy,1)
        else:
            self.Liquidate()

        self.Plot("Benchmark", "52 Week High", high)
        self.Plot("Benchmark", "52 Week Low", low)
        self.Plot("Benchmark", "SMA", self.sma.Current.Value)

        