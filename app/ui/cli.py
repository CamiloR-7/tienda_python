from app.services.auth_service import AuthService
from app.services.producto_service import ProductoService
from app.services.inventario_service import InventarioService
from app.services.factura_service import FacturaService
from app.repositories.producto_repo import ProductoRepo

class CLI:
    def __init__(self):
        self.auth = AuthService()
        self.prod_s = ProductoService()
        self.inv_s = InventarioService()
        self.fact_s = FacturaService()
        self.usuario = None

    def inicio(self):
        while True:
            print('\n--- TIENDA COQUITO AMARILLO ---')
            print('1) Login')
            print('2) Salir')
            opc = input('> ')
            if opc == '1':
                self.login()
            else:
                print('Saliendo')
                break

    def login(self):
        email = input('Email: ')
        contrasenia = input('Contraseña: ')
        usuario, err = self.auth.login(email, contrasenia)
        if err:
            print('Error:', err)
            return
        self.usuario = usuario
        if usuario.get('id_rol') == 'admin':
            self.menu_admin()
        else:
            self.menu_empleado()

    def menu_admin(self):
        while True:
            print('\n--- ADMIN ---')
            print('1) Usuarios')
            print('2) Sucursales')
            print('3) Productos')
            print('4) Inventario')
            print('5) Cerrar sesión')
            opc = input('> ')
            if opc == '1':
                self.menu_usuarios()
            elif opc == '3':
                self.menu_productos()
            elif opc == '4':
                self.menu_inventario()
            elif opc == '5':
                self.usuario = None
                break
            else:
                print('Opción no implementada')

    def menu_empleado(self):
        while True:
            print('\n--- EMPLEADO ---')
            print('1) Vender')
            print('2) Devolver (nota crédito)')
            print('3) Cerrar sesión')
            opc = input('> ')
            if opc == '1':
                self.vender()
            elif opc == '2':
                print('Funcionalidad devolución (nota crédito) pendiente')
            elif opc == '3':
                self.usuario = None
                break
            else:
                print('Opción inválida')

    # Admin - usuarios
    def menu_usuarios(self):
        while True:
            print('\n--- USUARIOS ---')
            print('1) Crear')
            print('2) Listar')
            print('3) Actualizar')
            print('4) Eliminar')
            print('5) Volver')
            opc = input('> ')
            if opc == '1':
                doc = input('Documento: ')
                nombre = input('Nombre: ')
                email = input('Email: ')
                contr = input('Contraseña: ')
                rol = input('Rol (admin/empleado): ')
                suc = ''
                if rol != 'admin':
                    suc = input('Id sucursal asignada: ')
                u, err = self.auth.crear_usuario(doc, nombre, email, contr, rol, suc)
                if err:
                    print('Error:', err)
                else:
                    print('Usuario creado:', u)
            elif opc == '2':
                for u in self.auth.listar():
                    print(u)
            elif opc == '3':
                idu = input('Id usuario: ')
                nombre = input('Nuevo nombre (enter=omitir): ')
                cambios = {}
                if nombre:
                    cambios['nombre'] = nombre
                if cambios:
                    ok = self.auth.actualizar(idu, cambios)
                    print('Actualizado' if ok else 'No existe')
            elif opc == '4':
                idu = input('Id a eliminar: ')
                ok = self.auth.eliminar(idu)
                print('Eliminado' if ok else 'No existe')
            else:
                break

    # Admin - productos
    def menu_productos(self):
        while True:
            print('\n--- PRODUCTOS ---')
            print('1) Crear')
            print('2) Listar')
            print('3) Buscar/Filtrar')
            print('4) Actualizar')
            print('5) Eliminar')
            print('6) Volver')
            opc = input('> ')
            if opc == '1':
                codigo = input('Código (SKU): ')
                nombre = input('Nombre: ')
                precio = input('Precio: ')
                costo = input('Costo: ')
                p = self.prod_s.crear(codigo, nombre, precio, costo)
                print('Creado:', p)
            elif opc == '2':
                for p in self.prod_s.listar():
                    print(p)
            elif opc == '3':
                texto = input('Texto búsqueda: ')
                for p in self.prod_s.buscar(texto):
                    print(p)
            elif opc == '4':
                idp = input('Id producto: ')
                nombre = input('Nuevo nombre (enter=omitir): ')
                cambios = {}
                if nombre:
                    cambios['nombre'] = nombre
                if cambios:
                    ok = self.prod_s.actualizar(idp, cambios)
                    print('Actualizado' if ok else 'No existe')
            elif opc == '5':
                idp = input('Id a eliminar: ')
                ok = self.prod_s.eliminar(idp)
                print('Eliminado' if ok else 'No existe')
            else:
                break

    # Admin - inventario
    def menu_inventario(self):
        while True:
            print('\n--- INVENTARIO ---')
            print('1) Ajuste')
            print('2) Ver existencia')
            print('3) Volver')
            opc = input('> ')
            if opc == '1':
                idp = input('Id producto: ')
                ids = input('Id sucursal: ')
                delta = input('Delta (ej: -2 o 5): ')
                ok, err = self.inv_s.ajustar(idp, ids, int(delta))
                if not ok:
                    print('Error:', err)
                else:
                    print('Ajuste realizado')
            elif opc == '2':
                idp = input('Id producto: ')
                ids = input('Id sucursal: ')
                print('Existencia:', self.inv_s.existencia(idp, ids))
            else:
                break

    # Empleado - vender
    def vender(self):
        idp = input('Id producto a vender: ')
        ids = self.usuario.get('id_sucursal')
        cantidad = int(input('Cantidad: '))
        existencia = self.inv_s.existencia(idp, ids)
        if existencia < cantidad:
            print('Stock insuficiente:', existencia)
            return
        pr = ProductoRepo()
        producto = pr.find_by_id(idp)
        if not producto:
            print('Producto no existe')
            return
        precio = float(producto.get('precio'))
        subtotal = precio * cantidad
        factura = self.fact_s.crear(ids, subtotal)
        ok, err = self.inv_s.ajustar(idp, ids, -cantidad)
        if not ok:
            print('No se pudo ajustar inventario:', err)
            return
        print('Venta registrada. Factura:', factura['numero'])