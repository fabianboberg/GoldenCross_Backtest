import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#Function to cut out the first 200 days when SMA200 is unable to respond
def datatrimmer(result):

    #Find first actionable day
    first_valid_day = None
    for i in range(1, len(result)):
        if pd.notna(result['SMA50'].values[i]) and pd.notna(result['SMA200'].values[i]):
            first_valid_day = i
            break

    if first_valid_day is None:
        raise ValueError("Time frame is too short and no valid data could be found")

     # Trimmed result data
    result_trimmed = result.iloc[first_valid_day:].copy()

    return result_trimmed

#Calculate the average CAGR of the period
def cagrcalc(result):
    start_date = result.index[0]
    end_date = result.index[-1]

    start_value = result['Equity'].values[0]
    end_value = result['Equity'].values[-1]
    end_valuehodl = result['Equity_HODL'].values[-1]

    #For more flexibility when feeding dates
    if hasattr(start_date, 'year'):
        years = (end_date - start_date).days / 365.25
    else:
        years = (end_date - start_date) / 365.25

    #Standard CAGR equation
    cagr = float((end_value / start_value) ** (1 / years) - 1) * 100
    cagr_hodl = float((end_valuehodl / start_value) ** (1 / years) - 1) * 100
    return cagr, cagr_hodl

#Calculate average annual volatiltiy over the entire period
def calculate_volatility(result):
    equity = result['Equity'].apply(lambda x: x[0] if isinstance(x, (np.ndarray, list)) else x)
    equity_hodl = result['Equity_HODL'].apply(lambda x: x[0] if isinstance(x, (np.ndarray, list)) else x)

    #Fix deprecated warning
    daily_returns_hodl = equity_hodl.pct_change(fill_method=None).dropna()
    daily_returns = equity.pct_change(fill_method=None).dropna()

    daily_vol_hodl = daily_returns_hodl.std()
    annual_volatility_hodl = daily_vol_hodl * np.sqrt(252)
    daily_vol = daily_returns.std()
    annual_volatility = daily_vol * np.sqrt(252)


    return annual_volatility, annual_volatility_hodl

#Calculate the sharpe ratio
def sharpe_ratio(cagr, cagr_hodl, annual_volatility, annual_volatility_hodl):

    risk_free_rate = 0.03

    cagr = cagr/100
    cagr_hodl = cagr_hodl/100

    sharpe = (cagr - risk_free_rate) / annual_volatility
    sharpe_hodl = (cagr_hodl - risk_free_rate) / annual_volatility_hodl

    return sharpe, sharpe_hodl

#Collect the input from the user
def user_input():
    ticker = input('Enter stock ticker symbol (AAPL, GOOGL, MSFT): ').upper().strip()

    user_start_date = input('Enter start date (YYYY-MM-DD) or press enter for 2010-01-01: ').strip()
    if not user_start_date:
        user_start_date = '2010-01-01'

    end_date = input('Enter end date (YYYY-MM-DD) or press enter for today: ').strip()
    if not end_date:
        end_date = None

    return ticker, user_start_date, end_date

#Function to ensure sufficient historical data is retrieved before the user-specified start date,
#allowing the SMA calculation to return valid values for the entire selected period.
def adjust_start_date(user_start_date):
    #Number of days calculated before user input date
    calculation_margin = 365

    start_dt = datetime.strptime(user_start_date, '%Y-%m-%d')
    adjusted_start_date = (start_dt - timedelta(days=calculation_margin)).strftime('%Y-%m-%d')
    return adjusted_start_date
