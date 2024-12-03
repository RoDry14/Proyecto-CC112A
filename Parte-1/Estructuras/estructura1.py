from collections import namedtuple
Punto = namedtuple("Punto",["x","y"])
def distancia_punt(p1,p2):
    return ((p2.x-p1.x)**2+(p2.y-p1.y)**2)**0.5

#Ejemplo de implementacion
lista = input("Coordenadas (x,y) de p1: ").split()
x,y = int(lista[0]),int(lista[1])
p1 = Punto(x,y)
lista = input("Coordenadas (x,y) de p2: ").split()
x,y = int(lista[0]),int(lista[1])
p2 = Punto(x,y)
print(f"Distancia: {distancia_punt(p1,p2)}")