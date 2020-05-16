'''
Decorators com diferentes assinaturas
-A assinatura de uma função é representada pelo seu retorno, nome e parâmetro de entrada
'''


def gritar(funcao):
    def aumentar(*args):
        return funcao(*args).upper()

    return aumentar


@gritar
def saudar(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, rango):
    return f'Olá, eu gostaria de {principal}, acompanhado de {rango}, rápido!'


@gritar
def ole():
    return 'ole, olee, oleee, oleeee, oleeeee'


@gritar
def eai(nome):
    return 'Eai ' + nome + nome[-1] * 20


print(saudar('Olímpio'))
print(ordenar('giroba', 'cebola'))
print(ole())
print(eai('rapaziada'))
print(20*'---')


# Decorators com argumentos

def verifica_primeiro(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, o primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro('pizza')
def comida_fav(*args):
    print(f'Minha comida favorita é {args[0]} e {args[1]}, o resto é resto')

@verifica_primeiro(10)
def soma_dez(num1, num2):
    return f'A soma é {num2 + num1}!'

print(soma_dez(10, 50))
print(soma_dez(12, 10))
print(20*'---')
print(comida_fav('batata'))
print(comida_fav('pizza', 'batata'))
