# my_list = [1, 5, 17, 1234]
#
# for element in my_list:
#     print('element', element)


# incomes = [120, 38.5, 40.5, 80]
#
# S = 0
# for income in incomes:
#     print('current income', income)
#     print('current S', S)
#     S += income
#     print('New S', S)
#     print()
#
# print('Answer: s=', S)


# num_list = [98, 24, 23, 12, 3]
# p = 1
#
# for nums in num_list:
#     p *= nums


# n = 5
# sum = 1
# for i in range(2,n + 1):
#     sum *= i
#     print(sum,i)


# n = 25
# for i in range(n+1):
#     print('*' * i)


# # Задаём список значений массы товаров
# weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
#
#
# # Задаём максимальное значение веса груза
# max_weight = 100
# # Задаём начальный номер груза
# num = 1
# # Создаём цикл по элементам списка со значениями массы товаров
# # weight — текущее значение веса
# for weight in weight_of_products:
#     # Если текущий вес меньше максимального,
#     if weight < max_weight:
#         # выводим номер груза, его вес и отправляем его в легковую машину.
#         print('Product {}, weight: {} -passenger car'.format(num, weight))
#     else:
#         # В противном случае
#         # выводим номер груза, его вес и отправляем его в грузовую машину.
#         print('Product {}, weight: {} -truck'.format(num, weight))
#     # Увеличиваем значение номера груза на 1
#     num += 1


# # Задаём список значений массы товаров
# weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
# # Задаём максимальное значение веса груза
# max_weight = 100
# # Вычисляем длину списка
# N = len(weight_of_products)
# # Создаём цикл по последовательности чисел от 0 до N (не включая N)
# # i — текущее значение последовательности
# for i in range(N):
#     # Обращаемся к элементу по индексу и сравниваем его с максимумом
#     if weight_of_products[i] < max_weight:
#         # Если текущий вес меньше максимального,
#         # выводим номер груза, его массу и отправляем его в легковую машину.
#         print('Product {}, weight: {} -passenger car'.format(i+1, weight_of_products[i]))
#     else:
#         # В противном случае
#         # выводим номер груза, его массу и отправляем его в грузовую машину
#         print('Product {}, weight: {} -truck'.format(i+1, weight_of_products[i]))


# num_list = [1, 10, 3, -5]
# i = 0
# num_list.sort()
# for element in num_list:
#     print("element {}: {}".format(i, element))
#     i+=1


# num_list = list(range(0,100,3))
# count_even = 0
#
# for num in num_list:
#
#     if num %2 == 0:
#         count_even+=1


# mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
# count_str = 0
# for element in mixture_list:
#     if type(element) == type("da"):
#
#         count_str +=1
#
# print(count_str)


# word_list = ["My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
# text = ''
# for word in word_list:
#     if word == 'EOS':
#         word =  '.'
#         text+= word
#     else:
#         text += ' ' + word
# text = text.strip()
# print(text)