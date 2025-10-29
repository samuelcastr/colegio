## 📂 Estructura del Proyecto.

La estructura del proyecto está organizada de la siguiente manera para facilitar el desarrollo y mantenimiento del sistema de gestión escolar:

> [!IMPORTANT]
> esto es provicional


```plaintext
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


```

## ⚙️ Funcionalidades

### Coordinador

1. **Registrar estudiante**  
   Permite agregar un estudiante con `nombre` y `grado`.

2. **Asignar profesor**  
   Permite agregar un profesor con `nombre` y `materia`.

3. **Ver listados**  
   Muestra todos los estudiantes y profesores registrados.

4. **Eliminar estudiante / profesor**  
   Permite eliminar un estudiante o profesor mediante su `ID`.

5. **Actualizar estudiante / profesor**  
   Permite actualizar el nombre y grado de un estudiante o la información de un profesor.

6. **Enviar aviso al rector**  
   Envía un aviso que quedará registrado en `avisos.json`.

7. **Ver avisos enviados**  
   Permite revisar todos los avisos enviados al rector.

8. **Generar reporte CSV**  
   Genera un archivo `reporte_general.csv` con todos los estudiantes y profesores.

9. **Cerrar sesión**

---

### Rector

1. **Ver avisos de coordinadores**  
   Permite revisar todos los avisos enviados por los coordinadores.

2. **Ver listados de estudiantes y profesores**  
   Permite visualizar los datos registrados.

3. **Generar reporte CSV**  
   Genera un archivo `reporte_general.csv` con los datos de estudiantes y profesores.

4. **Enviar comunicado general**  
   Permite crear un comunicado dirigido a toda la institución (guardado en `comunicados.json`).

5. **Ver comunicados**  
   Permite visualizar todos los comunicados enviados por el rector.

6. **Actualizar comunicado**  
   Permite modificar el asunto o el mensaje de un comunicado existente.

7. **Cerrar sesión**

---

## 📄 Ejemplo de uso

### Ejecutar el sistema


### 📄 Ejemplo de uso

#### Ejecutar el sistema

```bash
python src/main.py
Se presentará un menú para seleccionar el rol: Coordinador o Rector. Cada rol tendrá acceso a sus funcionalidades correspondientes.
```
### Ejemplo de registro de estudiante

```bash
Ingrese nombre del estudiante: Juan Pérez
Ingrese grado del estudiante: 5
✅ Estudiante 'Juan Pérez' registrado exitosamente.
```

### Ejemplo de envío de aviso al rector

```bash
Asunto del aviso: Reunión urgente
Mensaje: Se requiere reunión con todos los profesores el viernes.
✅ Aviso enviado correctamente al rector.
```

### Ejemplo de generar reporte CSV

```bash
📊 Reporte CSV generado exitosamente en src/data/reportes/reporte_general.csv
```

### 🛠️ Archivos principales

```bash
coordinador.py: Funciones para registrar, actualizar, eliminar estudiantes y profesores, enviar avisos y generar reportes.
rector.py: Funciones para ver avisos, listados, generar reportes y gestionar comunicados.
data_manager.py: Funciones auxiliares para leer y guardar archivos JSON.
estudiantes.json, profesores.json, avisos.json, comunicados.json: Archivos que almacenan la información del sistema.
reporte_general.csv: Archivo generado automáticamente con los datos de estudiantes y profesores.
```

### 📝 Consideraciones

```bash
- Todos los IDs son incrementales y únicos.
- Los archivos JSON se crean automáticamente si no existen.
- El sistema está pensado para ser ejecutado en consola.
- Los reportes CSV se generan en src/data/reportes/.
```
### Ejemplo de registro de estudiante

```bash
Ingrese nombre del estudiante: Juan Pérez
Copiar código
Asunto del aviso: Reunión urgente
Mensaje: Se requiere reunión con todos los profesores el viernes.
✅ Aviso enviado correctamente al rector.
✅ Estudiante 'Juan Pérez' registrado exitosamente.
```
### Ejemplo de envío de aviso al rector

```bash
Asunto del aviso: Reunión urgente
Mensaje: Se requiere reunión con todos los profesores el viernes.
✅ Aviso enviado correctamente al rector.
```
### 🛠️ Archivos principales

```bash
coordinador.py: Funciones para registrar, actualizar, eliminar estudiantes y profesores, enviar avisos y generar reportes.
rector.py: Funciones para ver avisos, listados, generar reportes y gestionar comunicados.
data_manager.py: Funciones auxiliares para leer y guardar archivos JSON.
estudiantes.json, profesores.json, avisos.json, comunicados.json: Archivos que almacenan la información del sistema.
reporte_general.csv: Archivo generado automáticamente con los datos de estudiantes y profesores.
```
```bash     
coordinador.py: Funciones para registrar, actualizar, eliminar estudiantes y profesores, enviar avisos y generar reportes.
rector.py: Funciones para ver avisos, listados, generar reportes y gestionar comunicados.
data_manager.py: Funciones auxiliares para leer y guardar archivos JSON.
estudiantes.json, profesores.json, avisos.json, comunicados.json: Archivos que almacenan la información del sistema.
reporte_general.csv: Archivo generado automáticamente con los datos de estudiantes y profesores.
```
### 📝 Consideraciones
- Todos los IDs son incrementales y únicos.
- Los archivos JSON se crean automáticamente si no existen.
- El sistema está pensado para ser ejecutado en consola.
- Los reportes CSV se generan en src/data/reportes/.