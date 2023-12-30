def test_params(*args):
    for arg in args:
        print(arg)

def factorial(n):
    if n == 1:
        return 1
    factorial_recursive = factorial(n=n-1)
    return n * factorial_recursive

test_params(10, 'строка', True, 3.14)
result = factorial(9)
print(f'Факториал числа 5: {result}')