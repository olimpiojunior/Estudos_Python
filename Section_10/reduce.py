'''
Reduce
Obs: A partir do Python 3+ a função reduce não é mais uma função Built in. Agora temos que importar a partir do módulo 'funtools'

A função reduce recebe dois parametros, a função e o iterável - reduce(função, dados)
'''
from functools import reduce
#Usando função
def soma(x,y):
    return x+y

l = [1,2,3,4,5,6,7]

print(reduce(soma, l))

#Usando lambda
mult = lambda x,y: x*y

print(reduce(mult,l))

#Usando for
n = 0
for i in l:
    n += i

print(n)