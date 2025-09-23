import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

def bs_price(S, K, T, r, q, sigma, option_type='call'):
    if T <= 0:
        if option_type == 'call':
            return max(S - K, 0.0)
        else:
            return max(K - S, 0.0)
    sqrtT = np.sqrt(T)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    if option_type == 'call':
        price = np.exp(-q*T)*S*norm.cdf(d1) - np.exp(-r*T)*K*norm.cdf(d2)
    else:
        price = np.exp(-r*T)*K*norm.cdf(-d2) - np.exp(-q*T)*S*norm.cdf(-d1)
    return price

def implied_vol(price, S, K, T, r, q, option_type='call', tol=1e-6, maxiter=100):
    def objective(vol):
        return bs_price(S, K, T, r, q, vol, option_type) - price
    try:
        vol = brentq(objective, 1e-8, 5.0, xtol=tol, maxiter=maxiter)
        return vol
    except ValueError:
        return float('nan')