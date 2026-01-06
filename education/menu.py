from education.theory import THEORY_TOPICS

def theory_menu():
    while True:
        print("\n📘 TEORÍA - ANÁLISIS TÉCNICO")
        print("1 - ¿Qué es una EMA?")
        print("2 - ¿Qué es el RSI?")
        print("3 - ¿Qué significa el cruce de EMAs?")
        print("4 - ¿Qué es el ATR?")
        print("5 - Volver al menú principal")

        option = input("Elegí un tema: ").strip()

        if option == "5":
            break

        explanation = THEORY_TOPICS.get(option)
        if explanation:
            print("\n" + explanation)
            input("\nPresioná ENTER para continuar...")
        else:
            print("Opción inválida")