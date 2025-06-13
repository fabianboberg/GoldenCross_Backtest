import yfinance as yf

def get_stockdata(ticker, start_date, end_date):
    #Fetches apple stock data from requested dates, format is pandas.DataFrame
    stock_data = yf.download(ticker, start_date, end_date)
    return stock_data
