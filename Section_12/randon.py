'''
O módulo Random

import random
for i in range(10):
    print(random.random())

#Forma correta de importar uma funão específico
from random import random
for a in range(16):
    print(random())

#Gerando números aleatórios com a função uniform()
from random import uniform
for i in range(10):
    print(uniform(3,5)) #Limite superior não é incluido

#Gerando valores Reais com a função randint()
from random import randint
for i in range(6):
    print(randint(1, 60), end = ', ')

#Gerando valor aleatório em um conjunto com a função choice()
from random import choice
jogadas = ['Pedra', 'Papel', 'Tesoura']

jogador_1 = choice(jogadas)
jogador_2 = choice(jogadas)

print(f'Jogador 1: {jogador_1}')
print(f'Jogador 2: {jogador_2}')

if jogador_1 == jogadas[0] and jogador_2 == jogadas[1]:
    print('Jogador 2 venceu')
elif jogador_1 == jogadas[0] and jogador_2 == jogadas[2]:
    print('Jogador 1 venceu')
elif jogador_1 == jogadas[1] and jogador_2 == jogadas[0]:
    print('Jogador 1 venceu')
elif jogador_1 == jogadas[1] and jogador_2 == jogadas[2]:
    print('Jogador 2 venceu')
elif jogador_1 == jogadas[2] and jogador_2 == jogadas[0]:
    print('Jogador 2 venceu')
elif jogador_1 == jogadas[2] and jogador_2 == jogadas[1]:
    print('Jogador 1 venceu')
else:
    print('Empate')

#Jogando uma moeda
escolha = input('Voce quer Cara ou Coroa? ')
moeda = ['Cara', 'Coroa']
result = choice(moeda)
print(f'E o valor da moeda foi.......: {result}')
if escolha.title() == result:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
'''
#Embaralhando valores com a função shuffle()
from random import shuffle
cartas = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(cartas)
shuffle(cartas)
print(cartas)




