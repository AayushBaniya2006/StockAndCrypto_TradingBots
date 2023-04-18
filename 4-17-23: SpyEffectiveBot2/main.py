
from AlgorithmImports import *
# endregion

class JumpingTanCobra(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 4, 15)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        spy = self.AddEquity("SPY", Resolution.Daily) 
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.spy = spy.Symbol

        self.SetBenchmark("SPY")
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage,AccountType.Margin)
        self.entryPrice = 0
        self.period = timedelta(7)
        self.pricedropholder = 0
        self.nextEntryTime = self.Time
        


    def OnData(self, data: Slice):
        
        if not self.spy in data:
            return 

        self.dailyprice = data[self.spy].Close
         
        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time and self.dailyprice > self.pricedropholder:
                self.SetHoldings(self.spy,1)
                self.Log("BUY SPY @" + str(self.dailyprice))
                self.entryPrice = data[self.spy].Close
            
        elif(self.entryPrice * .90<=self.dailyprice):
            self.Liquidate()
            self.Log("SELL SPY @" + str(self.dailyprice))
            liquidatePrice = data[self.spy].Close
            self.nextEntryTime = self.Time + self.period
            self.pricedropholder = self.dailyprice
            

        elif(self.entryPrice*1.1>=self.dailyprice and holder == True):
            if(self.dailyprice < self.holderprice):
                self.Liquidate()
                self.Log("SELL SPY @" + str(self.dailyprice))
                self.nextEntryTime = self.Time + self.period
                self.pricedropholder = self.dailyprice
            if(self.entryPrice*1.3>=self.dailyprice): 
                self.Liquidate()
                self.Log("SELL SPY @" + str(self.dailyprice))
                holder=False

        elif(self.entryPrice*1.1>=self.dailyprice):
            self.holderprice = self.dailyprice
            self.holder = True
            if(self.entryPrice*1.3>=self.dailyprice): 
                self.Liquidate()
                self.Log("SELL SPY @" + str(self.dailyprice))
                holder=False