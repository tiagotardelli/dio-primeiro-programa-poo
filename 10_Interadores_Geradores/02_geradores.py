# Usar com iteradores simples
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2 

if __name__ == "__main__":
    for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
        print(i)
