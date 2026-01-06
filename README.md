Bot Profesor de Análisis Técnico

Proyecto educativo de análisis técnico en Python que combina indicadores clásicos, gestión de riesgo y explicaciones didácticas para aprender a interpretar el mercado, no solo operar.

¿Qué hace este bot?

- Analiza activos de **Argentina y USA**
- Calcula indicadores técnicos:
  - EMA 20 / EMA 50
  - RSI (14)
  - Volumen relativo
  - ATR (volatilidad)
- Genera señales:
  - BUY / BUY FUERTE / HOLD / SELL
- Asigna un score de fuerza
- Calcula Stop Loss y Take Profit basados en ATR
- Explica por qué se genera cada señal (modo profesor)
- Visualiza el análisis con gráficos en Matplotlib

 Enfoque educativo

El objetivo no es automatizar trading, sino:
- Entender qué mide cada indicador
- Aprender cuándo **NO** operar
- Interpretar contexto, tendencia y volatilidad
- Practicar análisis técnico de forma responsable

Tecnologías

- Python
- yfinance
- pandas
- matplotlib

Ejecución

```bash
pip install -r requirements.txt
python main.py
