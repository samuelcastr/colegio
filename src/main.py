# src/main.py
from src.modules.data_manager import load_json
from src.roles.rector import menu_rector
from src.roles.coordinador import menu_coordinador
from src.roles.profesor import menu_profesor
from src.roles.estudiante import menu_estudiante

USUARIOS_PATH = "src/data/usuarios.json"


def login():
    """
    Simula un inicio de sesión simple.
    Busca el usuario por nombre y lo identifica por rol.
    """
    usuarios = load_json(USUARIOS_PATH)
    if not usuarios:
        print("⚠️ No hay usuarios registrados. Debe registrar al menos un rector o coordinador.")
        return None

    usuario_input = input("Ingrese su nombre de usuario: ").strip()
    contraseña_input = input("Ingrese su contraseña: ").strip()

    for u in usuarios:
        if u["usuario"].lower() == usuario_input.lower() and u["contraseña"] == contraseña_input:
            print(f"\n✅ Bienvenido, {u['usuario']} (rol: {u['rol']})\n")
            return u

    print("❌ Usuario o contraseña incorrectos.\n")
    return None


def main():
    print("=== SISTEMA DE GESTIÓN DEL COLEGIO ===\n")

    while True:
        usuario = login()
        if not usuario:
            opcion = input("¿Desea intentar de nuevo? (s/n): ").lower()
            if opcion != "s":
                print("👋 Saliendo del sistema...")
                break
            else:
                continue

        rol = usuario["rol"]

        if rol == "rector":
            menu_rector()
        elif rol == "coordinador":
            menu_coordinador()
        elif rol == "profesor":
            menu_profesor()
        elif rol == "estudiante":
            menu_estudiante()  
        else:
            print(f"⚠️ Rol '{rol}' no tiene menú asignado todavía.\n")

        # Preguntar si desea cerrar sesión o salir del programa
        opcion = input("\n¿Desea cerrar sesión (1) o salir del programa (2)? ").strip()
        if opcion == "1":
            print("\n🔁 Cerrando sesión... Volviendo al inicio.\n")
            continue  # vuelve a pedir login
        elif opcion == "2":
            print("\n👋 Saliendo completamente del sistema. Hasta luego.")
            break
        else:
            print("\n⚠️ Opción no válida. Saliendo por seguridad.")
            break


if __name__ == "__main__":
    main()
