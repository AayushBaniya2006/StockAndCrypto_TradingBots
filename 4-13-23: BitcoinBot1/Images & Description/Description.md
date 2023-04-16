Hello! 

This was my first crypto project, it takes a 40 day analysis of the market and how it expects bitcoin to flucuate day by day.

As this was my first project, the main goal was just to learn about some trading strategies and the actual code/function on how bots work.

Because of this I HIGHLY RECOMMEND this NOT be used as it really is quite ineffective, but I am not dissapointed as this is my first project!

The main reason this algorithm is quite ineffective is because first, the fees are taking an atrocius amount of the starting balance (Starting Balance in all cases: $100,000, Fees in all cases: $30,000+). This is because the algorithm isn't really that effective, as it uses daily history requests instead of the rolling door method. Overall the bots code was also quite poor, as it had ≈ 40% win rate, with the wins being worth less in comparison to the losses. The bot would also end up just going on long win or loss streaks, which lead to a great amount of capital being burnt.  

There are someways these could be fixed easily, for example when shorting the stock 
"else:
            self.SetHoldings(self.symbol, -0.5)"

set the risk amount for shorting to a much lower amount, such as .1, so losses aren't that major. 


Overall great first project, just being able to learn about this and gain experience was great, even if the bot didn't work as well as I would have liked, this was a great learning experience and taught me much about algorithmic trading, 