'''
Teste de memória com generator
sequência de fibonacci: 1,1,2,3, 5, 8, 13, 21...
'''

#Com lista consome muita memoria ~449MB
def seq_fib(max):
    nums = []
    a, b, = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b, = b, a + b
    return nums

print(seq_fib(9))

#Com generator consome muito menos memória ~3MB
def seq_fib(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b, = b, a + b
        yield a
        cont += 1

for i in seq_fib(9):
    print(i)
