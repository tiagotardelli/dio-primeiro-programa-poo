def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        funcao(*args, **kwargs)
        print('faz algo depois de executar')

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")        

if __name__ == "__main__":
    ola_mundo('João')
