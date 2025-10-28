# src/roles/coordinador.py
from src.modules.data_manager import load_json, save_json
import os
import csv
from datetime import datetime

# Usar SÓLO el nombre del archivo (data_manager hace el join con DATA_DIR)
ESTUDIANTES_FILE = "src/data/estudiantes.json"
PROFESORES_FILE = "src/data/profesores.json"
AVISOS_FILE = "src/data/avisos.json"
REPORTE_FILE = "src/data/reportes/reporte_general.csv"


def registrar_estudiante():
    estudiantes = load_json(ESTUDIANTES_FILE)

    nombre = input("Ingrese nombre del estudiante: ").strip()
    grado = input("Ingrese grado del estudiante: ").strip()

    nuevo = {
        "id": _next_id(estudiantes),
        "nombre": nombre,
        "grado": grado
    }
    estudiantes.append(nuevo)
    save_json(ESTUDIANTES_FILE, estudiantes)
    print(f"✅ Estudiante '{nombre}' registrado exitosamente.\n")


def asignar_profesor():
    profesores = load_json(PROFESORES_FILE)

    nombre = input("Ingrese nombre del profesor: ").strip()
    materia = input("Ingrese materia asignada: ").strip()

    nuevo = {
        "id": _next_id(profesores),
        "nombre": nombre,
        "materia": materia
    }
    profesores.append(nuevo)
    save_json(PROFESORES_FILE, profesores)
    print(f"✅ Profesor '{nombre}' asignado a '{materia}'.\n")

def eliminar_profesor():
    profesores = load_json(PROFESORES_FILE)
    if not profesores:
        print("\n⚠️ No hay profesores registrados.\n")
        return

    print("\n=== ELIMINAR PROFESOR ===")
    for p in profesores:
        print(f"ID: {p.get('id')} | {p.get('nombre')} - Materia: {p.get('materia')}")

    try:
        id_sel = input("\nIngrese el ID del profesor a eliminar: ").strip()
        # permitir que ingresen número o cadena id
        encontrado = next((d for d in profesores if str(d.get('id')) == id_sel), None)
        if not encontrado:
            print("❌ No se encontró profesor con ese ID.\n")
            return

        # Filtrar la lista excluyendo al profesor seleccionado
        profesores = [d for d in profesores if str(d.get('id')) != id_sel]
        save_json(PROFESORES_FILE, profesores)
        print(f"✅ Profesor '{encontrado['nombre']}' eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}\n")

def actualizar_profesor():
    profesores = load_json(PROFESORES_FILE)
    if not profesores:
        print("\n⚠️ No hay profesores registrados.\n")
        return

    print("\n=== ACTUALIZAR PROFESOR ===")
    for p in profesores:
        print(f"ID: {p.get('id')} | {p.get('nombre')} - Materia: {p.get('materia')}")

    id_sel = input("\nIngrese el ID del profesor a actualizar: ").strip()
    profesor = next((d for d in profesores if str(d.get('id')) == id_sel), None)

    if not profesor:
        print("❌ No se encontró profesor con ese ID.\n")
        return

    nombre = input(f"Ingrese nuevo nombre [{profesor['nombre']}]: ").strip()
    materia = input(f"Ingrese nueva materia [{profesor['materia']}]: ").strip()

    if nombre:
        profesor['nombre'] = nombre
    if materia:
        profesor['materia'] = materia

    save_json(PROFESORES_FILE, profesores)
    print(f"✅ Profesor ID {id_sel} actualizado correctamente.\n")


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

def actualizar_estudiante():
    estudiantes = load_json(ESTUDIANTES_FILE)
    if not estudiantes:
        print("\n⚠️ No hay estudiantes registrados.\n")
        return

    print("\n=== ACTUALIZAR ESTUDIANTE ===")
    for e in estudiantes:
        print(f"ID: {e.get('id')} | {e.get('nombre')} - Grado: {e.get('grado')}")

    id_sel = input("\nIngrese el ID del estudiante a actualizar: ").strip()
    estudiante = next((s for s in estudiantes if str(s.get('id')) == id_sel), None)

    if not estudiante:
        print("❌ No se encontró estudiante con ese ID.\n")
        return

    nombre = input(f"Ingrese nuevo nombre [{estudiante['nombre']}]: ").strip()
    grado = input(f"Ingrese nuevo grado [{estudiante['grado']}]: ").strip()

    if nombre:
        estudiante['nombre'] = nombre
    if grado:
        estudiante['grado'] = grado

    save_json(ESTUDIANTES_FILE, estudiantes)
    print(f"✅ Estudiante ID {id_sel} actualizado correctamente.\n")



