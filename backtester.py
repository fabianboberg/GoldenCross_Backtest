import pandas as pd

def backtest(result, initial_cash = 10000):
    cash = float(initial_cash)
    shares = 0
    equity_curve = [initial_cash]
    position = None

    for i in range(1, len(result)):
        price = result['Close'].values[i]
        sma50 = result['SMA50'].values[i]
        sma200 = result['SMA200'].values[i]

        if pd.notna(sma50) and pd.notna(sma200):
            if sma50 > sma200:
                current_signal = 'Buy'
            else:
                current_signal = 'Sell'


            if not current_signal == position:
                if current_signal == 'Buy' and shares == 0:
                    shares = int(cash // price)
                    cash -= shares * price

                elif current_signal == 'Sell' and shares > 0:
                    cash += shares * price
                    shares = 0


        equity_curve.append(cash + shares*price)

    result['Equity'] = equity_curve

    return result