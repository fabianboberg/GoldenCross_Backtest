from FetchStockData import get_aapl_stockdata
from SMA_Cross import sma_cross
from backtester import backtest
from visual import *
from helperfunctions import *

stock_data = get_aapl_stockdata()
result = sma_cross(stock_data)
result_trimmed = datatrimmer(result)

new_result_trimmed = backtest(result_trimmed)
cagr, cagr_hodl = cagrcalc(result_trimmed)

stockplotter(new_result_trimmed)
equityplotter(new_result_trimmed, cagr, cagr_hodl)