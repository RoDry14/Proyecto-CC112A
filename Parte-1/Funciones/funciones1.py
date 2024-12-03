def factorial_rec(n):
    #caso base
    if n==0:
        return 1
    return n*factorial_rec(n-1)

#Ejemplo de implementacion para n!
n = int(input("Ingrese el numero: "))
fact = factorial_rec(n)
print(f"El factorial de {n} es {fact}")