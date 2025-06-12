def sma_cross(stock_data, short_window = 50, long_window = 200):
    data = stock_data.copy() #Create a copy of the stock data
    data["SMA50"] = data['Close'].rolling(window=short_window).mean() #Create simple moving average, shorter time frame
    data["SMA200"] = data['Close'].rolling(window=long_window).mean() #Longer time frame
    return data