import matplotlib.pyplot as plt

def plot_price_with_signals(df, ticker, signal, score):
    fig, (ax_price, ax_rsi) = plt.subplots(
        2,
        1,
        figsize=(14, 8),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1]}
    )

    # ====== GRÁFICO DE PRECIO ======
    ax_price.plot(df["Date"], df["Close"], label="Precio de cierre")

    if "EMA_20" in df.columns:
        ax_price.plot(df["Date"], df["EMA_20"], label="EMA 20")

    if "EMA_50" in df.columns:
        ax_price.plot(df["Date"], df["EMA_50"], label="EMA 50")

    # Color según fuerza de señal
    if score >= 3:
        color = "darkgreen"
        signal = "BUY FUERTE"
    elif score == 2:
        color = "green"
        signal = "BUY"
    elif score <= -3:
        color = "darkred"
        signal = "SELL FUERTE"
    elif score == -2:
        color = "red"
        signal = "SELL"
    else:
        color = "gray"
        signal = "HOLD"

    # Señal actual
    last = df.iloc[-1]
    ax_price.scatter(
        last["Date"],
        last["Close"],
        color=color,
        s=180,
        zorder=5
    )

    ax_price.set_title(
    f"{ticker} — Señal actual: {signal} (score {score})"
    )


    ax_price.set_ylabel("Precio")
    ax_price.legend()
    ax_price.grid(True)

    # ====== GRÁFICO RSI ======
    ax_rsi.plot(df["Date"], df["RSI_14"], label="RSI 14")
    ax_rsi.axhline(70, linestyle="--", linewidth=1)
    ax_rsi.axhline(30, linestyle="--", linewidth=1)

    ax_rsi.set_ylabel("RSI")
    ax_rsi.set_xlabel("Fecha")
    ax_rsi.legend()
    ax_rsi.grid(True)

    plt.tight_layout()
    plt.show()