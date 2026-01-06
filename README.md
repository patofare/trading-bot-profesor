Trading Bot Profesor – Análisis Técnico Educativo

Trading Bot Profesor es un proyecto **educativo** desarrollado en Python que permite analizar activos financieros utilizando **indicadores técnicos clásicos**, explicando cada decisión como si fuera un profesor.

El objetivo no es automatizar trading real, sino **aprender y entender** cómo funcionan los indicadores y las reglas de análisis técnico.

---

Objetivo del proyecto

- Aprender análisis técnico desde una perspectiva práctica
- Comprender indicadores como:
  - EMA (medias móviles)
  - RSI
  - ATR (volatilidad)
  - Volumen relativo
- Traducir indicadores técnicos a **explicaciones en lenguaje natural**
- Construir una base sólida para futuros proyectos en:
  - Data Science
  - Trading cuantitativo
  - Análisis financiero

---

¿Qué hace el bot?

- Descarga datos históricos del mercado (Yahoo Finance)
- Calcula indicadores técnicos
- Evalúa reglas de trading educativas
- Genera:
  - Señal (Compra / Venta / Neutral)
  - Score de fuerza de señal
  - Explicación detallada del razonamiento
  - Stop Loss y Take Profit basados en ATR
- Muestra gráficos con señales

Todo el flujo está pensado para **entender el porqué**, no solo el resultado.

---

Tecnologías utilizadas

- Python 3
- pandas
- numpy
- yfinance
- matplotlib

Arquitectura modular:
- `core/` → lógica principal del análisis
- `indicators/` → indicadores técnicos
- `signals/` → reglas y explicaciones
- `visualization/` → gráficos
- `utils/` → utilidades generales

---

Disclaimer

Este proyecto es **100% educativo**.  
No constituye asesoramiento financiero ni recomendaciones de inversión.

El autor no se responsabiliza por el uso del código en entornos reales de trading.

---

Próximas mejoras

- Módulo teórico interactivo (EMA, RSI, cruces, volatilidad)
- Más indicadores técnicos
- Backtesting simple
- Exportación de reportes
- Integración con notebooks

---

Desarrollado por **Patricio Faré** 
Proyecto personal orientado a aprendizaje, data y finanzas.
