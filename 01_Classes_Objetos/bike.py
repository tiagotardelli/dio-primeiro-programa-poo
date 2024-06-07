class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor, marcha, aro = 18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha
        self.aro = aro

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicileta ...")
        print("Bicicleta parada")

    def correr(self):
        print("Vruuuunnmmmmm")

    def get_cor(self):
        return self.cor
    
    #def __str___(self):
    #    return f"Bicicleta: {self.cor} {self.modelo} {self.ano} {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def trocar_marchar(self, nro_marcha):
        print("Trocando marchar")
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha Trocada")
            else:
                print("Não foi possível trocar de marchas")

if __name__ == "__main__":
    b1 = Bicicleta("vermelha", "caloi", 2022, 600)
    b1.buzinar()
    b1.correr()
    b1.parar()
    print(b1.cor, b1.modelo, b1.ano, b1.valor)

    b2 = Bicicleta("Verde", "monark", 2000, 2202)
    Bicicleta.buzinar(b2)
    print(b2.get_cor()) # Não utilizado em Python
    print(b2)
