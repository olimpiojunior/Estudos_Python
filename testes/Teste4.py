"""
mypy só funciona quando se utiliza o type hinting
type hinting é a utilização de atributos com os tipos sendo passados dentro da função, como abaixo
"""
import math

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '+')


nome = cabecalho('olimpio junior')
nome2 = cabecalho('olimpio junior', alinhamento=False)
print(nome)
print(nome2)
print(type(nome))
print(type(nome2))

nome3 = cabecalho('olimpio junior', alinhamento=True)
print(nome3)

def circunf(raio: float) -> float:
    return 2 * math.pi * raio ** 2

print(circunf(2.))

num: float = 5.
print(__annotations__)

print(circunf.__annotations__)
print(' olimpio junior '.center(50, '#').title())


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    def andar(self):
        return f'{self.__nome} está andando!'


olimpio = Pessoa('Olimpio', 24, 81.4)

print(olimpio.__dict__)
print(olimpio.andar())
print(olimpio.nome)

# Obs: Classe não tem annotations, mas é possivel acessar com __init__
print(olimpio.andar.__annotations__) # Retorna um dict vazio
print(olimpio.__init__.__annotations__)



