def generate_signal(df):
    last = df.iloc[-1]
    price = last["Close"]
    ema20 = last["EMA_20"]
    dist_ema20 = abs(price - ema20) / ema20
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

    # Timing para entrar

    if dist_ema20 > 0.03:
        score -= 1
        reasons.append(
            "El precio está extendido respecto a la EMA 20, se recomienda esperar un pullback")
    elif 0.005 <= dist_ema20 <= 0.015:
        score += 0.5
        reasons.append(
            "El precio se encuentra cerca de la EMA 20, zona favorable de entrada")

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
    atr_pct = atr / price

    if atr_pct > 0.04:
        score -= 1
        reasons.append("Alta volatilidad (ATR elevado), riesgo aumentado")

    elif atr_pct < 0.015:
        score += 0.5
        reasons.append("Baja volatilidad, movimiento más estable")

    if score >= 3:
        signal = "BUY FUERTE"
    elif score >= 2:
        signal = "BUY"
    elif score <= -3:
        signal = "SELL FUERTE"
    elif score <= -2:
        signal = "SELL"
    else:
        signal = "HOLD"


    return signal, score, reasons
