"""
Sistema de Arquivos - Manipulação
"""
import os
#descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt')) #False
print(os.path.exists('frutas.txt')) #True

#voltando uma pasta no path
print(os.getcwd()) #C:\Users\Olimpio\guppe\Section_13
os.chdir('..') #C:\Users\Olimpio\guppe

print(os.path.exists('Lib')) #True
print(os.path.exists('Section_12/built-in.py')) #True

os.chdir('..')
print(os.getcwd()) #C:\Users\Olimpio

print(os.path.exists('Documents')) #True

#Criando Arquivos no path atual (C:\Users\Olimpio)
open('arquivo-teste.txt', 'w').close()
print(os.getcwd())
with open('arquivo-teste.txt', 'w') as arquivo:
    arquivo.write('Estou escrevendo em um arquivo que esta no meu sistema operacional')

print(20*'---')
#Criando um diretorio (pasta) no path atual
#os.mkdir('pasta')

#Criando diretorios e arquivos no disco C:
#with open('C:/Users/Olimpio/pasta/arquivo.txt', 'w') as pasta:
    #pasta.write('Criei uma pasta e estou criando um arquivo.txt dentro\n')
    #pasta.write('Este texto dever escrito dentro do arquivo')

#Criando diretorios e arquivos no disco D:
#with open('D:/Users/Olimpio/Documents/Junior/QUARENTENA/Arquivo.txt', 'w') as pasta:
    #pasta.write('Estou criando esse arquivo aqui para dizer algo:\n')
    #pasta.write('   Eu vou passar no processo seletivo de Trainee 2020')

#Renomeando diretório
#os.rename('C:/Users/Olimpio/pasta', 'NOME_NOVO2')


#Renomeando arquivo
#os.rename('C:/Users/Olimpio/TESTANDO.txt', 'TESTANDO2222.txt')

#Removendo arquivos. No windows precisa de permissão
print(os.getcwd())
os.remove('C:/Users/Olimpio/NOME_NOVO2')
os.remove('C:/Users/Olimpio/NOME_NOVO')


