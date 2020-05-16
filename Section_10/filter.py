"""
Filter - Serve para filtrar dados de uma determinada seleção
function - f(x)
dados - a1, a2, a3 ... an
map object: map(f, dados) -> f(a1), f(a2), f(a3), ...f(an)
OBS: Após utilizar a função map(), após a primeira utilização dos resultados, os valores são zerados
"""
import statistics

dados = [1.3, 4.3, 7.6, 9.8, 6.6]
media = statistics.mean(dados)

res = filter(lambda x: x < media, dados)
#print(list(res))
#print(type(res))

paises = ['', 'Brasil', '', 'Venezuela', 'Argentina', '', '', 'Colombia']

#ros = filter(lambda x: len(x) > 0, paises)
#print(list(ros))
res = filter(None, paises)
#print(list(res))

#Exemplo
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu amo bolo', 'eu amo pizza']},
    {'username': 'pedro', 'tweets': ['Eu amo bolo']},
    {'username': 'maria', 'tweets': []},
    {'username': 'carla', 'tweets': []},
    {'username': 'joão', 'tweets': ['Eu amo pedalar', 'eu fui na disney']},
    {'username': 'will', 'tweets': []}
]

#Filtrar os usuários que estão inativos
#Forma 01
inativos = filter(lambda user: len(user['tweets']) == 0, usuarios)
#print(f'A lista possue {len(list(inativos))} usuarios inativos')

#forma 2

inativos2 = filter(lambda user: not user['tweets'], usuarios)
#print(list(inativos2))
#print(f'A lista possue {len(list(inativos2))} usuarios inativos')
#------------------------------------------------------------------

#combinar filter com map

nomes = ['Vanessa', 'ana', 'Maria']

#Criar uma lista contendo 'Sua estrutura é' +nome, se o nome tiver menos de 5 caracter

lista = map(lambda nome: f'Sua estrutura é {nome}', filter(lambda nome: len(nome) < 5, nomes))
print(list(lista))