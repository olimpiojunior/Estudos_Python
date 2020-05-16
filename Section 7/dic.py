receita = {'jan': 100, 'fev':200, 'mar': 300}
print(receita)

for i in receita:
    print(i)

for v in receita:
    print(receita[v])

for k in receita:
    print(f'Em {k} eu recebi {receita[k]}')

for v in receita.values():
    print(v)

for k in receita.keys():
    print(k)

for k,v in receita.items():
    print(f'Em {k}, nós ganhamos {v}')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))