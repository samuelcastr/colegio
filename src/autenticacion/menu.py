from src.roles import rector, coordinador, profesor, estudiante

def mostrar_menu(rol):
    """Muestra el menú correspondiente según el rol del usuario."""
    if rol == "rector":
        rector.menu_rector()
    elif rol == "coordinador":
        coordinador.menu_coordinador()
    elif rol == "profesor":
        profesor.menu_profesor()
    elif rol == "estudiante":
        estudiante.menu_estudiante()
    else:
        print("⚠️ Rol no reconocido o sin permisos.")

