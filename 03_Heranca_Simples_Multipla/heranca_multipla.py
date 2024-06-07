class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw) :
         self.cor_bico = cor_bico
         super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Oi estou falando"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico
                         , numero_patas=numero_patas)

if __name__ == "__main__":
    gato = Gato(numero_patas=4, cor_pelo="preto")
    print(gato)

    ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="Marrom",cor_bico="Laranja")
    print(ornitorrinco)
    print(ornitorrinco.falar())