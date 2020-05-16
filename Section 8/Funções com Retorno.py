'''
Funções com retorno
Quando uma fução não retorna nenhum valor, ela retornara None
Para retornar um resultado, utiliza-se a palavra return
podemos ter em uma função diferentes returns

------------------------------------------------------
num = [1,2,3,4]
ret_pop = num.pop()
ret_pr = print(num)

print(f'Retorno de pop: {ret_pop}')
print(f'Retorno de print: {ret_pr}')
------------------------------------------------------
def quadrado(x):
    return x**2

req = quadrado(4)
print(req)

print(f'retorno: {quadrado(6)}')

------------------------------------------------------
def new_function():
    val = False
    if val:
        return 'val é True'
    elif val == None:
        return 'val é Nnone'
    return 'graça'

print(new_function())
'''
from random import random

#A função random retorna valores randomicos entre 0 e 1
def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())