from app.repositories.producto_repo import ProductoRepo
from app.utils import generar_uuid, ahora_str

class ProductoService:
    def __init__(self):
        self.repo = ProductoRepo()

    def crear(self, codigo, nombre, precio, costo, id_categoria='', id_estado=''):
        nuevo = {
            'id': generar_uuid(),
            'codigo': codigo,
            'nombre': nombre,
            'precio': str(precio),
            'costo': str(costo),
            'id_categoria': id_categoria,
            'fecha_creacion': ahora_str(),
            'id_estado': id_estado,
        }
        self.repo.save(nuevo)
        return nuevo

    def listar(self):
        return self.repo.all()

    def buscar(self, texto):
        return self.repo.buscar_por_texto(texto)

    def actualizar(self, id, cambios):
        return self.repo.update(id, cambios)

    def eliminar(self, id):
        return self.repo.delete(id)