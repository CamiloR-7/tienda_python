from repositories.base_repo import BaseRepo
from config import HEADERS

class SucursalRepo(BaseRepo):
    def __init__(self):
        super().__init__('sucursal', HEADERS['sucursal'])