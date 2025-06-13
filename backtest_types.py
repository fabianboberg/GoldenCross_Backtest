from dataclasses import dataclass
import pandas as pd

@dataclass
class BacktestResult:
    data: pd.DataFrame
    cagr: float
    cagr_hodl: float
    volatility: float
    volatility_hodl: float
    sharpe: float
    sharpe_hodl: float