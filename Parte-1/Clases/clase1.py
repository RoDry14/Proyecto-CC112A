class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")

#Ejemplo de implementacion
lista = input("Ingrese los datos (nombre,edad): ").split()
persona = Persona(lista[0],lista[1])
persona.mostrar()