"""
POO - Classe -> Modelos dos objetos do mundo real sendo representados computacionalmente

Classes podem conter atributos:
    -Atributos: Representam as caracteristicas dos objetos. Ou seja, pelos atributos
    conseguimos computacionalmente os estados de um objeto. No caso da lampada, poderia
    ser a potência, cor, luminosidade e etc..

    -Métodos: Funções que representam os comportamenos do objeto, ou seja, as ações que
    o objeto pode realizar em um sistema. No caso da lampada, por exemplo, um comportamento
    comum seria de ligar ou desligar a lâmpada.

Obs: Utilizamos a palavra reservada pass, quando temos um bloco de código que ainda não está
implementado.
Obs: Por convenção, as classes criadas por usuários devem ser CamelCase, visto que as classes
internas criadas por desenvolvedores são iniciadas por letras minúsculas
Obs: Quando estamos planejando um software definimos quais classes teremos que ter no sistema,
chamamos esses objetos que serão mapeados para a classe de entidades.
"""


# Exemplo: Criando uma lampada em Python


class Lampada:
    pass


lamp = Lampada()
print(lamp)  # Objeto do tipo lampada
