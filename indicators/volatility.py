def calculate_atr(df, period=14):
    high = df["High"]
    low = df["Low"]
    close = df["Close"]

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    true_range = tr1.combine(tr2, max).combine(tr3, max)
    df["ATR"] = true_range.rolling(period).mean()

    return df