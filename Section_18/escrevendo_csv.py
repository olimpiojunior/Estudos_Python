"""
Escrever no arquivo CSV
writer() -> escritor
writerow() -> escreve uma linha

Obs: writer() gera um objeto para que possamos escrever em uma lista csv. Utilizando o
método writerow() para escrever cada linha
"""
from csv import writer, reader, DictWriter

# Criando e escrevendo arquivos CSV com writer
with open("filme.csv", "w") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Autor', 'Duração'])
    # print(escritor_csv)
    while filme != 'sair':
        filme = input('Deseja sair ou adicionar um filme: ')
        if filme != 'sair':
            print(20 * '-+')
            titulo = input('Informe o nome do filme: ')
            autor = input('Informe o nome do autor: ')
            duracao = input('Informe a duração do filme: ')
            print(20 * '-+')
            escritor_csv.writerow([titulo, autor, duracao])
        else:
            print('Obrigado!')

# Realizando a leitura dos filmes
with open("filme.csv") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f"O filme '{linha[0].title()}', escrito por {linha[1].title()} tem duração de {linha[2]} horas")

# Criando e adicionando livros com DictWriter
with open("livros.csv", "w") as arquivo2:
    cabecalho = ["Título", "Autor", "Paginas"]
    dict_csv = DictWriter(arquivo2, fieldnames=cabecalho)
    dict_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('\nDeseja adicionar livros ou sair? ')
        if filme != 'sair':
            print(20 * '-+')
            titulo2 = input('Informe o nome do livro: ')
            autor2 = input('Informe o nome do Autor: ')
            paginas = input('Informe o numero de paginas: ')
            dict_csv.writerow({"Título": titulo2, "Autor": autor2, "Paginas": paginas})
            print(20 * '-+')
        else:
            print('Obrigado!')

# Realizando a leitura dos livros
with open("livros.csv") as arquivo:
    leitor2_csv = reader(arquivo)
    next(leitor2_csv)
    for linha in leitor2_csv:
        print(f"O livro '{linha[0].title()}', escrito por {linha[1].title()} tem {linha[2]} paginas")
