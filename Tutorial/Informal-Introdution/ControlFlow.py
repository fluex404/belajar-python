
def fib(n):
    """print a Fibonanci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b, = b, a+b
        print()
fib(2000)
f = fib
print('jkkk')
f(20)