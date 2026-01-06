from utils.data_loader import load_stock_data
from indicators.trend import calculate_ema
from indicators.momentum import calculate_rsi
from indicators.volume import calculate_volume_indicators
from signals.rules import generate_signal
from signals.explanations import explain_signal, explain_rsi
from indicators.volatility import calculate_atr


def run_analysis(ticker):
    print("\n Iniciando análisis técnico educativo")
    print(f"Activo seleccionado: {ticker}")

    try:
        print("\n Cargando datos históricos del mercado...")
        df = load_stock_data(ticker, period="2y")
        print(f"   ✔ {len(df)} registros cargados")

        print("\n Calculando medias móviles (EMA 20 y EMA 50)...")
        df = calculate_ema(df, 20)
        df = calculate_ema(df, 50)
        print("   ✔ Medias móviles calculadas")

        print("\n Calculando RSI (14 períodos)...")
        df = calculate_rsi(df)
        print("   ✔ RSI calculado")

        print("\n Calculando ATR (volatilidad)...")
        df = calculate_atr(df)
        print("   ✔ ATR calculado")

        print("\n Calculando indicadores de volumen...")
        df = calculate_volume_indicators(df)
        print("   ✔ Volumen relativo calculado")

        print("\n Evaluando reglas de trading...")
        signal, score, reasons = generate_signal(df)
        df["Signal"] = "HOLD"
        df.loc[df.index[-1], "Signal"] = signal

        last = df.iloc[-1]

        price = last["Close"]
        atr = last["ATR"]
        stop_loss = price - 1.5 * atr
        take_profit = price + 3 * atr

        risk_atr = 1.5
        reward_atr = 3

        print("\n Gestión de riesgo sugerida:")
        print(f" - Precio actual: {price:.2f}")
        print(f" - Stop Loss (ATR): {stop_loss:.2f}")
        print(f" - Take Profit (ATR): {take_profit:.2f}")
        print(f" - Relación riesgo/beneficio: 1:{reward_atr / risk_atr:.1f}")

        explanation = explain_signal(signal, score, reasons)
        rsi_explanation = explain_rsi(last["RSI_14"])


        return df, signal, score, reasons, explanation, rsi_explanation, stop_loss, take_profit

    except Exception as e:
        print("\n Error durante el análisis educativo")
        print("Detalle:", e)
        return None, None, None, None, None, None, None, None