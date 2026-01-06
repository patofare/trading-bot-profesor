import pandas as pd

def calculate_sma(df, window):
    df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean() ##CALCULA MEDIA MOVIL SIMPLE
    return df

def calculate_ema(df, window):
    df[f"EMA_{window}"] = df["Close"].ewm(span=window, adjust=False).mean() ##CALCULA MEDIA MOVIL EXPONENCIAL
    return df