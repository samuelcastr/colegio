from src.modules.data_manager import load_json, save_json
import os
import csv
from datetime import datetime

ESTUDIANTES_FILE = "src/data/estudiantes.json"
PROFESORES_FILE = "src/data/profesores.json"
AVISOS_FILE = "src/data/avisos.json"
COMUNICADOS_FILE = "src/data/comunicados.json"  # opcional para comunicados del rector

def ver_avisos():
    avisos = load_json(AVISOS_FILE)
    print("\n📬 --- AVISOS DE COORDINADORES ---")
    if not avisos:
        print("⚠️ No hay avisos registrados.\n")
        return
    for a in avisos:
        print(f"ID:{a.get('id')} | {a.get('fecha')} | {a.get('asunto')}\n  {a.get('mensaje')}\n")


def ver_listados():
    estudiantes = load_json(ESTUDIANTES_FILE)
    profesores = load_json(PROFESORES_FILE)

    print("\n📋 --- LISTADO DE ESTUDIANTES ---")
    if estudiantes:
        for e in estudiantes:
            print(f"ID:{e.get('id','?')}  👩‍🎓 {e['nombre']} - Grado: {e['grado']}")
    else:
        print("⚠️ No hay estudiantes registrados.")

    print("\n👨‍🏫 --- LISTADO DE PROFESORES ---")
    if profesores:
        for p in profesores:
            print(f"ID:{p.get('id','?')}  {p['nombre']} - Materia: {p['materia']}")
    else:
        print("⚠️ No hay profesores registrados.")


def generar_reporte():
    try:
        estudiantes = load_json(ESTUDIANTES_FILE)
        profesores = load_json(PROFESORES_FILE)

        reportes_dir = os.path.join("src", "data", "reportes")
        os.makedirs(reportes_dir, exist_ok=True)
        ruta_csv = os.path.join(reportes_dir, "reporte_general.csv")

        with open(ruta_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Tipo", "Nombre", "Detalle"])
            for e in estudiantes:
                writer.writerow(["Estudiante", e.get("nombre"), e.get("grado")])
            for p in profesores:
                writer.writerow(["Profesor", p.get("nombre"), p.get("materia")])

        print(f"📊 Reporte CSV generado exitosamente en {ruta_csv}\n")
    except Exception as e:
        print(f"❌ Error al generar reporte: {e}\n")


def enviar_comunicado():
    print("\n=== ENVIAR COMUNICADO GENERAL ===")
    asunto = input("Asunto: ").strip()
    mensaje = input("Mensaje: ").strip()

    if not asunto or not mensaje:
        print("⚠️ El asunto y mensaje no pueden estar vacíos.\n")
        return

    comunicados = load_json(COMUNICADOS_FILE)
    nuevo = {
        "id": _next_id(comunicados),
        "asunto": asunto,
        "mensaje": mensaje,
        "fecha": datetime.utcnow().isoformat()
    }
    comunicados.append(nuevo)
    save_json(COMUNICADOS_FILE, comunicados)
    print("✅ Comunicado enviado correctamente.\n")

def ver_comunicados():
    comunicados = load_json(COMUNICADOS_FILE)
    print("\n📬 --- COMUNICADOS GENERALES ---")
    if not comunicados:
        print("⚠️ No hay comunicados registrados.\n")
        return
    for c in comunicados:
        print(f"ID:{c.get('id')} | {c.get('fecha')} | {c.get('asunto')}\n  {c.get('mensaje')}\n")

def actualizar_comunicado():
    comunicados = load_json(COMUNICADOS_FILE)
    if not comunicados:
        print("\n⚠️ No hay comunicados registrados.\n")
        return

    print("\n=== ACTUALIZAR COMUNICADO ===")
    for c in comunicados:
        print(f"ID:{c.get('id')} | {c.get('fecha')} | {c.get('asunto')}")

    id_sel = input("\nIngrese el ID del comunicado a actualizar: ").strip()
    comunicado = next((c for c in comunicados if str(c.get('id')) == id_sel), None)

    if not comunicado:
        print("❌ No se encontró comunicado con ese ID.\n")
        return

    asunto = input(f"Ingrese nuevo asunto [{comunicado['asunto']}]: ").strip()
    mensaje = input(f"Ingrese nuevo mensaje [{comunicado['mensaje']}]: ").strip()

    if asunto:
        comunicado['asunto'] = asunto
    if mensaje:
        comunicado['mensaje'] = mensaje

    save_json(COMUNICADOS_FILE, comunicados)
    print(f"✅ Comunicado ID {id_sel} actualizado correctamente.\n")



def menu_rector():
    while True:
        print("""
=== MENÚ DEL RECTOR ===
1. Ver avisos de coordinadores
2. Ver listados de estudiantes y profesores
3. Generar reporte CSV
4. Enviar comunicado general
5. Ver comunicados
6. Actualizar comunicado
7. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ver_avisos()
        elif opcion == "2":
            ver_listados()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            enviar_comunicado()
        elif opcion == "5":
            ver_comunicados()
        elif opcion == "6":
            actualizar_comunicado()
        elif opcion == "7":
            print("👋 Cerrando sesión del rector...\n")
            break
        else:
            print("⚠️ Opción no válida, intente nuevamente.\n")
                              


# ------- helpers internos -------
def _next_id(items):
    if not items:
        return 1
    try:
        max_id = max(int(i.get("id", 0)) for i in items)
        return max_id + 1
    except Exception:
        return len(items) + 1
