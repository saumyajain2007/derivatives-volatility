from src.black_scholes import bs_price, implied_vol
from src.heston import heston_price, calibrate_heston
from src.volatility import historical_volatility
from src.utils import load_price
import numpy as np

def main():
    S = 150.0
    K = 160.0
    T = 30/252
    r = 0.02
    q = 0.0
    sigma = 0.25
    print('BS call price:', bs_price(S,K,T,r,q,sigma,'call'))
    kappa, theta, sigma_h, rho, v0 = 2.0, 0.04, 0.3, -0.6, 0.04
    print('Heston call price:', heston_price(S,K,T,r,q,kappa,theta,sigma_h,rho,v0,'call'))
    # load price history and compute hv (requires internet)
    # df = load_price('AAPL', start='2020-01-01', end='2024-12-31')
    # print(historical_volatility(df['Adj Close']).tail())

if __name__ == '__main__':
    main()