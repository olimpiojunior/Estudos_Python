'''
Seek & Cursor
seek() - É utilizada para movimentar um cursor
'''
arquivo = open('texto.txt')
print(arquivo.read())

#Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(20*'--')
print(arquivo.read())

arquivo.seek(100)
print(20*'--')
print(arquivo.read())

arquivo.seek(150)
print(20*'--')
print(arquivo.read())

#Para ler o arquivo linha a linha, usa-se a função readline()
print(20*'--')
arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#Transformando o texto em string
arquivo.seek(0)
ret = arquivo.readline()
texto = arquivo.read()
print(type(ret))
print(ret)
print(ret.split(' '))
print(20*'--')
print(texto)
print(20*'--')
print(texto.title())

#utilizando readlines()
print(20*'--')
arquivo.seek(0)
rets = arquivo.readlines()
print(rets[1:4])
print(rets[4:8])
print(len(rets))

#Após abrir (open) o arquivo e trabalhar com ele, é necessário fecha-lo
print(20*'--')
print(texto)
print(arquivo.closed) #False se aberto
arquivo.close() #Fechando o arquivo
print(arquivo.closed) #True se fechado


