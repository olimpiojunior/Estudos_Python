"""
Set Comprehension
"""

num = {num for num in range(1,9)}
print(num)

num2 = {x**2 for x in range(10)}
print(num2)

num2 = {x: x*'x' for x in range(10)}
print(num2)

letras = {letra for letra in 'olimpio junior'}
print(letras)

def diz():
    print('HELLO WORDL')