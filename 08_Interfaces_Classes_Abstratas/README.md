## O que são Interfaces?
IMPORTANTE! -> Interfaces definem o que uma classe deve fazer e não como.
Ex.: Uma lapiséria tem como padrão colocar grafite e ter um botão para soltar a gravite

## Python tem interface?
P conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas
assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas.

## ABC
Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as
classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, em
seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado
com @abstractmethod.
