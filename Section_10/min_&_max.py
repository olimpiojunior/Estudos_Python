'''
Min e Max
max() - Retorna o maior valor em um iteravel
min() - Retorna o menor valor em um iteravel

lista = [8,7,6,5,4,3,4,7,9,78,6,5]
print(f'Lista: {max(lista)}')

tupla = (8,7,6,5,4,3,4,7,9,78,6,5)
print(f'Tupla: {max(lista)}')

conjunto = {8,7,6,5,4,3,4,7,9,78,6,5}
print(f'Conjunto: {max(lista)}')

diction = {'a': 10, 'b': 28, 'c': 34, 'd': 44, 'e': 25}
print(f'Chave dict: {max(diction)}')
print(f'Valor dict: {max(diction.values())}')

#Retornando o maior
var1 = int(input('Primeiro valor: '))
var2 = int(input('Segundo valor: '))

print(f'O maior entre os dois é: {max(var1, var2)}')

#Outras operações
print(max(3,4,5,6,54,43,3))
print(max('a', 'z', 'j', 's'))
print(max('abc', 'zab', 'jqk', 'stu'))
'''
#Obs: Para a função min() funciona da mesma forma

nomes = ['Olimpio', 'Lenis', 'Talita', 'Glaucia', 'Junior']

#Retorna o maior/menor por ordem alfabética
print(max(nomes))
print(min(nomes))

#Retornando pelo tamanho
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

#Buscando as musicas mais e menos tocadas
musicas = [
    {'titulo': 'Maranata', 'tocou': 5},
    {'titulo': 'Gabriel', 'tocou': 16},
    {'titulo': 'Tranquilão', 'tocou': 2},
    {'titulo': 'Umaduc', 'tocou': 10}
]
print(max(musicas, key=lambda music: music['tocou']))
print(min(musicas, key=lambda music: music['tocou']))

#Imprimindo somente os titulos das musicas mais e menos tocadas
print(max(musicas, key=lambda music: music['titulo'])['titulo'])
print(min(musicas, key=lambda music: music['titulo'])['titulo'])

#Desafio - Como encontrar a musica mais tocada sem Max, Min ou lambda
max = 99999
for music in musicas:
    if music['tocou'] < max:
        max = music['tocou']

print(max)