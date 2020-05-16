"""
list Comprehension
Utilizadando list comprehension nós podemos gerar ovas listas com dados processados a partir de outro iterável

#Parte 01
#1
num = [1,2,3,4,5]
res = [i * 10 for i in num if i%2 != 0]
print(res)

#2
print([i**2 for i in [1,2,3,4,5]])

#3
nome = 'olimpio'

print([l.upper() for l in nome])

#4
lista = 'maria', 'julia', 'guilherme', 'vanessa'

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(nome) for nome in lista])

#5
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

#6
print([str(valor) for valor in range(0,10, 2)])
"""
#Parte2

#1
num = [1,2,3,4,5,6,8, 9]

par = [x for x in num if x%2 == 0]
impar = [x for x in num if x%2 == 1] #ou

#Em numeros pares, o módulo de 2 é zero, em python 0 == False (not False = True)
pares = [x for x in num if not x % 2]
impares = [x for x in num if x % 2]

print(par)
print(impar)
print(pares)
print(impares)

#2
res = [n*2 if n%2 == 0 else n/2 for n in num]
rit = [n**2 if n == 2 else n-5 for n in num]
print(res)
print(rit)