'''
With - É utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o with
Com o with, não precisa fechar o arquivo, o with fecha o arquivo após a utilização
'''
#Utilizando with
with open('texto.txt') as arquivo:
    print(arquivo.read())
    arquivo.seek(0)
    print(20*'--')
    print(arquivo.readlines())
    print(arquivo.closed)

#Sintaxe - Com o texto.txt aberto como arquivo:


