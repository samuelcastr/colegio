colegio-sistema/
├─ src/
│  ├─ main.py                     # Punto de entrada con menú o CLI
│  ├─ core/
│  │  ├─ auth.py                  # Login / autenticación (roles)
│  │  ├─ menu.py                  # Menú principal dinámico según el rol
│  │  └─ utils.py                 # Validaciones, IDs, logs, etc.
│  ├─ roles/
│  │  ├─ rector.py                # Funciones del rector
│  │  ├─ coordinador.py           # Funciones del coordinador
│  │  ├─ profesor.py              # Funciones del profesor
│  │  └─ estudiante.py            # Funciones del estudiante
│  ├─ modules/
│  │  ├─ models.py                # Clases: Usuario, Solicitud, Nota, etc.
│  │  ├─ data_manager.py          # Guardar/cargar datos (JSON)
│  │  ├─ reportes.py              # Generación de CSV de resultados
│  │  └─ notificaciones.py        # Mensajes automáticos / recordatorios
│  └─ data/
│     ├─ usuarios.json            # Base de datos simulada
│     ├─ solicitudes.json         # Casos o peticiones
│     └─ reportes/
│        └─ reporte_general.csv   # Salidas generadas
├─ tests/                         # (opcional) pruebas simples
├─ requirements.txt
├─ README.md
└─ .gitignore
