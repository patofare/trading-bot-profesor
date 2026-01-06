def calculate_volume_indicators(df, window=20):
    df["VOL_MA"] = df["Volume"].rolling(window).mean()
    df["VOL_RATIO"] = df["Volume"] / df["VOL_MA"]
    return df