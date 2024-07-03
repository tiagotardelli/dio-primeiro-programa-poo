import functools

def meu_decorador(funcao):
    @functools.wraps(funcao) ## acrescentado para que no __name__ ele apareça o nome da função
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('faz algo depois de executar')
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()

if __name__ == "__main__":
    resultado = ola_mundo('João')
    print(resultado)
    print(ola_mundo.__name__)