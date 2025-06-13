import matplotlib.pyplot as plt
from backtest_types import BacktestResult


def stockplotter(result: BacktestResult):
    #Fetch necessary data
    df = result.data
    date = df.index
    sma50 = df['SMA50']
    sma200 = df['SMA200']
    close = df['Close']

    #Increase resolution for readability
    plt.figure(figsize=(12, 6), dpi=300)
    plt.title("Stock Price and moving averages against date")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")

    plt.plot(date, sma50, label="SMA50")
    plt.plot(date, sma200, label="SMA200")
    plt.plot(date, close, label="Stock Price")

    plt.legend()
    plt.show()

def equityplotter(result: BacktestResult):
    #Fetch necessary data
    df = result.data
    equity = df['Equity']
    equity_hodl = df['Equity_HODL']
    date = df.index

    plt.figure(figsize=(12, 6), dpi=100)
    plt.title("Equity growth with golden cross method")
    plt.xlabel("Date")
    plt.ylabel("Equity")

    plt.plot(
        date, equity,
        label=f"Equity - Golden cross method "
              f"(CAGR: {result.cagr:.1f}%) "
              f"(Volatility: {result.volatility:.2%}) "
              f"(Sharpe: {result.sharpe:.2f})")

    plt.plot(
        date, equity_hodl,
             label=f"Equity - Holding stocks "
                   f"(CAGR: {result.cagr_hodl:.1f}%) "
                   f"(Volatility: {result.volatility_hodl:.2%}) "
                   f"(Sharpe: {result.sharpe_hodl:.2f})")

    plt.legend()
    plt.show()

