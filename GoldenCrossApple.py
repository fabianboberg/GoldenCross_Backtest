#The purpose of this backtest is to increase my proficiency in git, python and common financial strategies, more specifically golden cross
import yfinance as yf

raw_apple_stock_data = yf.download('AAPL', start='2010-01-01') #Fetches apple stockdata from 2010-01-01 to today, format is pandas.DataFrame
close_data = raw_apple_stock_data['Close'] #Takes out closing price for each day
