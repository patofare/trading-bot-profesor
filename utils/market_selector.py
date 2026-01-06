def select_market_and_ticker():
    print("\nSeleccioná el mercado:")
    print("1 - Argentina")
    print("2 - USA")

    market_option = input("Elegí mercado: ").strip()
    if market_option not in ["1", "2"]:
        print("Mercado inválido")
        return None, None

    ticker_input = input("Ingresá el ticker (ej: YPFD, GGAL, AAPL): ").strip().upper()
    if ticker_input == "":
        print("Ticker vacío")
        return None, None

    if market_option == "1":
        market = "Argentina"
        if not ticker_input.endswith(".BA"):
            ticker = ticker_input + ".BA"
        else:
            ticker = ticker_input

    else:
        market = "USA"
        ticker = ticker_input

    return ticker, market