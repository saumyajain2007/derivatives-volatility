import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

# Compact Heston characteristic function and price (educational - not production optimized)
def _heston_cf(phi, S0, T, r, q, kappa, theta, sigma, rho, v0, Pnum):
    i = 1j
    x = np.log(S0)
    a = kappa * theta
    # choose u and b depending on P1/P2 (Heston's original formulation)
    if Pnum == 1:
        u = 0.5
        b = kappa - rho * sigma
    else:
        u = -0.5
        b = kappa
    # parameters per homog formulation
    d = np.sqrt((rho*sigma*i*phi - b)**2 - sigma**2 * (2*u*i*phi - phi**2))
    g = (b - rho*sigma*i*phi - d) / (b - rho*sigma*i*phi + d)
    exp_dt = np.exp(-d * T)
    C = (r - q) * i * phi * T + (a / sigma**2) * ( (b - rho*sigma*i*phi - d) * T - 2.0 * np.log((1 - g*exp_dt)/(1 - g)) )
    D = ((b - rho*sigma*i*phi - d) / sigma**2) * (1 - exp_dt) / (1 - g*exp_dt)
    cf = np.exp(C + D * v0 + i * phi * x)
    return cf

def heston_price(S0, K, T, r, q, kappa, theta, sigma, rho, v0, option_type='call'):
    i = 1j
    def integrand(phi, Pnum):
        cf = _heston_cf(phi - i*0.0001, S0, T, r, q, kappa, theta, sigma, rho, v0, Pnum)
        numerator = np.exp(-i*phi*np.log(K)) * cf
        return (numerator / (i*phi)).real
    # Integrate to get probabilities
    limit = 200.0
    P1 = 0.5 + (1.0/np.pi) * quad(lambda x: integrand(x, 1), 0.0, limit, limit=200)[0]
    P2 = 0.5 + (1.0/np.pi) * quad(lambda x: integrand(x, 2), 0.0, limit, limit=200)[0]
    discountedK = K * np.exp(-r*T)
    if option_type == 'call':
        return np.exp(-q*T)*S0*P1 - discountedK*P2
    else:
        call = np.exp(-q*T)*S0*P1 - discountedK*P2
        put = call - np.exp(-q*T)*S0 + discountedK
        return put

def calibrate_heston(market_data, S0, r, q, initial_params):
    def loss(params):
        kappa, theta, sigma, rho, v0 = params
        err = 0.0
        for d in market_data:
            model_p = heston_price(S0, d['strike'], d['T'], r, q, kappa, theta, sigma, rho, v0, d.get('option_type','call'))
            err += (model_p - d['market_price'])**2
        return err
    bounds = [(1e-6, 10), (1e-6, 2), (1e-6, 5), (-0.99, 0.99), (1e-6, 2)]
    res = minimize(loss, initial_params, bounds=bounds, method='L-BFGS-B')
    return res