## Recapitulando
Funções em Python são objetos de primeira classe. Isso significa que as funções podem ser passadas
e usadas como argumentos.
```python
def dizer_oi(nome):
    return f"Oi {nome}"
    
def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"
    
def mensagem_para _guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")

    mensagem_para_guilherme(dizer_oi)
    mensagem_para_guilherme(incentivar_aprender)

$ python decoradores.py
>>>Oi Guilherme
>>>Oi Guilherme, vamos aprender Python juntos!
```
Funções em Python são objetos de primeira classe. Minha função é um objeto, assim condigo
passar ela para outras funções

## Inner functions
É possível definir funções dentro de outras funções. Tais funções são chamadas de funções
internas.
```python
def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")
    
    def filho2():
        print("Escrevendo da filho2() função")
    
    filho2()
    filho1()
pai()
$ python decoradores.py
>>Escrevendo da pai() função
>>>Escrevendo da filho2() função
>>>Escrevendo da filho1() função
```

## Retornar funções de funções
Python também permite que você use funções como valores de retorno
```python
def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    if operacao == "+":
        return somar
    else:
        return subtrair
resultado = calcular("+")(1, 3)
print(resultado)
```

## Decorador simples
Decoro uma funcao chamando meu decorador com a função que quero e retorno para ela mesma
```python
def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar')
        funcao()
        print('faz algo depois de executar')

    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
```

## Açucar Suntático!
o Python permite que você use decoradores de maneira mais simples com o símbolo @
```python
def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar')
        funcao()
        print('faz algo depois de executar')

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

ola_mundo
```

## Funções de decoração com argumentos
Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número
árbitrário de argumentos posicionais e de palavras-chave
```python
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")        

aprender("Python")
```

## Retornando valores de funções decoradas
O decorador pode decidir se retorna o valor da função decorada ou não.
Para que o valor seja retornado a função de envelope deve retornar o valor
da função decorada.
```python
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()        

tecnologia = aprender("Python")
print(tecnologia)
```

## Instropecção
Instrospecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo
de execução.
```python
import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()        

tecnologia = aprender("Python")
print(tecnologia)
```