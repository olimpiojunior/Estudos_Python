"""
Lambda - São funções sem nome, ou seja, funções anonimas
-------------------------
#Ex: função normal
def funcao(x):
    return 3 * x + 1

print(funcao(5))
-------------------------
#Ex: função lambda
calc = lambda x: 3 * x + 1

print(calc(8))
---------------------------------------------------------
#Podemos ter expressões lambdas com multiplas entradas

nome_comp = lambda nome, sobre: nome.strip().title() + ' ' + sobre.strip().title()
print(nome_comp('oliMpio', '   BARBosa'))
print(nome_comp('   olimpio', ' junior  '))
-------------------------------------------------------------------------------------
#Podemos ter varias ou nenhuma entrada na função lambda
amar = lambda: 'Como não amar Python?'
uma = lambda x: x**2
duas = lambda x, y: (x+y)*(x*y)
tres = lambda x, y, z: x ^ 2 + (2*y) + z

print(amar())
print(uma(2))
print(duas(2, 4))
print(tres(1,2,3))
------------------------------------------------------------------------------------------------------------
#Ordenando nomes pelo sobrenome usando a funcção lambda
nomes = ['mario bross', 'dart vader', 'donald trump', 'guido van roussen', 'olimpio junior', 'perna longa']
print(nomes)
nomes.sort(key=lambda sobre: sobre.split(' ')[-1].title())

print(nomes)
"""
#Gerando uma função quadratica com lambda

def funcao(a, b, c):
    return lambda x: (a * x)**2 + b*x + c

if __name__ == '__main__':
    #passando os valores de a, b, c
    num = funcao(2,2,3)

    #passando o valor de x
    print(num(2))

    #ou
    print(funcao(2, 2, 3)(2))

