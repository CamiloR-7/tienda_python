from app.repositories.factura_repo import FacturaRepo
from app.utils import generar_uuid
from app.config import IVA
from datetime import datetime

class FacturaService:
    def __init__(self):
        self.repo = FacturaRepo()

    def numero_por_sucursal(self, id_sucursal):
        fecha = datetime.now()
        fecha_tag = fecha.strftime('%Y%m%d')
        incremento = self.repo.next_incremento_por_sucursal_y_fecha(id_sucursal, fecha_tag)
        return f'POS-{id_sucursal}-{fecha_tag}-{incremento}'

    def crear(self, id_sucursal, subtotal):
        iva = float(subtotal) * IVA
        total = float(subtotal) + iva
        nuevo = {
            'id': generar_uuid(),
            'numero': self.numero_por_sucursal(id_sucursal),
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'id_sucursal': id_sucursal,
            'subtotal': str(subtotal),
            'iva': str(round(iva,2)),
            'total': str(round(total,2)),
            'id_estado': 'emitida'
        }
        self.repo.save(nuevo)
        return nuevo