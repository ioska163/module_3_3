def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params(b=25)
print_params(c=[1,2,3])

values_list = [1, 'Hello', True]
values_dict = {'a':5, 'b':(6,7,8,9), 'c':'hello'}
values_list_2 = ['hello', False ]
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)







