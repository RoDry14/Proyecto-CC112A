import re

#usando expresiones regulares
def es_palindromo(cadena):
    cadena_aux = re.sub(r'[^a-zA-Z]',"",cadena)
    n = len(cadena_aux)
    for i in range(n//2):
        if cadena_aux[i]!=cadena_aux[-(i+1)]:
            return False
    return True

'''
def es_palindromo(cadena):
    cadena_aux = ("".join(cadena.split())).lower()
    n = len(cadena_aux)
    for i in range(n//2):
        if cadena_aux[i]!=cadena_aux[-(i+1)]:
            return False
    return True
'''

def es_palindromo_iter(cadena):
    cadena_aux = re.sub(r'[^a-zA-Z]',"",cadena)
    izq,der = 0,len(cadena_aux)-1
    while izq < der:
        if cadena_aux[izq]!=cadena_aux[der]:
            return False
        izq -= 1
        der -= 1
    return True

'''
def es_palindromo_iter(cadena):
    cadena_aux = ("".join(cadena.split())).lower
    izq,der = 0,len(cadena_aux)-1
    while izq < der:
        if cadena_aux[izq]!=cadena_aux[der]:
            return False
        izq -= 1
        der -= 1
    return True
'''

def es_palindromo_rec(cadena):
    cadena_aux = re.sub(r'[^a-zA-Z]',"",cadena)
    if len(cadena_aux)==1:
        return True
    if cadena_aux[0]!=cadena_aux[-1]:
        return False
    return es_palindromo_rec(cadena_aux[1:-1])

'''
def es_palindromo_rec(cadena):
    cadena_aux = ("".join(cadena.split())).lower
    if len(cadena_aux)==1:
        return True
    if cadena_aux[0]!=cadena_aux[-1]:
        return False
    return es_palindromo_rec(cadena_aux[1:-1])
'''

#Ejemplo de implementacion
cadena = input("Ingrese una cadena: ")
print(f"1. {es_palindromo(cadena)}")
print(f"2. {es_palindromo_iter(cadena)}")
print(f"3. {es_palindromo_rec(cadena)}")