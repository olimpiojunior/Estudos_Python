'''
Manipulando arquivos do OS
'''
import os

print(os.getcwd()) #verificando o path
os.chdir('..') #Voltando uma pasta
print(os.getcwd())
print(os.path.isabs('C:\\User\\Olimpio'))

#Identificando o OS
print(os.name) #windows = nt

import sys
print(sys.platform) #win32

res = os.path.join(os.getcwd(), 'Scripts')
os.chdir(res)

#listando o diretório
print(len(os.listdir()))
print(20*'--')

#Utilizando scandir(), após utiliza-la é preciso fecha-la
arquivo = list(os.scandir())
print(arquivo)
print(dir(arquivo))

print(arquivo[0].inode()) #identificador de node
print(arquivo[0].is_dir()) #É um diretório? False
print(arquivo[0].is_file()) #É um arquivo? True
print(arquivo[0].is_symlink()) #É um link simbólico? False
print(arquivo[0].name) #Nome do arquivo
print(arquivo[0].path) #Caminho até o arquivo
print(arquivo[0].stat()) #Estatistic

