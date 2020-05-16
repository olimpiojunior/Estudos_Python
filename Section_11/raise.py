'''
Raise - Criar exceções para funçoes criadas
sintaxe - raise TipoDoErro('Msh do erro')
obs: O raise finaliza a função assim como return
'''
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser string')
    if cor not in cores:
        raise ValueError(f'A cor tem que ser uma entre: {cores}')
    print(f'O texto "{texto}" será escrito na cor: {cor.title()}')

colore('Olimpio', 'azul')
#colore('preto', 6)
colore('O brasil não vai parar', 'branco')
#colore('O fogo vai cair', 'preto')
colore('In God we trust, all others bring data', 'amarelo')
colore('Mais que ano estranho esse de 2020', 'verde')
colore('Quanto mais o tempo passa, mais perto estou de vencer', 'branco')
