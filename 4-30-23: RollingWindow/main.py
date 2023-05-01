# region imports
from AlgorithmImports import *
# endregion

class RetrospectiveYellowGreenHornet(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 10, 29)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.symbol = self.AddEquity("SPY", Resolution.Minute).Symbol
        self.rollingWindow = RollingWindow[TradeBar](2)
        self.Consolidate(self.symbol, Resolution.Daily, self.BarHandle)
        self.Schedule.On(self.DateRules.EveryDay(self.symbol), self.TimeRules.BeforeMarketClose(self.symbol,15), self.exit)
    
    def OnData(self, data: Slice):
        if not self.rollingWindow.IsReady:
            return
        if not(self.Time.hour == 9 and self.Time.minute == 31):
            return
        if data[self.symbol].Open >= 1.01 * self.rollingWindow[0].Close:
            self.SetHoldings(self.symbol, -1)    
        elif data[self.symbol].Open <= 0.99 * self.rollingWindow[0].Close:
            self.SetHoldings(self.symbol,1)

    def BarHandle(self, bar):
        self.rollingWindow.Add(bar)

    def exit(self):
        self.Liquidate()
