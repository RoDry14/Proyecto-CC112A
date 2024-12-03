import random

def generador_cont(tamaño):
    contrasena = ""
    for i in range(tamaño):
        c = chr(random.choice(range(33,127)))
        contrasena += c
    return contrasena

#Ejemplo de implementacion
cant = int(input("Cantidad de contraseñas: "))
long = int(input("Longitud de las contraseñas: "))
for _ in range(cant):
    print(generador_cont(long))