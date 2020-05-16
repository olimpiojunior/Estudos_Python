'''
Criando sua própria versão de loop
'''

#Criando um for
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

#meu_for('olimpio junior')
#meu_for([1,2,3,4,5,6,7])

#Iterador customizado (range())
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration("Deu um erro por que ja acabou e voce continua tentandooooooooooooooooooooooooooooooooo")

con = Contador(1, 4)
print(con.menor) #1
print(con.maior) #4

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) #StopIteration

for i in Contador(1, 51):
    print(i)