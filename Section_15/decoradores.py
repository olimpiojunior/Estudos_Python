'''
Decorators (decoradores)
Decorators são; funções, Higher Order Function, possuem uma sintaxe propria usando '@' (syntact sugar)
'''


# Decorators como função (Sintaxe não recomendada / No syntact sugar
def seja_educado(funcao):
    def sendo():
        print("Sua presença para nós trouxe alegria.")
        funcao()
        print('Foi bom conhecher você!')

    return sendo


def saudacao():
    nome = input('Qual é o seu nome? ')
    print(f'{nome.title()} veio nos visitar')


def raiva():
    print('EU TE ODEIO')


# Sem decorar a função
# audacao()

# Decorando
# teste = seja_educado(saudacao)
# teste()

#teste2 = seja_educado(raiva)
#teste2()


# Ecarators com Syntact Sugar
def mal_educado(funcao):
    def sendo():
        print('Foi um desprazer te encontrar')
        funcao()
        print('Ja falei pra não me perturbar')
    return sendo


@mal_educado
def resposta():
    print('-Desprazer digo eu, mal educada!')

@mal_educado
def grilada():
    print('-Tira a mão de mim')

resposta()
print(20*'--')
grilada()