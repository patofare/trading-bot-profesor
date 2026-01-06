def generate_signal(df):
    last = df.iloc[-1]
    score = 0
    reasons = []

    # Tendencia

    if last["Close"] > last["EMA_20"]:
        score += 1
        reasons.append("El precio está por encima de la EMA 20")
    else:
        score -= 1
        reasons.append("El precio está por debajo de la EMA 20")

    if last["EMA_20"] > last["EMA_50"]:
        score += 1
        reasons.append("La EMA 20 está por encima de la EMA 50")
    else:
        score -= 1
        reasons.append("La EMA 20 está por debajo de la EMA 50")

    # RSI como CONTEXTO, no como gatillo
    
    if last["RSI_14"] < 30:
        score += 0.5
        reasons.append("RSI en sobreventa, posible rebote")

    elif last["RSI_14"] > 70:
        score -= 0.5
        reasons.append("RSI en sobrecompra, posible corrección")

    # Volumen

    if last["VOL_RATIO"] > 1.2:
        score += 1
        reasons.append("Volumen superior al promedio, confirma el movimiento")
    elif last["VOL_RATIO"] < 0.8:
        score -= 1
        reasons.append("Volumen bajo, la señal pierde fuerza")

    # ATR

    atr = last["ATR"]
    price = last["Close"]
    atr_pct = atr / price

    if atr_pct > 0.04:
        score -= 1
        reasons.append("Alta volatilidad (ATR elevado), riesgo aumentado")

    elif atr_pct < 0.015:
        score += 0.5
        reasons.append("Baja volatilidad, movimiento más estable")

    if score >= 3:
        signal = "BUY FUERTE"
    elif score == 2:
        signal = "BUY"
    elif score == -2:
        signal = "SELL"
    elif score <= -3:
        signal = "SELL FUERTE"
    else:
        signal = "HOLD"

    return signal, score, reasons
