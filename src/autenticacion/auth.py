from src.modules.data_manager import load_json

def login():
    """Solicita usuario y contraseña, valida en usuarios.json y devuelve el rol."""
    usuarios = load_json("src/data/usuarios.json")

    if not usuarios:
        print("⚠️ No hay usuarios registrados. Debe registrar al menos un rector o coordinador.")
        return None

    print("\n=== INICIO DE SESIÓN ===")
    usuario = input("👤 Usuario: ").strip()
    contraseña = input("🔑 Contraseña: ").strip()

    for u in usuarios:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            print(f"\n✅ Bienvenido, {usuario}. Rol: {u['rol'].capitalize()}")
            return u["rol"]

    print("❌ Usuario o contraseña incorrectos.")
    return None
