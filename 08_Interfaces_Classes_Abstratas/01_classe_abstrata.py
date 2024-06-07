from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Liganda")
    
    def desligar(self):
        print("Desligando a TV...")
        print("Desligando!")
    
    @property
    def marca(self):
        return "Philco"
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a Ar Condicionado...")
        print("Liganda")
    
    def desligar(self):
        print("Desligando a Ar Condicionado...")
        print("Desligando!")
    
    @property
    def marca(self):
        return "LG"

if __name__ == "__main__":

    controle = ControleTV()
    controle.ligar()
    controle.desligar()

    controle2 = ControleArCondicionado()
    controle2.ligar()
    controle2.desligar()
