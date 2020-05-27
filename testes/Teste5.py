"""
Utilizando type hinting como comentário
"""

import math

def circunf(raio):
    # type: (float) -> float
    return 2 * math.pi * raio ** 2

print(circunf(5))
# print(circunf('geek'))

def texto(texto, tamanho, alinhamento = False):
    # type: (str, bool, int) -> str
    if alinhamento:
        print(f'Eu não gosto de voce')
        tamanho -= 1
    return texto

texto('olimpio', 19, True)

