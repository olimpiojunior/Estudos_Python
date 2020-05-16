'''
Escrevendo em aquivo
Ao abrir o arquivo existente para write, ele será modificado
'''
with open('texto.txt', 'w') as arquivo:
    arquivo.write('Estou escrevendo nesse arquivo.\n')
    arquivo.write('Estou gostando de aprender python.\n')
    arquivo.write('Vale lembrar que ele reescreveu o texto.\n')
    arquivo.write('Não sabia que ele ia sobreescrever o texto.\n')
    arquivo.write('Mas faz sentido por que o cursor não foi configurado.\n')

with open('texto.txt', 'r') as arquivo:
    print(arquivo.read())

#Criando um arquivo
arquivox = open('junior.txt', 'w')

arquivox.write('Novo arquivo criado no diretório Sectoin_13.\n')
arquivox.write('Não tem como não gostar de Python')

arquivox.close()

with open('junior.txt') as junior:
    print(junior.read() + '\n')

print(20*'---')

#recebendo dados
with open('frutas.txt', 'w') as frutas:
    while True:
        fruta = input('Informe um texto ou digite sair: ')
        if fruta != 'sair':
            frutas.write(fruta + '\n')
        else:
            break
print(20*'---')
with open('frutas.txt') as frutas:
    print(frutas.read().title())