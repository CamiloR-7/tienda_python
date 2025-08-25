from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

IVA = 0.19

CSV_FILES = {
    'rol': DATA_DIR / 'rol.csv',
    'usuario': DATA_DIR / 'usuario.csv',
    'sucursal': DATA_DIR / 'sucursal.csv',
    'ciudad': DATA_DIR / 'ciudad.csv',
    'producto': DATA_DIR / 'producto.csv',
    'categoria': DATA_DIR / 'categoria.csv',
    'inventario': DATA_DIR / 'inventario.csv',
    'factura': DATA_DIR / 'factura.csv',
    'venta': DATA_DIR / 'venta.csv',
    'detalle_venta': DATA_DIR / 'detalle_venta.csv',
    'compra': DATA_DIR / 'compra.csv',
    'detalle_compra': DATA_DIR / 'detalle_compra.csv',
    'perdida': DATA_DIR / 'perdida.csv',
    'detalle_perdida': DATA_DIR / 'detalle_perdida.csv',
    'proveedor': DATA_DIR / 'proveedor.csv',
    'nota_credito': DATA_DIR / 'nota_credito.csv',
    'metodo_pago': DATA_DIR / 'metodo_pago.csv',
}

HEADERS = {
    'rol': ['id','nombre'],
    'usuario': ['id','documento','nombre','email','contrasenia','id_rol','id_sucursal'],
    'sucursal': ['id','nombre','id_ciudad'],
    'producto': ['id','codigo','nombre','precio','costo','id_categoria','fecha_creacion','id_estado'],
    'inventario': ['id','id_producto','id_sucursal','existencia'],
    'factura': ['id','numero','fecha','id_sucursal','subtotal','iva','total','id_estado'],
}