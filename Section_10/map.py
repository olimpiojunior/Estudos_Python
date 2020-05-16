"""
map - função map realiza mapeamento de valores para função
function - f(x)
dados - a1, a2, a3 ... an
map object: map(f, dados) -> f(a1), f(a2), f(a3), ...f(an)
-------------------------------------------------------------------
import math

def calc(r):
    return math.pi * (r**2)

raios = [1, 2.2, 3., 4, 5.7, 8]
lista = []
for i in raios:
    lista.append(calc(i))

print(lista)

#Usando map - map(função, intervalo), retorna um map object
areas2 = map(calc, raios)
print(list(areas2))
print(type(areas2))

#map com lambda

print(list(map(lambda r: math.pi * r**2, raios)))
print(tuple(map(lambda r: math.pi * r**2, raios)))
print(set(map(lambda r: math.pi * r**2, raios)))

#OBS: Após utilizar a função map(), após a primeira utilização dos resultados, os valores são zerados
-----------------------------------------------------------------------------------------------------
"""
cidades = [('Berlin', 45), ('Tókio', 55), ('Rio', 27), ('Nairobi', 34), ('cairo', 65), ('Paris', 12)]

print(cidades)

c_para_f = map(lambda dado: (dado[0], (9/5)*dado[1]+32), cidades)
print(list(c_para_f))