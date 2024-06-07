class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("auau")

    def __del__(self):
        print("Removendo instância da classe.")


if __name__ == "__main__":

    def criar_cachorro():
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)

    c = Cachorro("Chappie", "amarelo")
    c.falar()

    print("Ola mundo")
    del c
    print("Ola Mundo")

    criar_cachorro()