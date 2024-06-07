## Métodos de Classe
Estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para
a classe e não para instância do objeto.

## Métodos Estáticos
Não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este
método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe poeque faz sentido que o 
método esteja presente na classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em
uma classe porque faz sentido que o método esteja presente na classe.

## Método de Classe X Métodos Estáticos
* Um método de classe recebe um primeiro parâmtero que aponta para a classe, enquanto um método estático não.
* Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou
  modificá-lo.

## Quando Utilizar Método de Classe ou Estático
* Geralmente usamos o método de classe para criar métodos de fábrica (retornam instâncias).
* Geralmente usamos métodos estáticos para criar funções utilitárias (Ex.: Pessoa maior de idade?).