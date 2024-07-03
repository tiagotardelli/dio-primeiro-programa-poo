def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('faz algo depois de executar')
        return resultado

    return envelope

@meu_decorador
def ola_mundo(*args, **kwargs):
    for arg in args:
        print(arg)
    print(f"Olá mundo {kwargs['nome']}!")
    return kwargs['nome'].upper()

if __name__ == "__main__":
    resultado = ola_mundo(1, 2, nome ='João')
    print(resultado)