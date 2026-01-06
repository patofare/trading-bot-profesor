import os
import yfinance as yf
import pandas as pd


def load_stock_data(ticker, period="2y"):        ## Define las variables que vamos a usar en la carga de datos nombre del ticker, fecha de inicio de toma de datos y fecha de fin
    
    data = yf.download(ticker, period=period, auto_adjust=True)
    
    if data.empty:
        raise ValueError("No se encontraron datos para el ticker solicitado")
    
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    data = data.reset_index()

    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{ticker}_raw.csv"
    data.to_csv(file_path, index=False)
    
    return data