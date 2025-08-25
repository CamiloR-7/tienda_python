from decimal import Decimal


class Producto:
    def __init__(self, id, codigo, nombre, precio, costo, id_categoria='', fecha_creacion='', id_estado=''):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.precio = Decimal(precio)
        self.costo = Decimal(costo)
        self.id_categoria = id_categoria
        self.fecha_creacion = fecha_creacion
        self.id_estado = id_estado