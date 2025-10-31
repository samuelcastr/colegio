from src.modules.data_manager import load_json, save_json
import os
import csv
from datetime import datetime

ESTUDIANTES_FILE = "src/data/estudiantes.json"
PROFESORES_FILE = "src/data/profesores.json"
AVISOS_FILE = "src/data/avisos.json"
COMUNICADOS_FILE = "src/data/comunicados.json" 




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
            if e.get("activo", True):
                print(f"ID:{e.get('id','?')}  👩‍🎓 {e['nombre']} - Grado: {e['grado']}")
    else:
        print("⚠️ No hay estudiantes registrados.")

    print("\n👨‍🏫 --- LISTADO DE PROFESORES ---")
    if profesores:
        for p in profesores:
            if p.get("activo", True):
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
        "fecha": datetime.utcnow().isoformat(),
        "activo": True
    }
    comunicados.append(nuevo)
    save_json(COMUNICADOS_FILE, comunicados)
    print("✅ Comunicado enviado correctamente.\n")


def ver_comunicados():
    comunicados = load_json(COMUNICADOS_FILE)
    print("\n📬 --- COMUNICADOS GENERALES ---")
    activos = [c for c in comunicados if c.get("activo", True)]
    if not activos:
        print("⚠️ No hay comunicados activos registrados.\n")
        return
    for c in activos:
        print(f"ID:{c.get('id')} | {c.get('fecha')} | {c.get('asunto')}\n  {c.get('mensaje')}\n")


def actualizar_comunicado():
    comunicados = load_json(COMUNICADOS_FILE)
    if not comunicados:
        print("\n⚠️ No hay comunicados registrados.\n")
        return

    print("\n=== ACTUALIZAR COMUNICADO ===")
    for c in comunicados:
        if c.get("activo", True):
            print(f"ID:{c.get('id')} | {c.get('fecha')} | {c.get('asunto')}")

    id_sel = input("\nIngrese el ID del comunicado a actualizar: ").strip()
    comunicado = next((c for c in comunicados if str(c.get('id')) == id_sel and c.get("activo", True)), None)

    if not comunicado:
        print("❌ No se encontró comunicado con ese ID o está inactivo.\n")
        return

    asunto = input(f"Ingrese nuevo asunto [{comunicado['asunto']}]: ").strip()
    mensaje = input(f"Ingrese nuevo mensaje [{comunicado['mensaje']}]: ").strip()

    if asunto:
        comunicado['asunto'] = asunto
    if mensaje:
        comunicado['mensaje'] = mensaje

    save_json(COMUNICADOS_FILE, comunicados)
    print(f"✅ Comunicado ID {id_sel} actualizado correctamente.\n")


# ================= NUEVAS FUNCIONALIDADES =================

def ver_estadisticas():
    """Muestra estadísticas generales del colegio."""
    estudiantes = load_json(ESTUDIANTES_FILE)
    profesores = load_json(PROFESORES_FILE)
    comunicados = load_json(COMUNICADOS_FILE)

    total_estudiantes = sum(1 for e in estudiantes if e.get("activo", True))
    total_profesores = sum(1 for p in profesores if p.get("activo", True))
    total_comunicados = sum(1 for c in comunicados if c.get("activo", True))

    print("\n📊 --- ESTADÍSTICAS DEL COLEGIO ---")
    print(f"👩‍🎓 Estudiantes activos: {total_estudiantes}")
    print(f"👨‍🏫 Profesores activos: {total_profesores}")
    print(f"📬 Comunicados activos: {total_comunicados}")
    print("------------------------------------\n")


def eliminar_comunicado():
    """Marca un comunicado como inactivo."""
    comunicados = load_json(COMUNICADOS_FILE)
    activos = [c for c in comunicados if c.get("activo", True)]

    if not activos:
        print("\n⚠️ No hay comunicados activos para eliminar.\n")
        return

    print("\n🗑️ --- ELIMINAR COMUNICADO ---")
    for c in activos:
        print(f"ID:{c.get('id')} | {c.get('asunto')}")

    id_sel = input("\nIngrese el ID del comunicado a eliminar: ").strip()
    comunicado = next((c for c in comunicados if str(c.get('id')) == id_sel), None)

    if not comunicado or not comunicado.get("activo", True):
        print("❌ No se encontró comunicado activo con ese ID.\n")
        return

    confirmar = input(f"⚠️ ¿Está seguro de eliminar el comunicado '{comunicado['asunto']}'? (s/n): ").lower()
    if confirmar == "s":
        comunicado["activo"] = False
        save_json(COMUNICADOS_FILE, comunicados)
        print("✅ Comunicado marcado como inactivo correctamente.\n")
    else:
        print("❎ Operación cancelada.\n")


def eliminar_registro():
    """Permite al rector eliminar (marcar como inactivo) estudiantes o profesores."""
    print("\n🗑️ --- ELIMINAR REGISTRO ---")
    print("1. Eliminar estudiante")
    print("2. Eliminar profesor")
    tipo = input("Seleccione una opción: ").strip()

    if tipo == "1":
        archivo = ESTUDIANTES_FILE
        tipo_txt = "estudiante"
    elif tipo == "2":
        archivo = PROFESORES_FILE
        tipo_txt = "profesor"
    else:
        print("⚠️ Opción no válida.\n")
        return

    registros = load_json(archivo)
    activos = [r for r in registros if r.get("activo", True)]

    if not activos:
        print(f"⚠️ No hay {tipo_txt}s activos registrados.\n")
        return

    for r in activos:
        print(f"ID:{r.get('id')} | {r['nombre']}")

    id_sel = input(f"Ingrese el ID del {tipo_txt} a eliminar: ").strip()
    registro = next((r for r in registros if str(r.get('id')) == id_sel), None)

    if not registro or not registro.get("activo", True):
        print(f"❌ No se encontró {tipo_txt} activo con ese ID.\n")
        return

    confirmar = input(f"⚠️ ¿Está seguro de eliminar a '{registro['nombre']}'? (s/n): ").lower()
    if confirmar == "s":
        registro["activo"] = False
        save_json(archivo, registros)
        print(f"✅ {tipo_txt.capitalize()} marcado como inactivo correctamente.\n")
    else:
        print("❎ Operación cancelada.\n")


# ================= MENÚ DEL RECTOR =================

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
7. Ver estadísticas generales
8. Eliminar comunicado
9. Eliminar profesor o estudiante
10. Cerrar sesión
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
            ver_estadisticas()
        elif opcion == "8":
            eliminar_comunicado()
        elif opcion == "9":
            eliminar_registro()
        elif opcion == "10":
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

