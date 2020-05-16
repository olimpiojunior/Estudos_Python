'''
Funções com parametros
funções que recebem dados para serem processados dentro da função
entrada -> processamento -> saida

A função é feita com parametros, Ao usar essa funão é passado os argumentos

-----------------------------------------------------
def quadrado(x):
    return x**2

print(quadrado(2))
print(quadrado(3))
print(quadrado(4))

-----------------------------------------------------------
def nome_completo(nome, sobre):
    return f'Certificamos que {nome.title()} {sobre.title()} concluiu o curso com exito'

print(nome_completo('olimpio', 'barbosa dos santos junior'))
------------------------------------------------------------
def nome_completo(nome, sobre):
    return f'Certificamos que {nome.title()} {sobre.title()} concluiu o curso com exito'

#Argumentos nomeados
nome = 'olimpio'
sobre = 'junior'

print(nome_completo(nome, sobre))
print(nome_completo(nome = 'bartolomeu', sobre = 'judioli'))
print(nome_completo(sobre = 'graciel', nome = 'emanuel'))
'''

