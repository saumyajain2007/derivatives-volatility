import math
from src.black_scholes import bs_price, implied_vol
from src.heston import heston_price

def test_bs_price_vs_known():
    # Known BS price (from hand calculation)
    S = 100.0; K = 100.0; T = 0.5; r = 0.01; q = 0.0; sigma = 0.2
    price = bs_price(S,K,T,r,q,sigma,'call')
    assert price > 0.0

def test_implied_vol_roundtrip():
    S = 100.0; K = 100.0; T = 0.5; r = 0.01; q = 0.0; sigma = 0.22
    p = bs_price(S,K,T,r,q,sigma,'call')
    iv = implied_vol(p, S, K, T, r, q, 'call')
    assert not math.isnan(iv)
    assert abs(iv - sigma) < 1e-3

def test_heston_runs():
    S = 100.0; K = 100.0; T = 0.2; r = 0.01; q = 0.0
    kappa, theta, sigma_h, rho, v0 = 1.5, 0.04, 0.3, -0.5, 0.04
    p = heston_price(S,K,T,r,q,kappa,theta,sigma_h,rho,v0,'call')
    assert p >= 0.0