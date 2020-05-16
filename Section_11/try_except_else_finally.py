'''
try/except/else/finally
Quando tratar os erros?
Toda entrada de dados do usuário deve ser tratada

#Else é usado somente quando não ocorre o erro
try:
    num = int(input('informe seu cpf: '))
except ValueError:
    print(f'Não consegue néh moisés')
else:
    print(f'Voce digitou {num}')

#finally
try:
    num = int(input('informe seu cpf: '))
except ValueError:
    print(f'Não consegue néh moisés')
else:
    print(f'Voce digitou {num}')
finally:
    print('Executado com sucesso pai')

#------------------------------------------------------------------
#forma ruim
def divifir(a,b):
    return a/b

num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser  numerico')
try:
    print(f'A divisão é: {divifir(num1, num2)}')
except NameError:
    print('Tem erro ai')


#A melhor forma é tratar todos os erros dentro da função
def soma(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
       return 'Valor incorreto bb'
    except ZeroDivisionError:
        return 'Não é possivel realizar divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(soma(num1, num2))
'''
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))