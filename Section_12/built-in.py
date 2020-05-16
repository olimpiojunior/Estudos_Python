'''
Módulos Buit-in. são módulos que já vem instalados no python
'''
#utilizando alias (apelidos) para módulos/função
import random as junior
print(junior.randint(0, 10))

#importando todas as funções de um módulo com *
from random import *
print(random())

#apelidando a função
from random import random as eita, randint as olimpio
print(eita())
print(olimpio(1,5))

#usando tuple para multiplos imports
from random import (
    random,
    choice,
    randint,
    shuffle
)
print(60*'-')
cartas = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(random())
print(choice('olimpio'))
print(randint(1,80))
shuffle(cartas)
print(cartas)
