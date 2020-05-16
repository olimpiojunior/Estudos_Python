'''
Modulos Collections - Default Dict
Ao criar o dicionário, nós informamos um valor default
Se tentar acessar uma chave que não existe, a mesma será criada
'''
from collections import defaultdict

dict1 = defaultdict(lambda: 0)
dict1['curso'] = 'Python'
print(dict1['outro'])

print(dict1)