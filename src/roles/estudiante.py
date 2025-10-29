from src.modules.data_manager import load_json
from datetime import datetime

ESTUDIANTES_FILE = "src/data/estudiantes.json"
NOTAS_FILE = "src/data/notas.json"


def ver_mis_notas():
    """Permite al estudiante ver sus notas según su ID."""
    estudiantes = load_json(ESTUDIANTES_FILE)
    notas = load_json(NOTAS_FILE)

    if not estudiantes:
        print("⚠️ No hay estudiantes registrados.\n")
        return

    id_est = input("Ingrese su ID de estudiante: ").strip()
    estudiante = next((e for e in estudiantes if str(e["id"]) == id_est), None)

    if not estudiante:
        print("❌ No se encontró estudiante con ese ID.\n")
        return

    notas_est = [n for n in notas if str(n["id_estudiante"]) == id_est]

    if not notas_est:
        print(f"📭 No hay notas registradas para {estudiante['nombre']}.\n")
        return

    print(f"\n📘 --- NOTAS DE {estudiante['nombre']} ---")
    for n in notas_est:
        print(f"{n['materia']}: {n['nota']}  ({n['fecha']})")

    promedio = sum(n["nota"] for n in notas_est) / len(notas_est)
    print(f"\n📊 Promedio general: {promedio:.2f}\n")


def ver_mis_datos():
    """Muestra la información básica del estudiante."""
    estudiantes = load_json(ESTUDIANTES_FILE)

    id_est = input("Ingrese su ID de estudiante: ").strip()
    estudiante = next((e for e in estudiantes if str(e["id"]) == id_est), None)

    if not estudiante:
        print("❌ No se encontró estudiante con ese ID.\n")
        return

    print(f"""
=== DATOS DEL ESTUDIANTE ===
🪪 ID: {estudiante['id']}
👩‍🎓 Nombre: {estudiante['nombre']}
📘 Grado: {estudiante['grado']}
""")


def menu_estudiante():
    """Menú principal para el estudiante."""
    while True:
        print("""
=== MENÚ DEL ESTUDIANTE ===
1. Ver mis datos
2. Ver mis notas
3. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ver_mis_datos()
        elif opcion == "2":
            ver_mis_notas()
        elif opcion == "3":
            print("👋 Cerrando sesión del estudiante...\n")
            break
        else:
            print("🚫 Opción no válida, intente nuevamente.\n")
