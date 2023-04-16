# region imports
from AlgorithmImports import *
from tensorflow.python.keras.utils.generic_utils import serialize_keras_object
from tensorflow.python.keras.utils.generic_utils import serialize_keras_object
from tensorflow.keras import utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import json
# endregion

class AlertRedOrangeBull(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 10, 7)  
        self.SetEndDate(2022,1,1)

        model_key = 'bitcoin_prince_predictor'
        if self.ObjectStore.ContainsKey(model_key):
            model_str = self.ObjectStore.Read(model_key)
            config = json.loads(model_str)['config']
            self.model = Sequential.from_config(config)

        self.SetBrokerageModel(BrokerageName.Bitfinex, AccountType.Margin)
        self.SetCash(100000) 
        self.symbol = self.AddCrypto("BTCUSD", Resolution.Daily).Symbol
        self.SetBenchmark(self.symbol)
        

    def OnData(self, data: Slice):
        pass