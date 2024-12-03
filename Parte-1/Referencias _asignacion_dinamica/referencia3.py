def crear_matriz(m,n):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(n):
            elem = float(input(f"Ingrese el elemento {i+1},{j+1}: "))
            fila.append(elem)
        matriz.append(fila)
    return matriz    

#Ejemplo de implementacion
m = int(input("Filas: "))
n = int(input("Columnas: "))
matriz = crear_matriz(m,n)
for fila in matriz:
    print(fila)
