from archivo1 import leer_arch

def agregar_text_arch(nombre_arch):
    file = open(nombre_arch,"a")
    texto = input("Ingrese el texto: ")
    file.write(texto)
    file.close()
    
'''
def escribir_arch(nombre_arch):
    with open(nombre_arch,"a") as file:
        texto = input("Ingrese el texto: ")
        file.write(texto)
'''

#Ejemplo de implementacion
agregar_text_arch("archivo.txt")
leer_arch("archivo.txt")