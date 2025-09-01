from repositories.base_repo import BaseRepo
from config import HEADERS

class ProductoRepo(BaseRepo):
    def __init__(self):
        super().__init__('producto', HEADERS['producto'])

    def buscar_por_texto(self, texto):
        texto = texto.lower()
        return [p for p in self.all() if texto in p.get('nombre','').lower() or texto in p.get('codigo','').lower()]