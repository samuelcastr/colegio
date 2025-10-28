import csv
from src.modules.data_manager import load_json

ESTUDIANTES_PATH = "src/data/estudiantes.json"
PROFESORES_PATH = "src/data/profesores.json"
REPORTE_PATH = "src/data/reportes/reporte_general.csv"

def generar_reporte_csv():
    estudiantes = load_json(ESTUDIANTES_PATH)
    profesores = load_json(PROFESORES_PATH)

    with open(REPORTE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Tipo", "Nombre", "Detalle"])

        for e in estudiantes:
            writer.writerow(["Estudiante", e["nombre"], e["grado"]])
        for p in profesores:
            writer.writerow(["Profesor", p["nombre"], p["materia"]])
