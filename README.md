# Derivatives & Volatility Analysis

This repository implements Black–Scholes and Heston option pricing models, tools for historical and implied volatility calculation, a simple Heston calibration example, and tests/notebooks for exploration.

## Contents
- `src/` : model implementations and utilities
- `notebooks/analysis.ipynb` : interactive notebook demonstrating workflows
- `examples/` : example scripts for pricing and calibration
- `tests/` : pytest unit tests

## Quickstart
1. Create virtualenv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   pip install -r requirements.txt
   ```
2. Run the example script:
   ```bash
   python examples/price_examples.py
   ```
3. Launch the notebook:
   ```bash
   jupyter lab notebooks/analysis.ipynb
   ```