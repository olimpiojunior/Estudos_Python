'''
Any & All

all() - Retorna True, se todos os elementos do iteravel são verdadeiros ou se o iteravel esta vazio
'''

print(all([0,1,2,3,4]), 'all') #False - por causa do 0

print(all([1,2,3,4,5,6,7]), 'all') #True - por todos são verdadeiros

print(all([]), 'all vazio') #True - pq esta vazia

print(all((1,2,3,4,5)), 'all') #True - para tuple

print(all({1,2,3,4,5,6}), 'all') #True - para set

print(all('olimpio'), 'all') #True

nomes = ['Camila', 'Cassio', 'Carla', 'Carlos']

print(all([nome[0] == 'C' for nome in nomes]), 'all')

print(all([i>20 for i in range(1,10)]), 'all')

print(all([x for x in [2,4,6,8,10] if x%2 == 0]), 'all')

'''
any() - Retorna verdadeiro se algum elemento do iteravel for verdadeiro, ou False se estiver vazio
'''
print(any([0,1,2,3,4]), 'any') #False - por causa do 0

print(any([1,2,3,4,5,6,7]), 'any') #True - por todos são verdadeiros

print(any([]), 'any vazio') #True - pq esta vazia

print(any((1,2,3,4,5)), 'any') #True - para tuple

print(any({1,2,3,4,5,6}), 'any') #True - para set

print(any('olimpio'), 'any') #True

nomes = ['Camila', 'Cassio', 'Carla', 'Carlos']

print(any([nome[0] == 'C' for nome in nomes]), 'any')

print(any([i>20 for i in range(1,10)]), 'any')

print(any([x for x in [2,4,6,8,10] if x%2 == 0]), 'any')