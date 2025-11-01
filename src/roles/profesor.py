from src.modules.data_manager import load_json, save_json
from datetime import datetime

ESTUDIANTES_FILE = "src/data/estudiantes.json"
PROFESORES_FILE = "src/data/profesores.json"
NOTAS_FILE = "src/data/notas.json"


def registrar_nota():
    estudiantes = load_json(ESTUDIANTES_FILE)
    notas = load_json(NOTAS_FILE)

    if not estudiantes:
        print("👩🏼‍🎓 No hay estudiantes registrados.\n")
        return

    print("\n=== REGISTRAR NOTA ===")
    for e in estudiantes:
        print(f"ID:{e['id']} | {e['nombre']} - Grado: {e['grado']}")

    id_est = input("\nIngrese el ID del estudiante: ").strip()
    estudiante = next((e for e in estudiantes if str(e["id"]) == id_est), None)

    if not estudiante:
        print("❌ No se encontró estudiante con ese ID.\n")
        return

    grado = input("Ingrese el grado del estudiante: ").strip()
    if not grado.isdigit():
        print("⚠️ El grado debe ser un número.\n")
        return

    materia = input("Ingrese materia: ").strip()
    nota = input("Ingrese nota (0-5): ").strip()

    try:
        nota = float(nota)
        if nota < 0 or nota > 5:
            raise ValueError
    except ValueError:
        print("⚠️ La nota debe ser un número entre 0 y 5.\n")
        return

    nueva_nota = {
        "id": _next_id(notas),
        "id_estudiante": estudiante["id"],
        "nombre_estudiante": estudiante["nombre"],
        "grado": int(grado),
        "materia": materia,
        "nota": nota,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    }

    notas.append(nueva_nota)
    save_json(NOTAS_FILE, notas)
    print(f"✅ Nota registrada correctamente para {estudiante['nombre']} (Grado {grado}).\n")


def ver_notas():
    notas = load_json(NOTAS_FILE)
    if not notas:
        print("⚠️ No hay notas registradas.\n")
        return

    print("\n📘 --- LISTADO DE NOTAS ---")
    for n in notas:
        print(f"{n['nombre_estudiante']} | {n['materia']} | Grado: {n['grado']} = {n['nota']}  ({n['fecha']})")


def calcular_promedio():
    notas = load_json(NOTAS_FILE)
    if not notas:
        print("📝 No hay notas registradas.\n")
        return

    id_est = input("Ingrese el ID del estudiante: ").strip()
    notas_est = [n for n in notas if str(n["id_estudiante"]) == id_est]

    if not notas_est:
        print("❎ Ese estudiante no tiene notas registradas.\n")
        return

    promedio = sum(n["nota"] for n in notas_est) / len(notas_est)
    print(f"\n📊 Promedio de {notas_est[0]['nombre_estudiante']} (Grado: {notas_est[0]['grado']}): {promedio:.2f}\n")


def menu_profesor():
    while True:
        print("""
=== MENÚ DEL PROFESOR ===
1. Registrar nota
2. Ver notas
3. Calcular promedio
4. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            print("👋 Cerrando sesión del profesor...\n")
            break
        else:
            print("🚫 Opción no válida, intente nuevamente.\n")


def _next_id(items):
    if not items:
        return 1
    try:
        return max(int(i.get("id", 0)) for i in items) + 1
    except Exception:
        return len(items) + 1
