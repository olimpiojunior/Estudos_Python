s = set({1,2,3,4,3,2,4,7,8,9,0})
#print(s)
'''Ao criar um conjunto, caso seja adicionado um valor já existente,
o mesmo sera ignorado sem gerar erro
'''

s1 = {1,2,3,4,5,4,3,5,6,7,6,6}
#print(s1)

lista = [1,2,3,4,5,4,3,4,5,6,6]
l = set(lista)
#print(l)

if 0 in l:
    print(f'tem o {l}')

tui = (1,2,3,4,5,6,)
t = set(tui)
#print(tui)

tui1 = set(tui)
#print(tui1)
'''
#imprime tudo
lista = [1,2,3,4,12,23,34,45,56,67,56,45,2,3,1,12]
print(f'Lista: {lista}, tamanho: {len(lista)}')

#imprime tudo
tupla = 1,2,3,4,12,23,34,45,56,67,56,45,2,3,1,12
print(f'Tupla: {tupla}, tamanho: {len(tupla)}')

#Não repete chave
dict = {}.fromkeys([1,2,3,4,12,23,34,45,56,67,56,45,2,3,1,12], 'dici')
print(f'Dict: {dict}, tamanho: {len(dict)}')

#Não repete valor
conjunto = {1,2,3,4,12,23,34,45,56,67,56,45,2,3,1,12}
print(f'Conjunto: {conjunto}, tamanho: {len(conjunto)}')

#podem ser de qualquer tipo
s = {1,23,3,'b', True, False, 34.5}
print(s, type(s))

cidades = ['São Paulo', 'Uberlândia', 'Uberaba', 'Araguari', 'São Paulo', 'Uberaba']
print(set(cidades))


s = {1,2,3}
s.add(4)
print(s)
s.add(5)
print(s)
s.remove(2)
print(s)
s.discard(1)
print(s)
s.remove(22) #Da erro
print(s)
s.discard(22)#Não da erro
print(s)


s = {1,2,3,4,5}
novo = s.copy()
novo.add(44)
print(s)
print(novo)

#Imprime os alunos unicos de cada lista
estudantes_python = {'marcos', 'olimpio', 'marcelo', 'patricia', 'pedro'}
estudantes_java = {'gustavo', 'joão', 'marcos', 'olimpio'}

unicos1 = estudantes_python.union(estudantes_java) #ou
unicos2 = estudantes_java | estudantes_python
print(unicos1)
print(unicos2)

#Alunos de ambos os cursos
ambos1 = estudantes_python.intersection(estudantes_java) #ou
ambos2 = estudantes_java & estudantes_python
print(ambos1)
print(ambos2)

#Estudantes que só fazem um curso
so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)
print(so_python)
print(so_java)
'''
