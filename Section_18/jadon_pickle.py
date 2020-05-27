"""
Json -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços fornecidos por uma empresa (Facebook, Twiter, Youtube) e
terceitos (nós desenvolvedores)

Obs: Json trabalha com aspas duplas
"""
import json

import jsonpickle

ret = json.dumps(['produto', {"Playstation 4": ('2TB', 'Novo', '220V', 2350)}])
print(ret)
print(type(ret))


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


garfild = Gato('Garfild', 'vira-lata')
print(garfild.raca)
print(garfild.nome)
print(garfild.__dict__)
ret = json.dumps(garfild.__dict__)
print(ret)

# Integrando o Pickle com Json
# pip install jsonpickle
ret2 = jsonpickle.ecoding.encode(garfild)
