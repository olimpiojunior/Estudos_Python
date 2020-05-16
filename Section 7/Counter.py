'''
Módulo Collection - counter
counter - recebe um iterável como parametro e retorna um objeto do tipo colletions counter que é parecido com um dicionário
contendo o valor passado e a quantidade de repetições
'''

from collections import Counter

lista = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,6,7,8,8,8,8,8,4,4,4,56,56,56,56,13,13,13,13]
res = Counter(lista)
#print(f'Tipo: {type(res)}')
#print(res)

#Exemplo com texto
texto = '''E se o meu povo, que se chama pelo meu nome, se humilhar e orar, e se converter dos seus maus caminhos, então eu ouvirei dos céus,
perdoarei os seus pecados e sararei a sua terra
'''

res = Counter(texto)
#printando as letras com 5 mais ocorrencias
print(res.most_common(5))