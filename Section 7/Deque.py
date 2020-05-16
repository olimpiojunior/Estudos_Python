'''
Modulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance
'''

from collections import deque
#cirando uma lista deque
deq = deque('texto')
print(deq, type(deq))

#Adiciona no final
deq.append('k')
print(deq)

#Adiciona no inicio
deq.appendleft('kkk')
print(deq)

#Remove o ultimo elemento
deq.pop()
print(deq)

#Remove no inicio
deq.popleft()
print(deq)