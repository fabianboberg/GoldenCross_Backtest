import matplotlib.pyplot as plt

def stockplotter(result):
    #Fetch necessary data
    sma50 = result['SMA50']
    sma200 = result['SMA200']
    close = result['Close']
    date = result.index

    #Increase resolution for readability
    plt.figure(figsize=(12, 6), dpi=300)

    plt.xlabel("Date")
    plt.ylabel("Stock Price")

    plt.title("Stock Price and moving averages against date")

    plt.plot(date, sma50, label="SMA50")
    plt.plot(date, sma200, label="SMA200")
    plt.plot(date, close, label="Close Price")

    plt.legend()

    plt.show()

def equityplotter(result):
    #Fetch necessary data
    equity = result['Equity']
    date = result.index

    plt.figure(figsize=(12, 6), dpi=100)

    plt.xlabel("Date")
    plt.ylabel("Stock Price")

    plt.title("Equity growth with golden cross method")

    plt.plot(date, equity, label="Equity")

    plt.legend()

    plt.show()

