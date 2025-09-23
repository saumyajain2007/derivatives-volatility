# Example showing a simple calibration on synthetic market prices
from src.heston import calibrate_heston, heston_price
import numpy as np

def generate_synthetic_market(S0, r, q, true_params, strikes, T):
    kappa, theta, sigma, rho, v0 = true_params
    market = []
    for K in strikes:
        p = heston_price(S0, K, T, r, q, kappa, theta, sigma, rho, v0)
        market.append({'strike': K, 'T': T, 'option_type': 'call', 'market_price': p})
    return market

def main():
    S0 = 100.0
    r = 0.01
    q = 0.0
    true_params = (1.5, 0.04, 0.4, -0.5, 0.04)
    strikes = [80,90,100,110,120]
    T = 30/252
    market = generate_synthetic_market(S0, r, q, true_params, strikes, T)
    init = (2.0, 0.02, 0.3, -0.3, 0.02)
    res = calibrate_heston(market, S0, r, q, init)
    print('Calibration result:\n', res)

if __name__ == '__main__':
    main()