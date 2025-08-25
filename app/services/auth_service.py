from app.repositories.usuario_repo import UsuarioRepo
from app.utils import generar_uuid

class AuthService:
    def __init__(self):
        self.repo = UsuarioRepo()

    def login(self, email, contrasenia):
        usuario = self.repo.find_by_email(email)
        if not usuario:
            return None, 'Usuario no existe'
        if usuario.get('contrasenia') != contrasenia:
            return None, 'Contraseña inválida'
        return usuario, None

    def crear_usuario(self, documento, nombre, email, contrasenia, id_rol, id_sucursal=''):
        if self.repo.find_by_email(email):
            return None, 'Email ya registrado'
        nuevo = {
            'id': generar_uuid(),
            'documento': documento,
            'nombre': nombre,
            'email': email,
            'contrasenia': contrasenia,
            'id_rol': id_rol,
            'id_sucursal': id_sucursal,
        }
        self.repo.save(nuevo)
        return nuevo, None

    def listar(self):
        return self.repo.all()

    def actualizar(self, id, cambios):
        return self.repo.update(id, cambios)

    def eliminar(self, id):
        return self.repo.delete(id)