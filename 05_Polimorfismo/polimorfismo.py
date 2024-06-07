class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

#FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ....")

    def plano_voo(obj):
        obj.voar()

if __name__ == "__main__":
    plano_de_voo(Pardal())
    plano_de_voo(Avestruz())
    print(Aviao())