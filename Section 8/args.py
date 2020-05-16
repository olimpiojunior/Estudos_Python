'''
Entendendo o *args
O *args é um parametro como qqr outro, isso significa que pode ser chamado por qqr outro nome, desde que comece com *.
O parametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.


def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(soma(2, 3, 6, 100))
print(soma(2, 50))
---------------------------------------------------------------------
#Simplificando a soma anterior

def soma(*args):
    return sum(args)

print(soma(1.,2,3,4,5,))

--------------------------------------------------------------------
#Mais utilização com o parametro *args
def exemple(nome, num, *args):
    print(f'O numero de {nome.title()} é {num}')
    return sum(args)

print(exemple('olimpio', 99810154, 12,100,45))

---------------------------------------------------------------
#Mais informações sobre o parametro args
def verifica(*args):
    if 'olimpio' in args and 'milagre' in args:
        return 'Tem os nomes'
    elif 7 in args and 9 in args:
        return 'tem o 7 e o 9 heim'
    return 'Não tem o nome nem os numbs'

print(verifica())
print(verifica('olimpio', 7, 9))
print(verifica('manuel', 'milagre', 'olimpio'))
print(verifica(1,5,7,9))
-------------------------------------------------------------
#Relembrando o Desempacotamento
def soma(*args):
    return sum(args)

numeros = [1,2,3,4,5,6,7]
n1, n2, n3, n4, n5, n6, n7 = numeros

print(soma(n1, n2, n3, n4, n5, n6, n7))
#Ou
print(soma(*numeros))
#O * serve para informar ao Python que estamos passando um conjunto de números, é necessário desempacotar
'''