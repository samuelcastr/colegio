import json
import os

# Ruta base del proyecto (desde src/)
BASE_DIR = os.path.dirname(__file__)  # apunta a /src/modules
DATA_DIR = os.path.join(BASE_DIR, "..", "data")  # sube un nivel y entra a /data
DATA_DIR = os.path.abspath(DATA_DIR)  # convierte en ruta absoluta correcta


def load_json(filepath):
    """Carga datos desde un archivo JSON y devuelve una lista o dict."""
    if not os.path.exists(filepath):
        print(f"⚠️ No se encontró el archivo: {os.path.abspath(filepath)}")
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer el JSON en {filepath}")
        return []
    
def save_json(filename, data):
    """Guarda datos en formato JSON dentro de la carpeta data."""
    # Si el usuario pasó una ruta completa, nos quedamos solo con el nombre del archivo
    filename = os.path.basename(filename)
    path = os.path.join(DATA_DIR, filename)

    try:
        os.makedirs(DATA_DIR, exist_ok=True)  # crea la carpeta si no existe
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            print(f"✅ Datos guardados correctamente en {path}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo {filename}: {e}")