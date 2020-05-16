'''
Debugando com PDB (Python Debugegr)
Obs - O debbug é realizado na criação do código
Vida de inseto -> Life's Bug
Bug -> inseto
Para utilizar o python debugger, precisamos importar a bbt pdb e então usar a função set_trace()

comandos basicos pdb:
l = listar onde estamos no código
n = proxima linha
p = imprimir variável
c = continua a execução - finaliza o debugging
-------------------------------------------------------------------------------------------------
#Exemplo com pycharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'

print(dividir(6,0))
#----------------------------------------------------------------------------------------
#Exemplo 1 com PDB
import pdb

nome = 'olimpio'
sobrenome = 'barbosa'
pdb.set_trace()
nome_completo = nome.title() + ' ' + sobrenome.title()
curso = 'Programação em Python, melhor lingua'
final = nome_completo + 'Faz o curso' + curso
print(final)
#----------------------------------------------------------------------------------------
#Exemplo 2 com PDB

nome = 'olimpio'
sobrenome = 'barbosa'
import pdb; pdb.set_trace()
nome_completo = nome.title() + ' ' + sobrenome.title()
curso = 'Programação em Python, a melhor lingua foreva'
final = nome_completo + ' faz o curso ' + curso
print(final)
#----------------------------------------------------------------------------------------

#A partir no python 3.7 não precisa mais importar o pdb, ela foi incorporada (buitin) como breakpoint()
#Exemplo 3 com PDB

nome = 'curicacas'
breakpoint()
sobrenome = 'niNJA'
nome_completo = nome.title() + ' ' + sobrenome.title()
curso = 'Programação em Python, a melhor lingua foreva'
final = nome_completo + ' faz o curso ' + curso
print(final)

#cuidado com conflitos com nomes de variáveis e comandos pdb (p, l, n, c)
'''