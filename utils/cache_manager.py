import os

def clear_data_cache(folder="data/raw"):
    """
    Elimina todos los archivos CSV del cache de datos
    """
    if not os.path.exists(folder):
        print("No existe carpeta de cache")
        return

    files = [f for f in os.listdir(folder) if f.endswith(".csv")]

    if not files:
        print("No hay archivos para borrar")
        return

    for file in files:
        os.remove(os.path.join(folder, file))

    print(f"Cache limpiado ({len(files)} archivos eliminados)")
