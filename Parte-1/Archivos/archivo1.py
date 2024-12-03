def escribir_arch(nombre_arch):
    file = open(nombre_arch,"w")
    texto = input("Ingrese el texto: ")
    file.write(texto)
    file.close()
    
'''
def escribir_arch(nombre_arch):
    with open(nombre_arch,"w") as file:
        texto = input("Ingrese el texto: ")
        file.write(texto)
'''

def leer_arch(nombre_arch):
    file = open(nombre_arch,"r")
    contenido = file.read()
    file.close()
    print(contenido)

'''
def leer_arch(nombre_arch):
    with open(nombre_arch,"r") as file:
       contenido = file.read()
    print(contenido) 
'''

if __name__=="__main__":
    #Ejemplo de implementacion
    escribir_arch("archivo.txt")
    leer_arch("archivo.txt")