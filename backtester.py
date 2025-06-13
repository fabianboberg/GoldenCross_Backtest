import pandas as pd

def backtest(result, initial_cash = 10000):
    #Variable initialization golden cross
    cash = float(initial_cash)
    shares = 0
    equity_curve = [initial_cash]
    position = None

    #Variable initialization hold strategi
    cash_hodl = float(initial_cash)
    equity_hodl = [initial_cash]

    #Comparison of just holding stocks
    shares_hodl = int(initial_cash // result['Close'].values[0])
    cash_hodl -= shares_hodl * result['Close'].values[0]

    #Daily price and SMA
    for i in range(1, len(result)):
        price = result['Close'].values[i]
        sma50 = result['SMA50'].values[i]
        sma200 = result['SMA200'].values[i]

        #Required as SMA50 and SMA200 returns NaN for the first 50 and 200 days respectively
        if pd.notna(sma50) and pd.notna(sma200):
            if sma50 > sma200:
                current_signal = 'Buy'
            else:
                current_signal = 'Sell'


            #Only act when signal changes
            if not current_signal == position:
                if current_signal == 'Buy' and shares == 0:
                    shares = int(cash // price)
                    cash -= shares * price

                elif current_signal == 'Sell' and shares > 0:
                    cash += shares * price
                    shares = 0

                position = current_signal

        #Calculate current equity
        equity_curve.append(cash + shares*price)
        equity_hodl.append(cash_hodl + shares_hodl*price)

    result['Equity'] = equity_curve
    result['Equity_HODL'] = equity_hodl

    return result
