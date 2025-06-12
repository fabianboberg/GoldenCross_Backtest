import pandas as pd

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

#Calculate CAGR
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
