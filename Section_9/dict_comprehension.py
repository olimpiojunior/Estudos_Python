"""
Dictionary Comprehension
"""
num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in num.items()}
print(quadrado)

lista = [1, 2, 3, 4, 5] #or tuple, or set
cont = {valor: valor*'o' for valor in lista}
print(cont)

chaves = 'abcde'
valores = 1, 2, 3, 4, 5
junta = {chaves[i]: valores[i] for i in range(len(valores))}
print(junta)

#Exemplo de lógica condicional
res = {n: ('par' if n%2 == 0 else 'impar') for n in lista}
print(res)