# 📚 Sistema de Gestión Académica del Colegio

**Categoría:** Misional — *Formación Académica* 

**Versión de Python:** 3.13.9  

## 🚫 Problema / Necesidad
En muchos colegios, los docentes y directivos aún registran las calificaciones de manera manual o en hojas de cálculo, lo que puede generar errores, pérdida de información o dificultad para calcular promedios y hacer seguimiento académico a los estudiantes.

Por esta razón, se propone crear un sistema académico que facilite el **registro de estudiantes, notas y el cálculo de promedios**, para apoyar la labor educativa y administrativa de la institución.



## 💡 Solución Propuesta
El sistema desarrollado es una **aplicación de consola** que permite gestionar los procesos académicos de forma organizada.  
Cuenta con distintos **roles de usuario**:
- **Rector:** supervisa el sistema general.  
- **Coordinador:** gestiona el registro de estudiantes.  
- **Profesor:** ingresa las notas y calcula promedios.
- **Estudiante:** ver notas y dtos.



##  🔧 Arquitectura del Proyecto
```
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
│     ├─ profesores.json          # Profesores
|     ├─ notas.json               # Guarda notas
|     ├─ estudiantes.json         # Estudiantes
|     ├─ comunicados.json         # Mensaje, fecha
|     ├─ avisos.json              # Aviso
│     └─ reportes/
│        └─ reporte_general.csv   # Salidas generadas
├─ tests/                         # (opcional) pruebas simples
├─ requirements.txt
├─ README.md
└─ .gitignore

```


## 📘 Manual de Usuario
**Requisitos previos**
- Tener Python 3.11.2 o superior instalado.
- (Opcional) Crear y activar un entorno virtual:
  
  python -m venv venv
  venv\Scripts\activate
  
**Instalación**
- Descargar o clonar el proyecto desde GitHub.
- (Opcional) Instalar las librerías necesarias:
  
  pip install -r requirements.txt

**Ejecución**
- python -m src.main
- python src/main.py



##  👩🏽‍💻 Temas de Python aplicados
- Funciones y modularización
- Estructuras de datos (listas, diccionarios)
- Manejo de archivos JSON
- Importación de módulos
- Condicionales y bucles
- Programación por roles y permisos



##  👩🏻‍🤝‍👩🏼 Trabajo Colaborativo
**Integrantes:**

- Samuel Castro — *Rol:* 
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

- Saira Aragon — *Rol:*
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
7. **Ver estadísticas del colegio:** 
   muestra cantidad de estudiantes, profesores y comunicados activos.  
8.  **Eliminar comunicados:** 
   marca un comunicado como inactivo (sin borrar el registro).  
9.  **Eliminar estudiantes o profesores:** 
   permite marcar registros como inactivos para mantener el historial.   

10. **Cerrar sesión**

---

- Angelica Garcia — *Rol:*
### Profesor

1. **Iniciar sesión**  
   Inicia sesión como usuario profesor con su respectiva contraseña.

2. **Mensajes de bienvenida**  
   Bienvenido rol profesor.

3. **Registra notas**  
   - Ingresa nombre de estudiante por si ID.
   - Grado.
   - Materia.
   - Nota(0-5).

4. **Ver notas**  
   Puede ver las notas de sus estudiantes por su ID.

5. **Listado de notas**  
   Se observa una tabla con nombre de estudiante, materia, nota y fecha..

6. **Calcular promedio**  
   Se calcula el promedio de cada estudiante por sus respectivas notas.

7. **Cerrar sesión**

---

- Karen Gonzales — *Rol: Estudiante *
1. **Iniciar sesión**  
   Inicia sesión como usuario *estudiante* con su respectiva contraseña registrada en `usuarios.json`.

2. **Mensaje de bienvenida**  
   El sistema muestra un mensaje de acceso exitoso indicando el rol *estudiante*.

3. **Ver mis datos**  
   Permite consultar la información personal del estudiante, incluyendo:  
   - ID  
   - Nombre  
   - Grado  

4. **Ver mis notas**  
   Muestra todas las calificaciones registradas del estudiante con:  
   - Materia  
   - Nota  
   - Fecha de registro  
   Además, calcula y presenta el **promedio general**.

5. **Mensajes de alerta**  
   Si el ID no existe o el estudiante no tiene notas, se muestran mensajes informativos para orientar al usuario.

6. **Cerrar sesión**  
   Finaliza la sesión del estudiante y permite volver al inicio de sesión.

---
  

**Repositorio**
- https://github.com/samuelcastr/colegio.git



## 🔮 Límites y mejoras futuras
- Implementar autenticación segura (encriptar contraseñas).
- Agregar reportes automáticos (PDF).
- Integrar una interfaz gráfica o versión web.
- Permitir filtrar promedios por materia o grado.

## 📸 Ejemplos de uso

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

### Ejemplo de registro de estudiante

```bash
Ingrese nombre del estudiante: Juan Pérez
Copiar código
Asunto del aviso: Reunión urgente
Mensaje: Se requiere reunión con todos los profesores el viernes.
✅ Aviso enviado correctamente al rector.
✅ Estudiante 'Juan Pérez' registrado exitosamente.
```

### Ejemplo de registro de Profesor

```bash
=== SISTEMA DE GESTION DEL COLEGIO ===
Ingrese su nombre de usuario: Prof1
Ingrese su contraseña: p201

✅ Bienvenido, prof1 (rol: profesor)
```

```bash
=== MENÚ DEL PROFESOR ===
1. Registrar nota
2. Ver notas
3. Calcular promedio
4. Cerrar sesión

Seleccione una opción: 1

=== REGISTRAR NOTA ===
ID:1 | Andrés - Grado: 11
ID:2 | Camila - Grado: 10
ID:3 | Estu1 - Grado: 11

Ingrese el ID del estudiante: 1
Ingrese el grado del estudiante: 11
Ingrese materia: Inglés
Ingrese nota (0-5): 4

✅ Nota registrada correctamente para Andrés (Grado 11).


=== MENÚ DEL PROFESOR ===
1. Registrar nota
2. Ver notas
3. Calcular promedio
4. Cerrar sesión

Seleccione una opción: 2

📘 --- LISTADO DE NOTAS ---
Andrés | Inglés | Grado: 11 = 4.0  (2025-10-31)
Camila | Lenguaje | Grado: 10 = 3.5  (2025-10-30)
Estu1  | Matemáticas | Grado: 11 = 4.2  (2025-10-31)


Seleccione una opción: 3
Ingrese el ID del estudiante: 1

📊 Promedio de Andrés (Grado: 11): 4.00
```

```bash
Seleccione una opción: 4
👋 Cerrando sesión del profesor...
```


### 🛠️ Archivos principales

```bash
coordinador.py: Funciones para registrar, actualizar, eliminar estudiantes y profesores, enviar avisos y generar reportes.
rector.py: Funciones para ver avisos, listados, generar reportes y gestionar comunicados.
data_manager.py: Funciones auxiliares para leer y guardar archivos JSON.
estudiantes.json, profesores.json, avisos.json, comunicados.json: Archivos que almacenan la información del sistema.
reporte_general.csv: Archivo generado automáticamente con los datos de estudiantes y profesores.
```