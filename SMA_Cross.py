def sma_cross(stock_data, short_window = 50, long_window = 200):
    data = stock_data.copy()
    data["SMA50"] = data['Close'].rolling(window=short_window).mean()
    data["SMA200"] = data['Close'].rolling(window=long_window).mean()
    return data

