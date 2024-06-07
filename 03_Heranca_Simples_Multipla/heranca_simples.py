class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregando")

if __name__ == "__main__":
    moto = Motocicleta("preta", "abc-1234", 2)
    caminhao = Caminhao("roxo", "abc-1134", 4, True)
    carro = Carro("vermelgo", "abc-1234", 8)
    
    print(moto)
    print(caminhao)
    print(carro)
    
    moto.ligar_motor()
    caminhao.ligar_motor()
    carro.ligar_motor()

    caminhao.esta_carregado()
