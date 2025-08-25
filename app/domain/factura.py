from decimal import Decimal

class Factura:
    def __init__(self, id, numero, fecha, id_sucursal, subtotal, iva, total, id_estado=''):
        self.id = id
        self.numero = numero
        self.fecha = fecha
        self.id_sucursal = id_sucursal
        self.subtotal = Decimal(subtotal)
        self.iva = Decimal(iva)
        self.total = Decimal(total)
        self.id_estado = id_estado