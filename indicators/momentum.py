import pandas as pd

def calculate_rsi(df, window=14):
    delta = df["Close"].diff()

    gains = delta.where(delta > 0, 0.0)
    losses = -delta.where(delta < 0, 0.0)

    avg_gain = gains.rolling(window=window).mean()
    avg_loss = losses.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    df[f"RSI_{window}"] = rsi
    return df