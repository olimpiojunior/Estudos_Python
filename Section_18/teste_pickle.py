"""
Pickle

A função do Pickle é binarizar um objeto python. Esse processo é chamado Serealização/Deserealização

    Objeto Python -> Binarização
    Binarização -> Objeto Python

Obs: O módulo pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com
arquivos pickle vindos de outras pessoas que você não conhece ou de fontes desconhecidas.
"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'O {self.__nome} está comendo')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'O {self.nome} está latindo')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'O {self.nome} está miando')


# ------------------------------------------------------------------
# Objeto Python -> Binarização
felix = Gato("Felix")
pluto = Cachorro("Pluto")

with open("animais.pickle", "wb") as arquivo:
    pickle.dump((felix, pluto), arquivo)

# ------------------------------------------------------------------
# Binarização -> Objeto Python

with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.miar()
    print(f'O nome do cachorro é {cachorro.nome}')
    cachorro.latir()
