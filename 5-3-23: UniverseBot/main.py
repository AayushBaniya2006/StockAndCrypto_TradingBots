# region imports
from AlgorithmImports import *
# endregion

class CalculatingTanFrog(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019, 1, 1) # Set Start Date
        self.SetEndDate(2021, 1, 1) 
        self.SetCash(100000)  # Set Strategy Cash
        self.rebalanceTime = datetime.min
        self.activeStocks = set()

        self.AddUniverse(self.CoarseFilter, self.FineFilter)
        self.UniverseSettings.Resolution = Resolution.Hour

        self.portfolioTargets = []

    def CoarseFilter(self, coarse):
        if self.Time <= self.rebalanceTime:
            return self.Universe.Unchanged
        filtered = [x for x in coarse if x.Price > 10 and x.HasFundamentalData]
        sortedByDollarVolume = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume][:200]
        
    def FineFilter(self, fine): 
        sortedByPE = sorted(fine, key=lambda x: x.MarketCap) 
        return [x.Symbol for x in sortedByPE if x.MarketCap > 0][:10]

    def OnSecuritiesChanged(self, changes):
        for x in changes.RemovedSecurities:
            if x.Symbol in self.activeStocks:
                self.Liquidate(x.Symbol)
                self.activeStocks.remove(x.Symbol)
        for x in changes.AddedSecurities:
            self.activeStocks.add(x.Symbol)
        
        self.portfolioTargets = [PortfolioTarget(symbol, 1/len(self.activeStocks)) for symbol in self.activeStocks]
        
    def OnData(self, data: Slice):
        for symbol in self.activeStocks:
            if symbol not in data:
                return 
        self.SetHoldings(self.portfolioTargets)
        self.portfolioTargets = []
        
