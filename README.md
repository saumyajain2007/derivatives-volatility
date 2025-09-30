# 📊 Derivatives & Volatility Analysis  
This repository implements option pricing models (Black–Scholes and Heston), volatility analysis tools, and calibration routines. It serves as both a learning resource and a practical toolkit for quantitative finance enthusiasts, traders, and researchers.

## 🔎 Project Overview  

Options are derivative instruments whose value depends on an underlying asset (e.g., stock, index, commodity). Their pricing critically depends on volatility — a measure of uncertainty in asset returns.

This repository provides:  
- **Option Pricing Models**  
  - Black–Scholes–Merton (BSM) model  
  - Heston stochastic volatility model  
- **Volatility Analysis**  
  - Historical volatility estimation  
  - Implied volatility extraction  
- **Calibration**  
  - A simple example of calibrating the Heston model to market data  
- **Interactive Workflows**  
  - Jupyter notebooks for experimentation and visualization
 ---

## 📚 Theoretical Background

### 1. Black–Scholes Model

The **Black–Scholes–Merton model** (1973) assumes:  
- Asset prices follow **geometric Brownian motion (GBM)**:  

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

where:  
- $S_t$ = asset price at time $t$  
- $\mu$ = drift (expected return)  
- $\sigma$ = volatility  
- $W_t$ = Wiener process (Brownian motion)  

European call option price under risk-neutral measure:

$$
C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)
$$

with:  

$$
d_1 = \frac{\ln \left(\frac{S_t}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)(T-t)}{\sigma \sqrt{T-t}}, \quad
d_2 = d_1 - \sigma \sqrt{T-t}
$$

where $N(\cdot)$ is the standard normal CDF.

---

### 2. Heston Model

The **Heston model** (1993) extends Black–Scholes by allowing volatility itself to follow a stochastic process:

$$
dS_t = \mu S_t \, dt + \sqrt{v_t} S_t \, dW_t^S
$$

$$
dv_t = \kappa (\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^v
$$

with correlation:

$$
dW_t^S \, dW_t^v = \rho \, dt
$$

Parameters:  
- $v_t$: instantaneous variance  
- $\kappa$: mean reversion speed  
- $\theta$: long-term variance  
- $\xi$: volatility of variance ("vol of vol")  
- $\rho$: correlation between asset and variance shocks

---

### 3. Volatility Concepts

- **Historical Volatility (HV):**  

$$
\sigma_{hist} = \sqrt{252} \cdot \text{StdDev} \left( \ln \frac{S_t}{S_{t-1}} \right)
$$

- **Implied Volatility (IV):**  

$$
\text{Market Price} = BS(S, K, r, T, \sigma_{impl})
$$

IV reflects market expectations of future uncertainty.

---

### 4. Calibration

Calibrating models like Heston means finding parameters $(\kappa, \theta, \xi, \rho, v_0)$ that minimize the difference between model prices and observed market prices:

$$
\min_{\Theta} \sum_{i=1}^N \left( C_{model}(K_i, T_i; \Theta) - C_{market}(K_i, T_i) \right)^2
$$

---
.
├── LICENSE
├── README.md
├── examples
│   ├── calibrate_heston.py
│   └── price_examples.py
├── notebooks
│   └── analysis.ipynb
├── requirements.txt
├── src
│   ├── black_scholes.py
│   ├── heston.py
│   ├── utils.py
│   └── volatility.py
└── tests
    └── test_models.py
