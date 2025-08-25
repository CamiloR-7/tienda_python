from app.repositories.base_repo import BaseRepo
from app.config import HEADERS

class UsuarioRepo(BaseRepo):
    def __init__(self):
        super().__init__('usuario', HEADERS['usuario'])

    def find_by_email(self, email):
        for u in self.all():
            if u.get('email') == email:
                return u
        return None