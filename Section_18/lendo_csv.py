"""
CSV - Comma Separeted Values (Valores Separados por Virgula)

with open("original.csv") as arquivo:
    dados = arquivo.read()
    print(dados)
    dados = dados.split()[3:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em aquivos csv;
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts
"""
from csv import reader, DictReader

with open("original.csv") as arquivo:
    leitor_lista = reader(arquivo)
    for lista in list(leitor_lista)[1:]:
        print(f'O lutador {lista[0]}, nasceu na(o) {lista[1]}, e mede {lista[2]} cm ')

print(30 * '+-')

with open("paises.csv") as arquivo2:
    leitor_lista2 = DictReader(arquivo2, delimiter=';')
    # print(list(leitor_lista2))
    for lista2 in leitor_lista2:
        print(f"O Presidente do(a) {lista2['País']} é {lista2['Presidente']} e a capital é {lista2['Capital']}")
