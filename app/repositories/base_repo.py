from utils import leer_csv, escribir_csv, append_csv

class BaseRepo:
    def __init__(self, tabla, campos):
        self.tabla = tabla
        self.campos = campos

    def all(self):
        return leer_csv(self.tabla)

    def find_by_id(self, id):
        for r in self.all():
            if r.get('id') == id:
                return r
        return None

    def filter(self, **kwargs):
        registros = self.all()
        for k, v in kwargs.items():
            registros = [r for r in registros if r.get(k) == v]
        return registros

    def save(self, registro):
        append_csv(self.tabla, registro)

    def update(self, id, cambios):
        registros = self.all()
        modificado = False
        for r in registros:
            if r.get('id') == id:
                r.update(cambios)
                modificado = True
        if modificado:
            escribir_csv(self.tabla, registros)
        return modificado

    def delete(self, id):
        registros = self.all()
        nuevos = [r for r in registros if r.get('id') != id]
        if len(nuevos) != len(registros):
            escribir_csv(self.tabla, nuevos)
            return True
        return False