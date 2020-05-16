'''
Try / Except
Utilizanso o bloco try/except para tratar erros que podem ocorrer, previnindo assim que o programa para de funcionar
sintaxe:
try:
    //execução problematica
except:
    //o que deve ser feito em caso de problemas

#Tratando erro generico
try:
    geek()

except:
    print('ATENÇÃO: Algo de errado não esta certo')

try:
    len(5)
except:
    print('PRESTE MAIS ATENÇAO')
'''
#O usual é tratar os erros específicos
try:
    geek()

except NameError:
    print('ATENÇÃO: Algo de errado não esta certo. O nome não existe')
#--------------------------------------------------------------------------
try:
    len(5)
except TypeError:
    print('PRESTE MAIS ATENÇAO, o tipo esta errado bb :)')
#--------------------------------------------------------------------------
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seginte erro: {err}')
#--------------------------------------------------------------------------
#podemos efetuar diversos tratamentos de erros
try:
    #len(6)
    geek()
    #print('geek'[9])
except TypeError as erra:
    print(f'Deu Type erro: {erra}')
except NameError as errb:
    print(f'Deu Name erro: {errb}')
except:
    print('Deu um erro diferente bb')
#--------------------------------------------------------------------------
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'Nome': 'Olímpio'}
print(pega_valor(dic, 'game'))
print(pega_valor(7, 'Nome'))




