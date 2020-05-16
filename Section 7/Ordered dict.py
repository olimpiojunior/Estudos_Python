'''
Módulo Colletion - Ordered dict
Dicionário comum não garante a ordem dos pares chave:valor
O Ordered dict é usado quando essa ordem é requerida
'''
from collections import OrderedDict

dict1 = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
print(dict1['c'])
print(dict1)
for k,v in dict1.items():
    print(f'Chave: {k}, valor: {v}')
