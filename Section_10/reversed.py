'''
Reversed - Parecido com a função reverse, porém funciona com qualquer iterável
Obs: Diferente da função reverse(), que só funciona em listas
'''
l = [1,2,3,4,5,6,7,8,9]
res = reversed(l)

#Não retorna uma lista

print(res)

print(list(reversed(l)))
print(tuple(reversed(l)))
print(set(reversed(l))) #Em set não tem ordem

#iterando
for letra in reversed('olimpio'):
    print(letra, end='')

print('\n')
#É possivel fazer o mesmo sem uso do for
print(''.join(list(reversed('olimpio'))))

print('olimpio'[::-1])

#invertendo numeros
for n in reversed(range(10)):
    print(n, end='')

for n in range(9, -1, -1):
    print(n, end='')

