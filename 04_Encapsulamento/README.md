## Encapsulamento
Conceito fundamental em progrmação orientada a objetos. Ele descreve a ideia de agrupar dados e os métodos que
manipulam esses dados em uma unidade. Isso impões restrições ao acesso direto a variáveis e métodos e pode evitar
a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada
pelo método desse objeto.

## Modificadores de Acesso
Python nÃo tem uma palavra reservada, porém usamos convenções no nome do recurso, para definir se a variavel é
publica ou privada.
Público -> Só pode ser acessado de fora da classe.
Privado -> Só pode ser acessado pela classe

## Público/Privado
Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador do Python irá
garantir a proteção do recurso, mas por ser uma convençõa amplamnete adotada na comunidade, quando encontramos uma 
variável e/ou método com nome iniciado por ununderline, sabemos que não deveríamos manipular o seum valor diretamente,
ou invocar o método fora do escopo da classe.

## Propriedades
Com o property() do Pytohn, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados,
também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da 
classe.