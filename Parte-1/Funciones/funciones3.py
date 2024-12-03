def hanoi(n,origen,auxiliar,destino):
    #caso base
    if n==1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    #movemos los n-1 discos a auxiliar
    hanoi(n-1,origen,destino,auxiliar) 
    print(f"Mover disco {n} de {origen} a {destino} ")
    #movemos finalmente los n-1 discos a destino
    hanoi(n-1,auxiliar,origen,destino)
    
#Ejemplo de implementacion con n discos
n = int(input("Ingrese el numero de discos: "))
hanoi(n,"Origen","Auxiliar","Destino")