'''
A função é criada com valores sendo passados para os parametros
Obs: A funções com parametros que possuem valores default, devem sempre estar no final da declaração


def pot(num, pot = 2):
    return num**pot

print(pot(2))
print(pot(2,4))

def soma(num1, num2):
    return num1 + num2

print(soma(2,5))
--------------------------------------------------------------

def mostra_indormacao(nome = 'olimpio', instructor = False):
    if nome == 'olimpio' and instructor:
        print(f'Bem vindo instrutor {nome}')
    elif nome == 'olimpio':
        print(f'Eu pensei que voce era o {nome}')
    else:
        print(f'Olá instrutor {nome}')

mostra_indormacao(nome='olimpio', instructor=True)
-------------------------------------------------------------
def soma(a, b):
    return a+b

def mat(a, b, fun=soma):
    return fun(a, b)

def sub(a, b):
    return a - b

print(mat(2,4))
print(mat(2,8, sub))
print(mat(4,9))
------------------------------------------------------------
instructor = 'olimpio'

def retorno():
    instructor = 'maicon'
    return f'hello {instructor}'

print(retorno())

#Utilizando a palavra reservada global para iniciar uma variável global
total = 0

def soma():
    global total
    total += 1
    return total

print(soma())
----------------------------------------------------------------------
#Utilizando uma variável de uma função anterior com a palavra nonlocal

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()

print(fora())
'''
