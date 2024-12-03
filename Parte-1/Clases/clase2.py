class Cuenta_Banc:
    def __init__(self):
        self.__titular = input("Ingresa el nombre del titular: ")
        self.__saldo = 0 
        self._id = id(self)
    def depositar(self,monto):
        self.__saldo += monto
    def retirar(self,monto):
        if monto>self.__saldo:
            print(f"No dispone de {monto} actualmente. (Saldo: {self.__saldo})")
        else:
            self.__saldo -= monto
    def mostrar(self):
        print(f"El titular es {self.__titular}")
        print(f"Saldo: {self.__saldo}")

#Ejemplo de implementacion
cuenta_1 = Cuenta_Banc()
cuenta_1.depositar(100)
cuenta_1.mostrar()
cuenta_1.retirar(120)
cuenta_1.mostrar()

        