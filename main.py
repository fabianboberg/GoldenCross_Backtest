from FetchStockData import get_stockdata
from SMA_Cross import sma_cross
from backtester import backtest
from visual import *
from helperfunctions import *
from backtest_types import BacktestResult


ticker, user_start_date, end_date = user_input()

adjusted_start_date = adjust_start_date(user_start_date)

stock_data = get_stockdata(ticker, adjusted_start_date, end_date)
result = sma_cross(stock_data)
result_trimmed = datatrimmer(result)


reslut_rightdate = result_trimmed[result_trimmed.index >= user_start_date].copy()

data_backtested = backtest(reslut_rightdate)

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