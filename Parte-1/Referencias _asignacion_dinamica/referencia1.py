#no deben usar objetos inmutables como las listas
def intercambio_var(a,b):
    a[0],b[0] = b[0],a[0]
    return

#Ejemplo de implementacion
a0 = float(input("Ingrese el valor 'a': "))
b0 = float(input("Ingrese el valor 'b': "))

a = [a0]
b = [b0]

intercambio_var(a,b)
print(f"a: {a[0]}\nb: {b[0]}")