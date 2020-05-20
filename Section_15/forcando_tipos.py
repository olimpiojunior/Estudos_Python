'''
Forçando tipos de dados com decoradores
'''
def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_ars = []
            for valor, tipo in zip(args, tipos):
                novo_ars.append(tipo(valor))
            return funcao(*novo_ars, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

@forca_tipo(float, float)
def dividir(a, b):
    return a / b

print(repete_msg('Estou digitando essa msg', '6'))
print(dividir('7', '9'))
