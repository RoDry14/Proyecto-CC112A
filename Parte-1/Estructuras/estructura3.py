from dataclasses import dataclass,field

@dataclass
class Producto:
    __nombre: str = field(default="Sin registro")
    __precio: float = field(default=-1)
    __cantidad: int = field(default=-1)
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.__cantidad}")
                
#Ejemplo de implementacion
lista = input("Ingrese la informacion (nombre,precio,cantidad): ").split()
nombre,precio,cantidad = lista[0],lista[1],lista[2]
producto = Producto(nombre,precio,cantidad)
producto.mostrar()