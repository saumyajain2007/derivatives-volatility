📊 **Derivatives & Volatility Analysis**
This repository implements option pricing models (Black–Scholes and Heston), volatility analysis tools, and calibration routines. It serves as both a learning resource and a practical toolkit for quantitative finance enthusiasts, traders, and researchers.

🔎 **Project Overview**
Options are derivative instruments whose value depends on an underlying asset (e.g., stock, index, commodity). Their pricing critically depends on volatility — a measure of uncertainty in asset returns.

This repository provides:

**Option Pricing Models**
Black–Scholes–Merton (BSM) model

**Heston stochastic volatility model**

Volatility Analysis
Historical volatility estimation

Implied volatility extraction

Calibration
A simple example of calibrating the Heston model to market data

Interactive Workflows
Jupyter notebooks for experimentation and visualization

📚 Theoretical Background
1. Black–Scholes Model
The Black–Scholes–Merton model (1973) assumes:

Asset prices follow geometric Brownian motion (GBM):

dS_t=μS_tdt+σS_tdW_t
$$$$where:

S 
t
​
  = asset price at time t

μ = drift (expected return)

σ = volatility

W 
t
​
  = Wiener process (Brownian motion)

European call option price under risk-neutral measure:

C(S,t)=S_tN(d_1)−Ke 
−r(T−t)
 N(d_2)
$$$$with:

d_1= 
σ 
T−t
​
 
ln( 
K
S_t
​
 )+(r+ 
2
σ 
2
 
​
 )(T−t)
​
 ,d_2=d_1−σ 
T−t
​
 
$$$$where N(⋅) is the standard normal CDF.

2. Heston Model
The Heston model (1993) extends Black–Scholes by allowing volatility itself to follow a stochastic process:

Asset price process:

dS_t=μS_tdt+ 
v_t
​
 S_tdW_t 
S
 
$$$$

Variance process (Ornstein–Uhlenbeck type):

dv_t=κ(θ−v_t)dt+ξ 
v_t
​
 dW_t 
v
 
$$$$

Correlation:

dW_t 
S
 dW_t 
v
 =ρdt
$$$$
$$Parameters:

v 
t
​
 : instantaneous variance

κ: mean reversion speed

θ: long-term variance

ξ: volatility of variance ("vol of vol")

ρ: correlation between asset and variance shocks

The model captures volatility clustering, smiles/skews in implied volatility, and is widely used in practice.

3. Volatility Concepts
Historical Volatility (HV): Estimated from past returns:

σ_hist= 
252
​
 ⋅StdDev(ln 
S_t−1
S_t
​
 )
$$$$

Implied Volatility (IV): The volatility parameter that, when plugged into the Black–Scholes formula, matches the observed option market price.

Market Price=BS(S,K,r,T,σ_impl)
$$$$IV reflects market expectations of future uncertainty.

4. Calibration
Calibrating models like Heston means finding parameters (κ,θ,ξ,ρ,v 
0
​
 ) that minimize the difference between model prices and observed market prices.

Typical optimization target:

min_Θ∑_i=1 
N
 (C_model(K_i,T_i;Θ)−C_market(K_i,T_i)) 
2
 
$$$$where Θ is the parameter set.

📂 Repository Structure
Derivatives-Volatility-Analysis/
│── src/                # Model implementations and utilities
│── notebooks/          # Jupyter notebooks for analysis
│   └── analysis.ipynb
│── examples/           # Example scripts for pricing & calibration
│   └── price_examples.py
│── tests/              # Unit tests (pytest)
│── requirements.txt    # Dependencies
└── README.md           # Project documentation


🚀 Quickstart
1. Setup Environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate      # Windows
pip install -r requirements.txt


2. Run Example Script
python examples/price_examples.py


3. Launch Jupyter Notebook
jupyter lab notebooks/analysis.ipynb


✅ Features
Black–Scholes pricing for European options

Implied volatility calculation via numerical root-finding

Historical volatility from market data

Heston pricing using characteristic functions & Fourier inversion

Simple Heston calibration example

Interactive notebook visualization

🧪 Testing
Run unit tests with:

pytest tests/


📈 Future Enhancements
Local volatility model implementation

Advanced Heston calibration (global + local optimization)

Monte Carlo simulation for path-dependent options

Volatility surface construction and visualization

📖 References
Black, F., & Scholes, M. (1973). The Pricing of Options and Corporate Liabilities.

Heston, S. (1993). A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options.

Gatheral, J. (2006). The Volatility Surface.
