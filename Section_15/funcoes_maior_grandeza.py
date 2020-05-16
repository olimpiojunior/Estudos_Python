'''
Fuções de maior grandeza - Higher Order Function HOF
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado, ou que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis
do tipo de funções nos nossos programas.
'''
#Exemplo - definindo as funções
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(5, 3, soma))
print(calcular(5, 3, sub))
print(calcular(5, 3, mult))
print(calcular(5, 3, div))

#Nested Functions (funções aninhadas)
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Eai ', 'Suma daqui ', 'Como vai ', 'Gosto muito de vc '))
    return humor() + pessoa

print(cumprimento('Olímpio'))
print(cumprimento('Darth Vader'))

#Retornando funções de outras funções
def faz_rir():
    def rir():
        return choice(('kkkkkkkkkkk', 'HAHAHAHAHHAHAHAH', 'Ashuashuashuashuashu'))
    return rir

rindo = faz_rir()
print(rindo())

#Inner Functions (funções internas)
def xingar(pessoa):
    def xingando():
        xingamento =  choice(('Puta que pariu', 'Vai tomar no C*', 'Ta querendo me f*'))
        return f'{xingamento} {pessoa}'
    return xingando()

xing = xingar('Darth Vader')
print(xing)

