import pandas as pd
from AlgorithmImports import *

class AdaptableAsparagusLemur(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2015, 1, 1)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)

        self.apple = self.AddEquity("AAPL", Resolution.Daily).Symbol
        self.sma = self.SMA(self.apple, 30, Resolution.Daily)
        self.Volatility = self.AddEquity("VIX", Resolution.Daily).Symbol

        self.symbol_data = {}

    def CalculateFearAndGreedIndex(self):
        for symbol in self.symbol_data:
            history = self.symbol_data[symbol]
            ma_200 = history['close'].mean()
            current_price = self.Securities[symbol].Price

            if current_price > ma_200:
                sentiment = "Greed"
            else:
                sentiment = "Fear"

            self.Debug(f"Symbol: {symbol.Value}, Current Price: {current_price}, Sentiment: {sentiment}")

            if symbol == self.apple:
                if current_price > ma_200 and self.Securities[self.Volatility].Price > self.sma.Current.Value:
                    self.SetHoldings(symbol, -0.2)
                elif current_price < ma_200 and self.Securities[self.Volatility].Price < self.sma.Current.Value:
                    self.SetHoldings(symbol, 0.2)

    def OnData(self, data):
        for symbol in data.Keys:
            if symbol not in self.symbol_data:
                self.symbol_data[symbol] = pd.DataFrame(columns=["close"])

            self.symbol_data[symbol] = self.symbol_data[symbol].append(
                pd.DataFrame(
                    {
                        "close": [data[symbol].Close],
                    },
                    index=[self.Time]
                )
            )

        self.CalculateFearAndGreedIndex()
