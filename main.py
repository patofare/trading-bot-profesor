from visualization.charts import plot_price_with_signals
from core.analysis import run_analysis
from utils.market_selector import select_market_and_ticker
from education.menu import theory_menu

def welcome_menu():
    print("===================================")
    print("  BIENVENIDO AL BOT PROFESOR 📊📘 ")
    print("===================================")
    print("¿Qué querés hacer?")
    print("1 - Práctica de análisis técnico")
    print("2 - Ver teoría y repasar conceptos")
    print("0 - Salir")

    return input("Elegí una opción: ").strip()

def main():
    while True:
        
        choice = welcome_menu()

        if choice == "0":
            print("Hasta luego 👋")
            break

        elif choice == "2":
            theory_menu()
            continue

        elif choice != "1":
            print("Opción inválida")
            continue

        ticker, market = select_market_and_ticker()

        if ticker is None:
            input("\nPresioná ENTER para volver al menú...")
            continue

        print("===================================")
        print(f"Mercado: {market}")
        print(f"Activo actual: {ticker}\n")

        print("1 - Ver análisis completo")
        print("2 - Ver solo gráfico")
        print("3 - Ver solo explicación del RSI")
        print("4 - Ver solo recomendación final")
        print("0 - Salir")

        option = input("Elegí una opción: ").strip()

        if option == "0":
            print("Saliendo del sistema...")
            break  

        df, signal, score, reasons, explanation, rsi_explanation, stop_loss, take_profit = run_analysis(ticker)
    
        if df is None:
            print("No se pudo completar el análisis.")
            return
        
        if option == "1":
            print("\nSeñal actual:", signal)
            print(f"Fuerza de la señal (score): {score}")

            print("\n Factores considerados:")
            for r in reasons:
                print(f" - {r}")

            print("\n Explicación general:")
            print(explanation)

            print("\n Explicación del RSI:")
            print(rsi_explanation)

            plot_price_with_signals(df, ticker, signal, score)

        elif option == "2":
            plot_price_with_signals(df, ticker, signal, score)

        elif option == "3":
            print("\n Explicación del RSI:")
            print(rsi_explanation)

        elif option == "4":
            print("\n Recomendación del sistema:")
            print(explanation)

        else:
            print("Opción inválida")

        print("\n¿Qué querés hacer ahora?")
        print("1 - Volver al menú principal")
        print("0 - Salir")
        
        next_action = input("Elegí una opción: ").strip()

        if next_action == "0":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()



