class Usuario:
    def __init__(self, id, documento, nombre, email, contrasenia, id_rol, id_sucursal=''):
        self.id = id
        self.documento = documento
        self.nombre = nombre
        self.email = email
        self.contrasenia = contrasenia
        self.id_rol = id_rol
        self.id_sucursal = id_sucursal