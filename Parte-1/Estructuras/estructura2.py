from dataclasses import dataclass,field

@dataclass
class Estudiante:
    __nombre: str = field(default="No hay informacion")
    __edad: int = field(default=-1)
    __promedio: float = field(default=-1)
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Promedio: {self.__promedio}")
        
#Ejemplo de implementacion
lista = input("Ingrese los datos (nombre,edad,promedio): ").split()
nombre,edad,promedio = lista[0],lista[1],lista[2]
estudiante = Estudiante(nombre,edad,promedio)
estudiante.mostrar()