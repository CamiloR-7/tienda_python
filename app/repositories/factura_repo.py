from app.repositories.base_repo import BaseRepo
from app.config import HEADERS
from datetime import datetime

class FacturaRepo(BaseRepo):
    def __init__(self):
        super().__init__('factura', HEADERS['factura'])

    def next_incremento_por_sucursal_y_fecha(self, id_sucursal, fecha_yyyymmdd):
        cuentas = 0
        for f in self.all():
            if f.get('id_sucursal') == id_sucursal and f.get('fecha','').startswith(fecha_yyyymmdd):
                cuentas += 1
        return cuentas + 1