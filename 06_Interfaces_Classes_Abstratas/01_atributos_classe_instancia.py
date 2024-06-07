class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

if __name__ == "__main__":
    aluno_1 = Estudante("Tiago", 1)
    aluno_2 = Estudante("Giovana", 2)
    mostrar_valores(aluno_1, aluno_2)

    aluno_1.matricula = 3
    mostrar_valores(aluno_1, aluno_2)
    aluno_1.matricula = 1

    Estudante.escola = "Nova Escola"
    mostrar_valores(aluno_1, aluno_2)

    aluno_3 = Estudante("José", 3)
    aluno_3.escola = "Arararara"
    mostrar_valores(aluno_1, aluno_2, aluno_3)
