from abc import ABC,abstractmethod
import random

class Player(ABC):
    def __init__(self,name):
        self.name = name
        self.election = None
        self.points = 0
    @abstractmethod
    def choose(self):
        pass
    def wins(self):
        self.points += 1
        print(f"  {self.name} gana la ronda")
        
class Player1(Player):
    def __init__(self,name="Jugador1"):
        super().__init__(name)
    def choose(self,options):
        while(True):
            election = input("Ingrese su eleccion: ").replace(" ","").lower()
            if election in options:
                self.election = election
                return
            print(f"Ingrese una opcion valida {options}")
                
class Player2(Player):
    def __init__(self,name="Jugador2"):
        super().__init__(name)
    def choose(self,options):
        self.election = random.choice(options)
        print(f"La computadora eligio {self.election}")


class Round:
    def __init__(self,player1,player2,options,rules):
        self.winner = None
        self.rules = rules
        self.options = options
        self.player1 = player1
        self.player2 = player2
    def printresult(self):
       print(f"    Jugador1: {self.player1.points} puntos \n    Jugador2: {self.player2.points} puntos")
       print("-"*27)
    def start(self):
        while self.winner is None:
            self.player1.choose(self.options)
            self.player2.choose(self.options)
            if self.player1.election == self.player2.election:
                self.winner = None
                print("      Es un empate")
                self.printresult()
                continue
            if (self.player1.election,self.player2.election)  in self.rules:
                self.player1.wins()
                self.winner = self.player1
            else:
                self.player2.wins()
                self.winner = self.player2
            self.printresult()    
    
class Game:
    def __init__(self,ptswin,player1,player2):
         self.ptswin = ptswin
         self.winner = None
         self.player1 = player1
         self.player2 = player2
    def start(self,options,rules):
        while self.winner is None:
            round = Round(self.player1,self.player2,options,rules)
            round.start()
            if round.winner.points == self.ptswin:
                self.winner = round.winner
    def printresult(self):
        if self.winner.name is self.player1.name:
            print("Ganaste!")
        else:
            print("Perdiste")
            

if __name__ == '__main__' :
    
    options = ("piedra","papel","tijera")
    rules = (("piedra","tijera"),("papel","piedra"),("tijera","papel"))
    
    player1 = Player1()
    player2 = Player2()
    
    print("-"*27)
    game = Game(3,player1,player2)
    game.start(options,rules)
    game.printresult()