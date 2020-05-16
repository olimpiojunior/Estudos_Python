"""
Listas Aninhadas
Algumas linguagens (C/Java) possuem uma estrutura de dados chamadas arrays
    -Unidimensionais (arrays/vetores);
    -Multidimensionais (matrizes);
Em Python, nós temos listas;


listas = [[1,2,3], [4,5,6], [7,8,9]]
print(listas)

print(listas[0][1]) #2
print(listas[1][0]) #4
print(listas[2][2]) #9

#Acessando elementos das liistas
for l in listas:
    for n in l:
        print(n)

----------------------------------------------------------------
listas = [[1,2,3], [4,5,6], [7,8,9]]
[[print(n) for n in l] for l in listas]

caderno = [['fei', 'sol', 'rei'], ['mel', 'tio', 'pum']]
[[print(nome) for nome in nomes] for nomes in caderno]
"""

#Gerando um tabuleiro

tab = [[n for n in range(1,4)] for i in range(1,4)]
print(tab)

#jogadas para jogo da velha
velha = [['X' if v % 2 == 1 else 'O' for v in range(1, 4)] for i in range(1, 4)]
print(velha)

#Gerando valores iniciais

print([[' ' for i in range(1, 4)] for j in range(1, 4)])
