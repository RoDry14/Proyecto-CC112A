def calcular_pal1(cadena):
    n=len(cadena)
    cont = 0
    for i in range(n):
        if cadena[i].isspace():
            continue
        if cadena[i-1].isspace() or i==0:
            cont +=1
    return cont  

def calcular_pal2(cadena):
    en_palabra = False
    cont = 0
    for c in cadena:
        if c.isspace():
            en_palabra = False
            continue
        if not en_palabra:
            en_palabra = True
            cont += 1
    return cont

#split() es similar a strtok() de C++
def calcular_pal3(cadena):
    lista_aux = cadena.split()
    return len(lista_aux)        
    

#Ejemplo de implementacion
cadena = input("Ingrese una cadena: ")
print(f"1. Hay {calcular_pal1(cadena)} palabras")
print(f"2. Hay {calcular_pal2(cadena)} palabras")
print(f"3. Hay {calcular_pal3(cadena)} palabras")
            
        