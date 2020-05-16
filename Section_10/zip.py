'''
zip() - Cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis passados
'''
lista = [1,2,3,4,5,6,7]
tupla = (1,2,3,4,5,6,7)
conjunto = {1,2,3,4,5,6,7}
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
lista2 = [10,20,30,40,50,60,70]

#Cria pares com os iteraveis
zip1 = zip(lista, lista2)
print(zip1)
print(list(zip1))

print(f'lista: {list(zip(lista, dict1))}')
print(f'set:   {set(zip(lista, conjunto))}')
print(f'tupla: {tuple(zip(tupla, dict1))}')
print(f'dict:  {dict(zip(conjunto, tupla))}')
print(f'tres listas: {list(zip(dict1, tupla, conjunto))}')

#Desenpacotando
dados = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70)]
print(list(zip(*dados)))

#Verificando a maior nota de cada aluno
prova1 = [50,45,80]
prova2 = [56,76,30]
alunos = ['Pedro', 'Maria', 'João']

final = {dado[0] : max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

#com a função map
final2 = zip(alunos, map(lambda x: max(x), zip(prova1, prova2)))
print(dict(final2))
