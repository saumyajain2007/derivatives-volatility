import pandas as pd
import yfinance as yf

def load_price(symbol, start=None, end=None):
    df = yf.download(symbol, start=start, end=end, progress=False)
    return df

def load_option_chain_csv(path):
    return pd.read_csv(path)