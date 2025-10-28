# src/modules/models.py
import uuid

class Usuario:
    """
    Clase base para representar a cualquier usuario del sistema.
    Cada usuario tiene un id, nombre, rol y credenciales.
    """
    def __init__(self, nombre, usuario, contrasena, rol):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def __repr__(self):
        return f"{self.rol} - {self.nombre} ({self.usuario})"


class Rector(Usuario):
    """
    Clase para el rol de Rector.
    Puede ver reportes y gestionar coordinadores.
    """
    def __init__(self, nombre, usuario, contrasena):
        super().__init__(nombre, usuario, contrasena, rol="rector")


class Coordinador(Usuario):
    """
    Clase para el rol de Coordinador.
    Puede registrar solicitudes y gestionarlas.
    """
    def __init__(self, nombre, usuario, contrasena):
        super().__init__(nombre, usuario, contrasena, rol="coordinador")
