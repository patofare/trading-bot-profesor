def explain_rsi(rsi_value):
    """
    Devuelve explicación del RSI
    """

    if rsi_value < 30:
        return (
            f"RSI en {rsi_value:.2f}. "
            "El activo se encuentra en zona de sobreventa, "
            "o sea que el precio cayó muy rápido últimamente.(empieza a caer y todos se desesperan por vender) "
            "Se podría anticipar un posible rebote, aunque no es una señal de compra confirmada."
        )

    elif rsi_value > 70:
        return (
            f"RSI en {rsi_value:.2f}. "
            "El activo se encuentra en zona de sobrecompra, "
            "lo que nos dice que el precio ha subido con fuerza rápidamente.(empieza a subir y todos pagan lo que sea por comprar) "
            "Podría producirse una corrección."
        )

    else:
        return (
            f"RSI en {rsi_value:.2f}. "
            "El indicador se encuentra en zona neutral, "
            "sin señales claras de sobrecompra ni sobreventa."
        )
    
def explain_signal(signal, score, reasons):
    """
    Explica la señal generada por el sistema
    """

    base = f"La señal generada por el sistema es {signal} con un score de {score}. "

    if signal == "BUY FUERTE":
        base += (
            "La tendencia es claramente alcista y los indicadores técnicos "
            "confirman fortaleza en el movimiento."
        )

    elif signal == "BUY":
        base += (
            "Se observa una señal de compra moderada, con algunos indicadores "
            "acompañando el movimiento, aunque sin confirmación total."
        )

    elif signal == "SELL FUERTE":
        base += (
            "La presión vendedora es fuerte y los indicadores muestran debilidad "
            "en el precio."
        )

    elif signal == "SELL":
        base += (
            "Se detecta una señal de venta moderada, con pérdida parcial de fuerza "
            "en la tendencia actual."
        )

    else:  # HOLD
        base += (
            "El mercado se encuentra indeciso y no presenta una oportunidad clara "
            "en este momento."
        )

    return base

