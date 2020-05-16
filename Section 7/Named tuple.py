'''
Módulo Colletions - Named tuple
São tuplas diferenciadas onde especificamos um nome para a mesma e também parametros
'''
from collections import namedtuple

#Define nome e parametro
cachorro = namedtuple('cachorro', 'idade raca nome') #ou
cachorro = namedtuple('cachorro', 'idade, raca, nome') #ou
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=12, raca='chow-chow', nome = 'Ray')
rick = cachorro(12, 'vira-lata', 'Rick')
print(ray)
print(rick)

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(rick[0])
print(rick[1])
print(rick[2])
