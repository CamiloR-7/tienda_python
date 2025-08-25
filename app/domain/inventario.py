class Inventario:
    def __init__(self, id, id_producto, id_sucursal, existencia=0):
        self.id = id
        self.id_producto = id_producto
        self.id_sucursal = id_sucursal
        self.existencia = int(existencia)