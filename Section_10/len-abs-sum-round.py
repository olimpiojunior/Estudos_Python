'''
len() - retorna tamanho, ou seja, a qtd de elementos
abs() - retorna o valor absoluto de um inteiro ou real
sum() - retorna a soma total dos elementos
round() - retorna um numero arredondado para n digito de precisão
'''

lista = [1,2,3,4,5,6,7]
tupla = (1,2,3,4,5,6,7)
conjunto = {1,2,3,4,5,6,7}
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

#Retorna o tamanho
print(len(lista))
print(len(tupla))
print(len(conjunto))

#Retorna o valor absoluto
print(abs(-50))
print(abs(6.78))

#Soma os elementos
print(sum(lista))
print(sum(tupla))
print(sum(conjunto))
print(sum(lista, 5))
print(sum(dict1.values()))

#Rotorna o valor arredondado
print(round(10.4))
print(round(10.5))
print(round(10.6))
print(round(15.89999, 2))
print(round(15.77999, 2))