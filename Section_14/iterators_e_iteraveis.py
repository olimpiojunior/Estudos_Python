'''
Iterators e Iterables
iterator -> Um objeto que pode ser iterado e retorna um dado sendo um elemento por vez qnd uma função next() é chamada.
iterables -> Um objeto que irá retornar um iterator quando a função iter() for chamada.
'''
nome = 'geek'
num = [1,2,3,4,5]

it1 = iter(nome)
it2 = iter(num)

print(next(it1)) #g
print(next(it1)) #e
print(next(it1)) #e
print(next(it1)) #k

for i in num:
    print(f'{next(it2)}')