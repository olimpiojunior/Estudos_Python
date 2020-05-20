'''
Preservando Metadata com wraps
-Metadados ->São dados intrinsecos em arquivos
-Wraps -> São funções que envolvem elementos com diversas finalidades
'''
from functools import wraps

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Função para logar dentro de outra"""
        print(f'Voce esta chamando a função: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, *kwargs)

    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


#print(soma(6, 7))

#Quando chama a documentação e nome da funão soma, ela retorna o do decorator
print(f'Nome da função: {soma.__name__}')
print(f'Documentação da função: {soma.__doc__}')

#Para resolver, coloca-se o decorator wraps
def ver_log2(funcao2):
    @wraps(funcao2)
    def logar2(*args, **kwargs):
        """Função para logar dentro de outra"""
        print(f'Voce esta chamando a função: {funcao2.__name__}')
        print(f'Aqui a documentação: {funcao2.__doc__}')
        return funcao2(*args, *kwargs)
    return logar2


@ver_log2
def soma2(a, b):
    """Soma dois números"""
    return a + b

print(20*'--')
print(f'Nome da função: {soma2.__name__}')
print(f'Documentação da função: {soma2.__doc__}\n')
print(help(soma2))

