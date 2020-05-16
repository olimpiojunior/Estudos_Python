'''
Sorted - Serve para ordenar elementos. Podemos usar o sorted em qualquer iterável
obs: Diferente do sort(), que só funciona com listas
'''
#Sort()
num = [9,67,54,3,4,65,2,77,55,1,0]
num.sort()
print(f'Lista ordenada com sort():   {num}')
print(80*'-')

#Não permanente, a lista original permanece a mesma
lista = [1,32,4,30,6,8,0,9,7,12,5,19,4,23]
print(f'Lista original: {lista}')
print(f'Lista ordenada com sorted(): {sorted(lista)}')
print(f'Lista original: {lista}')

#Ordenando de forma decrescente (inverte)
print(f'Lista decrescente com sorted(): {sorted(lista, reverse = True)}')
print(80*'-')

#convertendo
print(f'Conv set: {set(sorted(lista))}')
print(f'Conv tuple: {tuple(sorted(lista))}')

#Ordenando coisas mais complexas
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu amo bolo', 'eu amo pizza']},
    {'username': 'pedro',  'tweets': ['Eu amo bolo']},
    {'username': 'maria',  'tweets': []},
    {'username': 'carla',  'tweets': []},
    {'username': 'joão',   'tweets': ['Eu amo pedalar', 'eu fui na disney']},
    {'username': 'will',   'tweets': []}
]
#Ordenando pela chave username de forma alfabetica (username)
print(sorted(usuarios, key=lambda usuario: usuario['username']))

#Ordenando pela qtd de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

#Titulos de musicas com qtd que tocou
musicas = [
    {'titulo': 'Maranata', 'tocou': 5},
    {'titulo': 'Gabriel', 'tocou': 16},
    {'titulo': 'Tranquilão', 'tocou': 2},
    {'titulo': 'Umaduc', 'tocou': 10}
]
#Ordenando da menos tocada para a mais tocada
print(sorted(musicas, key=lambda tocou: tocou['tocou']))

#Ordenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda tocou: tocou['tocou'], reverse=True))