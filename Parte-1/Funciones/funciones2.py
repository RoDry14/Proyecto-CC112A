def fibonacci_rec(n):
    if n<=2:
        return n-1
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)

#Ejemplo de implementacion para el n-simo termino
n = int(input("Ingrese la posicion: "))
n_term = fibonacci_rec(n)
print(f"El termino {n} es {n_term}")