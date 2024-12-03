def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma
    
#Ejemplo de implementacion
numero_elem = int(input("Ingrese el numero de elementos: "))
lista = []
for i in range(numero_elem):
    elem = float(input(f"Ingrese el elemento {i+1}: "))
    lista.append(elem)
print(f"La suma de elementos es {suma_lista(lista)}")