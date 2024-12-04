# def multiply_lst(lst):
#     if not lst:
#         return 1
#     return lst[0] * multiply_lst(lst[1:])
#
# def inv_sum_list(lst):
#     if not lst:
#         return 0
#     return 1/ lst[0] + inv_sum_list(lst[1:])


# def combination(n,k):
#     def factorial(n):
#         # Задаём условия выхода из рекурсии:
#         if n == 0: return 1
#         if n == 1: return 1
#         # Во всех других случаях возвращаем
#         # произведение текущего числа n и функции от n-1
#         return factorial(n - 1) * n
#     return factorial(n) /(factorial(n-k) * factorial(k))
#
# print(combination(10,5))

# def fib(n):
#     if n == 1: return 1
#     if n == 2: return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(6))
# def power(val,n):
#     return val ** n

# def add_asterisk(stroke):
#     if len(stroke) == 1: return stroke
#     return stroke[0] + "*" + add_asterisk(stroke[1:])
# print(add_asterisk("Hello"))
# def sum_list(matrix):
#     summa = 0
#     for elem in matrix:
#         if type(elem) == list:
#             summa += sum_list(elem)
#         else:
#             summa += elem
#     return summa
#
#
#
#
# matrix = [
#     [1, 1, [1, 2, 3], 0],
#     [4, 2, 1, [10, 52, 2]],
#     [0, 2, 1]
# ]
# print(sum_list(matrix))
# ## 82
#
# input_dict = {
#     'key1': {
#         'key2': ['value1', 'value2'],
#         'key3': {
#             'key4': ['value3']
#         }
#     },
#     'key5': {
#         'key6': {
#             'key7': ['value3', 'value5', 'value6']
#         }
#     }
# }
#
#
# # def print_dict(input_data, level=0):
#     # Если input_data — словарь
#     if type(input_data) is dict:
#         # Создаём цикл по ключам словаря
#         for key in input_data:
#             # Выводим ключ в формате "<пробелы> <имя ключа> ->"
#             print('  ' * level + '{} ->'.format(key))
#             # Повторяем те же операции для каждого значения словаря
#             print_dict(input_data[key], level= level + 1)
#     else: # В противном случае
#         # Выводим значения в формате "<пробелы> <значения>"
#         print('  ' * level + str(input_data))
#
# print_dict(input_dict)