def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar')
        funcao()
        print('faz algo depois de executar')

    return envelope

def ola_mundo():
    print("Olá mundo!")        

if __name__ == "__main__":
    ola_mundo = meu_decorador(ola_mundo)
    ola_mundo()