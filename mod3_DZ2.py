def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')
print_params()

print_params(b = 25)

print_params(c = [1,2,3])

values_list = [2, 'тест1', False]
values_dict = {'a' : 3, 'b' : 'тест2', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'тест3']
print_params(*values_list_2, 42)
