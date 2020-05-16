'''
Geradores -> Podem ser criados com funções geradoras (yield) e expressões geradoras
Obs: Generators são Iterators, mas nem todo iterator é um generator
Obs: Um Generator Functoin não é um Generator, Ele gera um generator
-------------------------------------------------------------------------------------
|        Funções                            |       Generators                      |
-------------------------------------------------------------------------------------
|Utilizam return                            |Utilizam yield                         |
|Retorna uma vez                            |Podem utilizar yield multiplas vezes   |
|Qnd executada, retorna um valor            |Qnd executada, retorna um generator    |
|Após o return sai da função                |Após o yield continua na função        |
-------------------------------------------------------------------------------------
'''
def conta_ate(valor_max):
    contador = 1
    while contador <= valor_max:
        yield contador
        contador += 1

gen = conta_ate(4)
print(type(gen))

print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
print('----')

gen2 = conta_ate(7)
print(next(gen2))
print(next(gen2))
print('----')
for i in gen2:
    print(i)










