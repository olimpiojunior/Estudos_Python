'''
Leitura de arquivo
open() - Na forma mais simples de utilização nós passamos apenas um paramâmetro de entrada, que neste caso
é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
FileNoFounderError

O python utiliza um cursor na manipulação de arquivos
'''
#Abrindo arquivo no diretório Section_13 (tipo = _io.TextIOWrapper)
arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

#Para ler o conteudo de um arquivo após sua abertura, usa-se a função read()
print(arquivo.read())
print(30*'--')

#Criando uma variável para guardar a leitura (tipo = str)
leitura = arquivo.read()
print(leitura)
print(type(leitura))




