'''
Generators
A diferença entre entre Generator e List comprehension é que o generator usa menos espaço de memória
'''
from sys import getsizeof

nomes = ['Camila', 'Cassio', 'Carla', 'Carlos']

print(any(nome[0] == 'C' for nome in nomes))

#List Comprehesion
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

#Generators
gen = (nome[0] == 'C' for nome in nomes)
print(type(gen))

#Função que retorna a qtd de memória que cada objeto esta ocupando

print(f'O tamanho do nome Olimpio: {getsizeof("Olimpio")} bytes')
print(f'O tamanho do numero 6 é: {getsizeof(6)} bytes')


#Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x*10 for x in range(100)])

#Gerando um set de numeros com list comprehension
set_comp = getsizeof({x*10 for x in range(100)})

#Gerando um dict de numeros com list comprehension
dict_comp = getsizeof({x: x*10 for x in range(100)})

#Gerando uma lista de numeros com list comprehension
gen_comp = getsizeof(x*10 for x in range(100))

print('Para fazer a mesma tarefa, utilizamos as seguintes memorias:')
print(f'list comprehension: {list_comp} bytes')
print(f'set comprehension: {set_comp} bytes')
print(f'dict comprehension: {dict_comp} bytes')
print(f'generate comprehension: {gen_comp} bytes')

#Também é possivel iterar em um generate
gen1 = (x*10 for x in range(100, 200) if x%2==0)

for i in gen1:
    print(i)