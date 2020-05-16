'''
**kwargs
Esse também é um parametro de função, mas diferente do *args, o **kwargs exige que coloquemos
parametros nomeados, e transforma esses parametros extras em dicionários

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores(pedro='azul', olimpio='preto', maria='amarelo', will='rosa')
cores(amaral='vermelho')

-------------------------------------------------------------------------
#Mais exemplos com kwargs
def cumprimento(**kwargs):
    if 'olimpio' in kwargs and kwargs['olimpio'] == 'python':
        return 'Não sei descrever o que sinto direito'
    elif 'olimpio' in kwargs:
        return f"{kwargs['olimpio']} não sabe"
    return 'Não tem chave'

print(cumprimento(olimpio='python'))
print(cumprimento(olimpio='Bartolomeu'))
print(cumprimento())


#Sequencia dos parametros: obrigatórios, *args, default, **kwargs (Nesta orgem)
def coisa(num, nome, *args, solteiro=False, **kwargs):
    print(f'O {nome} tem {num} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

coisa(90, 'julia')
coisa(78, 'pedro', 1,4,7,9,5)
coisa(78, 'pedro', 1,4,7,9,5, solteiro=True, )
coisa(67, 'joao', 6,7,8, solteiro=True, java=False, Python='isso')


#Desenpacotar com kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']} voltará!"

nomes = {'nome': 'Jesus', 'sobrenome': 'Cristo'}

print(mostra_nome(**nomes))


#Diferentes formas de desempacotar
def soma(a,b,c,d):
    return a+b+c+d

lista = [1,2,3,4]
tupla = (1,2,3,4)
conjunto = {1,2,3,4}

print(soma(*lista))
print(soma(*tupla))
print(soma(*conjunto))

dict1 = dict(a=2, b=5, c=8, d=9)

print(soma(**dict1))
'''