def eliminar_estudiante():
    estudiantes = load_json(ESTUDIANTES_FILE)
    if not estudiantes:
        print("\n⚠️ No hay estudiantes registrados.\n")
        return

    print("\n=== ELIMINAR ESTUDIANTE ===")
    for e in estudiantes:
        print(f"ID: {e.get('id')} | {e.get('nombre')} - Grado: {e.get('grado')}")

    try:
        id_sel = input("\nIngrese el ID del estudiante a eliminar: ").strip()
        # permitir que ingresen número o cadena id
        encontrado = next((s for s in estudiantes if str(s.get('id')) == id_sel), None)
        if not encontrado:
            print("❌ No se encontró estudiante con ese ID.\n")
            return
        estudiantes = [s for s in estudiantes if str(s.get('id')) != id_sel]
        save_json(ESTUDIANTES_FILE, estudiantes)
        print(f"✅ Estudiante '{encontrado['nombre']}' eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}\n")


def enviar_aviso_rector():
    print("\n=== ENVIAR AVISO AL RECTOR ===")
    asunto = input("Asunto del aviso: ").strip()
    mensaje = input("Mensaje: ").strip()

    if not asunto or not mensaje:
        print("⚠️ El asunto y el mensaje no pueden estar vacíos.\n")
        return

    avisos = load_json(AVISOS_FILE)
    nuevo_aviso = {
        "id": _next_id(avisos),
        "asunto": asunto,
        "mensaje": mensaje,
        "fecha": datetime.utcnow().isoformat()
    }
    avisos.append(nuevo_aviso)
    save_json(AVISOS_FILE, avisos)
    print("\n✅ Aviso enviado correctamente al rector.\n")


def ver_avisos():
    avisos = load_json(AVISOS_FILE)
    print("\n📬 --- AVISOS ENVIADOS AL RECTOR ---")
    if not avisos:
        print("⚠️ No hay avisos registrados.\n")
        return
    for a in avisos:
        print(f"ID:{a.get('id')} | {a.get('fecha')} | {a.get('asunto')}\n  {a.get('mensaje')}\n")


def generar_reporte():
    """
    Genera un CSV con estudiantes y profesores.
    El archivo se guarda en src/data/reportes/reporte_general.csv
    """
    try:
        estudiantes = load_json(ESTUDIANTES_FILE)
        profesores = load_json(PROFESORES_FILE)

        # Crear carpeta de reportes si no existe
        reportes_dir = os.path.join("src", "data", "reportes")
        os.makedirs(reportes_dir, exist_ok=True)

        # Ruta final del archivo CSV
        ruta_csv = os.path.join(reportes_dir, "reporte_general.csv")

        # Escribir los datos
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


def menu_coordinador():
    while True:
        print("""
=== MENÚ DEL COORDINADOR ===
1. Registrar estudiante
2. Asignar profesor
3. Ver listados
4. Eliminar estudiante
5. Enviar aviso al rector
6. Ver avisos enviados
7. Generar reporte CSV
8. Eliminar profesor
9. Actualizar estudiante
10. Actualizar profesor
11. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            asignar_profesor()
        elif opcion == "3":
            ver_listados()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            enviar_aviso_rector()
        elif opcion == "6":
            ver_avisos()
        elif opcion == "7":
            generar_reporte()
        elif opcion == "8":
            eliminar_profesor()
        elif opcion == "9":
            actualizar_estudiante()
        elif opcion == "10":
            actualizar_profesor()
        elif opcion == "11":
            print("👋 Cerrando sesión del coordinador...\n")
            break
        else:
            print("⚠️ Opción no válida, intente nuevamente.\n")


# ------- helpers internos -------
def _next_id(items):
    """Retorna siguiente id incremental (como entero) para una lista de dicts con clave 'id'."""
    if not items:
        return 1
    try:
        max_id = max(int(i.get("id", 0)) for i in items)
        return max_id + 1
    except Exception:
        return len(items) + 1
