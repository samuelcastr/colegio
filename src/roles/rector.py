# src/roles/rector.py
import csv
from src.modules.data_manager import load_json, save_json

DATA_PATH = "src/data/usuarios.json"
CSV_PATH = "src/data/reportes/reporte_general.csv"

def mostrar_usuarios():
    usuarios = load_json(DATA_PATH)
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return
    print("\n📋 LISTA DE USUARIOS:")
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Rol: {u['rol']}")
    print("")

def registrar_coordinador():
    usuarios = load_json(DATA_PATH)
    nuevo_id = len(usuarios) + 1
    nombre = input("Ingrese nombre del coordinador: ")
    usuario = {"id": nuevo_id, "nombre": nombre, "rol": "coordinador"}
    usuarios.append(usuario)
    save_json(DATA_PATH, usuarios)
    print(f"✅ Coordinador '{nombre}' registrado correctamente.\n")

def generar_reporte_csv():
    usuarios = load_json(DATA_PATH)
    if not usuarios:
        print("⚠️ No hay datos para generar el reporte.")
        return

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "rol"])
        writer.writeheader()
        writer.writerows(usuarios)

    print(f"📁 Reporte generado en: {CSV_PATH}\n")

def menu_rector():
    while True:
        print("\n=== MENÚ DEL RECTOR ===")
        print("1. Ver reportes generales")
        print("2. Gestionar coordinadores")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("📊 Mostrando reportes generales...")
        elif opcion == "2":
            print("👥 Gestión de coordinadores...")
        elif opcion == "3":
            print("👋 Cerrando sesión...")
            break
        else:
            print("⚠️ Opción no válida.")

