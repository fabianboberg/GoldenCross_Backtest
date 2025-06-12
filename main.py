#The purpose of this backtest is to increase my proficiency in git, python
# and common financial strategies, more specifically golden cross

from FetchCloseDataAAPL import get_aapl_stockdata
from SMA_Cross import sma_cross
from backtester import backtest
from visual import *

stock_data = get_aapl_stockdata()
result = sma_cross(stock_data)

backtest(result)

stockplotter(result)
equityplotter(result)