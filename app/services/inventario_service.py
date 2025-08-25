from app.repositories.inventario_repo import InventarioRepo
from app.utils import generar_uuid

class InventarioService:
    def __init__(self):
        self.repo = InventarioRepo()

    def ajustar(self, id_producto, id_sucursal, delta):
        fila = self.repo.find_by_producto_sucursal(id_producto, id_sucursal)
        if fila:
            nueva = int(fila.get('existencia', '0')) + int(delta)
            if nueva < 0:
                return False, 'Stock insuficiente'
            self.repo.update(fila['id'], {'existencia': str(nueva)})
            return True, None
        else:
            nuevo = {
                'id': generar_uuid(),
                'id_producto': id_producto,
                'id_sucursal': id_sucursal,
                'existencia': str(max(0,int(delta)))
            }
            self.repo.save(nuevo)
            return True, None

    def existencia(self, id_producto, id_sucursal):
        fila = self.repo.find_by_producto_sucursal(id_producto, id_sucursal)
        if not fila:
            return 0
        return int(fila.get('existencia', '0'))