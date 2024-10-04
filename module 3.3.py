def print_params(a,b,c):
    print(a,b,c)
print_params(1, "строка", True)
#print_params() выдает ошибку
#print_params(1, 'строка') выдает ошибку
print_params( 1, 25, True)
print_params(1, 'строка', [1,2,3])

values_list = [5,'name', 5.6]
values_dict = {'a' : 1 , 'b' : 'Pavel', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5,'Pavel']
print_params(*values_list_2, 42)








