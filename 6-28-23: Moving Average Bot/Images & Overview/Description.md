Hello, 

This bot is also using a tutorial from quantconnect, however, I will soon be creating my own bots using trading strategies that I have learned from "Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications" by John Murphy. 
 
For what the goal of this bot was, it was to increase my knowledge on backtesting, and to learn more about overfitting and try to prevent it. 

The bot itself runs a simple algorithm, when SPY is above its simple moving average (or in an uptrend), the bot invests 80% available capital in SPY and 20% in BND (which is a Bond Market ETF). If SPY is below its simple moving average (aka in a downtrend), the bot does the oppisite and invests 80% of the available capital in BND and 20% in SPY. The reason the bot does this is because SPY and BND are inverses, when BND is up, SPY is down (and vice versa)