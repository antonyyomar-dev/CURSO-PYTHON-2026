# inventario
class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre 
        self.categoria = categoria
        self.precio = precio 
        self.stock = stock
        
    def mostrar_producto(self):
        print("INFORMACIÓN SOBRE EL PRODUCTO:")
        print("Codigo   : ", self.codigo)
        print("Nombre   : ", self.nombre)
        print("Categoria: ", self.categoria)
        print("Precio   : ", self.precio)
        print("Stock    : ", self.stock)
        
    
class Gestora:
    def __init__(self):
        self.lista_productos = []
    
    
    def registrar_producto(self):
        codigo = input("Ingrese el codigo del producto (4 digitos numericos): ")
        nombre = input("Ingrese el nombre del producto: ").title()
        categoria = input("Ingrese la categoria: ").title()
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock del producto: "))
        
        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.lista_productos.append(producto)
        
        print()
        print("Producto registrado con exito")
        print()
    
    def buscar_producto (self):
        codigo = input("Ingrese el codigo del producto a buscar (4 digitos numericos): ")
        print()
        print("--"*20)
        for p in self.lista_productos:
            if p.codigo == codigo:
                p.mostrar_producto()
        print("--"*20)
    
    def eliminar_producto(self):
        codigo = input("Ingrese el codigo del producto a eliminar (4 digitos numericos): ")
        for p in self.lista_productos:
            if p.codigo == codigo:
                self.lista_productos.remove(p)
                print("El producto con ID ", codigo, " ha sido eliminado")
    
    def imprimir_productos(self):
        if len(self.lista_productos) == 0:
            print("No hay productos registrados")
        else:
            print("--"*20)
            for p in self.lista_productos:
                p.mostrar_producto()
                print("--"*20)
                print()


def menu():
    print("MENU PRINCIPAL")
    print("1. Registrar producto")
    print("2. Buscar producto por ID")
    print("3. Eliminar producto")
    print("4. Mostrar productos registrados")
    print("5. Salir")


# programa principal 

def main():
    g = Gestora()

    while True:
        while True:
            try:
                menu()
                opcion = int(input("Ingrese una opcion: "))
                if 1<= opcion <= 5:
                    break 
                else:
                    print("La opcion esta fuera de rango")
            except ValueError:
                print("Error en el ingreso de datos")
        
        if opcion == 5:
            print("Saliendo del sistema .....")
            break 
        
        if opcion == 1:
            g.registrar_producto()
        
        if opcion == 2:
            g.buscar_producto()
            
        
        if opcion == 3:
            g.eliminar_producto()
        
        if opcion == 4:
            g.imprimir_productos()
        

main()
        