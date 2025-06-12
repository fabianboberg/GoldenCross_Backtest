import yfinance as yf

def get_aapl_stockdata(ticker='AAPL', start="2010-01-01"):
    #Fetches apple stock data from 2010-01-01 to today, format is pandas.DataFrame
    stock_data = yf.download(ticker, start)
    return stock_data
