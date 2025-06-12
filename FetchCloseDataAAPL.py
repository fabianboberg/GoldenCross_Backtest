import yfinance as yf

def get_aapl_stockdata(ticker='AAPL', start="2010-01-01"):
    stock_data = yf.download(ticker, start) #Fetches apple stock data from 2010-01-01 to today, format is pandas.DataFrame
    return stock_data

