from src.roles import rector, coordinador

def mostrar_menu(rol):
    """Muestra menú según el rol."""
    if rol == "rector":
        rector.menu_rector()
    elif rol == "coordinador":
        coordinador.menu_coordinador()
    else:
        print("⚠️ Rol no reconocido o sin permisos.")
