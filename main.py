from FetchStockData import get_aapl_stockdata
from SMA_Cross import sma_cross
from backtester import backtest
from visual import *
from helperfunctions import *
from backtest_types import BacktestResult

stock_data = get_aapl_stockdata()
result = sma_cross(stock_data)
result_trimmed = datatrimmer(result)

data_backtested = backtest(result_trimmed)

cagr, cagr_hodl = cagrcalc(data_backtested)
annual_volatility, annual_volatility_hodl = calculate_volatility(data_backtested)
sharpe, sharpe_hodl = sharpe_ratio(cagr, cagr_hodl,annual_volatility, annual_volatility_hodl)

final_result = BacktestResult(
    data = data_backtested,
    cagr = cagr,
    cagr_hodl = cagr_hodl,
    volatility = annual_volatility,
    volatility_hodl = annual_volatility_hodl,
    sharpe = sharpe,
    sharpe_hodl = sharpe_hodl
)


stockplotter(final_result)
equityplotter(final_result)