def invertir_cad1(cadena):
    i = len(cadena) - 1
    cadena_inv = ""
    while i>=0:
        cadena_inv += cadena[i]
        i -= 1
    return cadena_inv

#usando indices negativos
def invertir_cad2(cadena):
    n = len(cadena)
    cadena_inv = ""
    for i in range(n-1,-1,-1):
        cadena_inv += cadena[i]
    return cadena_inv

def invertir_cad3(cadena):
    n = len(cadena)
    cadena_inv = ""
    for i in range(1,n+1):
        cadena_inv += cadena[-i]
    return cadena_inv

#usando slicing
def invertir_cad4(cadena):
    return cadena[ : :-1]

#Ejemplo de implementacion
cadena = input("Ingrese una cadena: ")
print(f"1. {invertir_cad1(cadena)}")
print(f"2. {invertir_cad2(cadena)}")
print(f"3. {invertir_cad3(cadena)}")
print(f"4. {invertir_cad4(cadena)}")
