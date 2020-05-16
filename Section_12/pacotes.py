'''
Pacotes - É um diretório contendo uma coleção de módulos;
módulos -> É apenas um arquivo python que pode ter diversas funções;
'''

#Importando funções que estão dentro de pacotes
from Section_10 import map
print(map.c_para_f)

from Section_9 import dict_comprehension
print(dict_comprehension.quadrado)

from Section_9.list_comprehension_p1 import pares
print(pares)