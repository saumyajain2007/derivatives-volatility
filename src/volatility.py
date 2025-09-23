import numpy as np
import pandas as pd
from .black_scholes import implied_vol, bs_price

def historical_volatility(prices, window=21, periods_per_year=252):
    logret = np.log(prices).diff().dropna()
    hv = logret.rolling(window).std() * np.sqrt(periods_per_year)
    return hv

def realized_volatility(returns, window=21, periods_per_year=252):
    rv = returns.pow(2).rolling(window).sum().apply(lambda x: np.sqrt(x * (periods_per_year / window)))
    return rv

def implied_vol_surface(option_df, S, r, q):
    vols = []
    for _, row in option_df.iterrows():
        vol = implied_vol(row['mid_price'], S, row['strike'], row['T'], r, q, row.get('option_type','call'))
        vols.append(vol)
    option_df = option_df.copy()
    option_df['implied_vol'] = vols
    return option_df