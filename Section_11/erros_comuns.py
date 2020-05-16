'''
Erros mais comuns
Exeption == Error

1 - SyntaxeError - Ocorre quando uma sintaxe é escrita de forma errada e que não é parte da linguagem
        def escreve:                | Na função ao lado está faltando '()'
            print('olimpio')        |

2 - NameError - Ocorre quando uma variável ou função não foi definida
        print(number)               | Number não foi definido. NameError

3 - TyperError - Ocorre quando uma função/ação é aplicada a um tipo errado
        print(len(5))               | len só é usada em iteraveis
        print([] + ())              | Só pode concatenar listas

4 - IndexError - Ocorre quando tentamos acessar um elemento em uma lista usando indice inválido
        lista = ['oi']              | Na lista ao lado só tem um elemento,
        print(lista[2])             | portanto, não é possivel acessar o indice 2 ou mais

5 - ValueError - Ocorre quando uma função ou operação builtin recebe um argumento com tipo correto
mas valor inapropriado
        print(int('olimpio'))       | O tipo está correto (str), mas não dever ser passado dessa forma

6 - KeyError - Ocorre quando tentameos acessar um dict, com uma chave que não existe
        dic = {}                    | O erro ocorre pq o dicionário esta vazio
        print(dic['nome'])          | não é possivel acessar a chame 'nome'

7 - AttributeError - Ocorre quando uma variavel não tem um atributo ou função
        tupla = (1,6,8,4)           | O erro ocorre pq a função sort() só é utilizada em lista
        print(tupla.sort())         | não é possivel utilizar em tuplas

8 - IndentationError - Ocorre quando não é feita a identação
        for i in range(10):         | O erro ocorre pq não foi feita a identação (4 espaços)
        print(i)                    |
'''

