'''
Modos de abertura de arquivos

r -> abre para leitura
w -> abre para escrita, e sobrescreve caso o arquivo ja esxista
x -> abre para escrita, somente se o arquivo não existir
a -> abre para escrita, adicionando no final do arquivo (não controla o cursor - seek)
+ _> abre para o mode de atualização leitura e escrita
'''

try:
    with open("university.txt", "x") as arquivo:
        arquivo.write('Sou um jovem muito feliz.\n')
        arquivo.write('E agora estou escrevendo este texto.\n')
except:
    print('O arquivo ja existe.\n')

with open("frutas.txt", "a") as arquivo1:
    while True:
        fruta = input('Digite o nome da fruta (ou digite sair): ')
        if fruta != 'sair':
            arquivo1.write(fruta + '\n')
        else:
            break

with open('junior.txt', 'r+') as arquivo2:
    arquivo2.write('Estou testando o + agora\n')

with open('junior.txt', 'w+') as arquivo2:
    arquivo2.write('Estou testando o + agora pela segunda vez.\n')





