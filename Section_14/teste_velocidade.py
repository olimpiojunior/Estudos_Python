'''
Teste de velocidade
'''

#Generator
def num():
    for i in range(10):
        yield i

n = num()
print(n)
print(next(n), next(n))

#Generator express
ge2 = (num for num in range(10))
print(ge2)
print(next(ge2), next(ge2))

print(sum(num for num in ge2))

#Realizando teste de velocidade
import time
#Generator express
gen_inicio = time.time()
print(sum(num for num in range(10000000)))
gen_tempo = time.time() - gen_inicio

#list comprehension
list_inicio = time.time()
print(sum(num for num in range(10000000)))
list_tempo = time.time() - list_inicio

print(f'Generator express levou: {gen_tempo}')
print(f'List comprehension levou: {list_tempo}')

#list comprehension levou menos tempo em todos os testes!