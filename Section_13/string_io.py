'''
String IO
Para ler e escrever dados em arquivos do SO, o software precisa de permissão,
por isso, utiliza-se o string io para criar aquivo em memória
'''
from io import StringIO

#criando um arquivo em memória, já com uma string inserida ou vazia
mensagem = 'Esta é a mensagem que estou escrevendo para dizer que não sei o que dizer'

arquivo = StringIO(mensagem) # -> arquivo = open('arquivo.txt', 'w')

print(arquivo.read())
arquivo.write('\nEstou sem saber agora.')
arquivo.seek(0)
print(arquivo.read())