from app.repositories.base_repo import BaseRepo
from app.config import HEADERS

class InventarioRepo(BaseRepo):
    def __init__(self):
        super().__init__('inventario', HEADERS['inventario'])

    def find_by_producto_sucursal(self, id_producto, id_sucursal):
        encontrados = self.filter(id_producto=id_producto, id_sucursal=id_sucursal)
        return encontrados[0] if encontrados else None