# def first_function():
#     print("Hello world!")
# first_function()
# first_function()


# def get_time(distance, speed):
#     result = distance // speed
#     return result
#
# time = get_time(1000, 150)
# print("Time travel will be {} hours".format(time.__round__()))


# def in_list(list_in,obj):
#     for elem in list_in:
#         if obj == elem:
#             print("Element is found!")
#             return True
#     print("Element is NOT found!")
#     return False
#
# num_list = [1,1,3,5,8,13]
# otvet = in_list(num_list, 13)
# print(otvet)


# def root(value,x=2):
#     result = value ** (1/x)
#     return result
# print(root(81,3))

# allowed_marks = [2,3,4,5]
# def add_mark(name, mark, journal = None):
#     if journal is None:
#         journal = {}
#     if mark not in allowed_marks:
#         raise ValueError("Invalid Mark!")
#
#     journal [name] = mark
#     return journal
# print(add_mark("Sasha", 7))


# def root(value, n=2, verbose=False):
#     result = value ** (1/n)
#     if verbose:
#         # Аргументы в функции print,
#         # перечисленные через запятую,
#         # печатаются через пробел
#         print('Root of power', n, 'from',
#             value, 'equals', result)
#     return result
#
# print(root(25,verbose=True))


# # В массив args будут записаны все переданные
# # порядковые аргументы
# def mean(*args):
#     # Среднее значение — это сумма всех значений,
#     # делённая на число этих значений
#     # Функция sum — встроенная, она возвращает
#     # сумму чисел
#     result = sum(args) / len(args)
#     return result
#
#
# # Передадим аргументы в функцию через запятую,
# # чтобы посчитать их среднее
# print(mean(5, 4, 4, 3))


# def mean_mark(name, *marks):
#     result = sum(marks) / len(marks)
#     # Не возвращаем результат, а печатаем его
#     print(name + ':', result)
#
#
# mean_mark("Ivanov", 5, 5, 5, 4,2,2,4,2,3,1,5,2,3,2,1,15,23,12,)
# mean_mark("Petrov", 5, 3, 5, 4)


# def mult(*numbers):
#     summ = 1
#     i =1
#     for num in numbers:
#         summ *= num
#         i+=1
#     return summ
# print(mult(3,5,10))
#


# langs = ['Python', 'SQL', 'Machine Learning', 'Statistics']
# print(*langs, sep = ", ")


#
# def mean_mark(name, *marks):
#     result = sum(marks) / len(marks)
#     # Не возвращаем результат, а печатаем его
#     print(name+':', result)
#
# marks = [4,5,5,5,5,3,4,4,5,4,5]
# mean_mark("Kuznetsov", *marks)


# def schedule(**kwargs):
#     # kwargs — это словарь, проверим это с помощью isinstance:
#     print(isinstance(kwargs, dict))
#     # Напечатаем объект kwargs
#     print(kwargs)
#
#
# schedule(monday='Python', tuesday='SQL', friday='ML')
# # Будет напечатано:
# # True
# # {'monday': 'Python', 'tuesday': 'SQL', 'friday': 'ML'}#



##Красивый вывод словарей
# def schedule(**kwargs):
#     print("Week schedule:")
#     for key in kwargs:
#         print(key, kwargs[key], sep=' - ')
#
#
# schedule(monday='Python', tuesday='SQL', friday='ML')
# # Будет напечатано:
# # Week schedule:
# # monday — Python
# # tuesday — SQL
# # friday — Math
#
# ## Лямда-функции
# root = lambda num,n: num**n
#
# print(root(3,48))
#
# is_even = lambda num: "even" if num % 2 == 0 else "odd"

# print(is_even(17821))


# names = ['Ivan', 'Kim', 'German', 'Margarita', 'Simon']
#
# names.sort(key=lambda name : len(name))
# print(names)
#

    ##Сортировка по размеру строки без лямбда функций
# def get_length(elem ):
#     return len(elem)
        ##Мое решение(ответ правильный, но делает не так оптимально)
#     # list = []
#     # for elem in my_list:
#     #     list.append(len(elem))
#     # list.sort()
#     # return list
#
#
#
#
# new_list = ['bbb', 'ababa', 'aaa', 'aaaaa', 'cc']
# new_list.sort(key=get_length)
# print(new_list)

## Тестовая штука от себя, спасибо чату ЖЭПЭТЭ
# def adding_to_list(my_list, nun):
#     for i in range(len(my_list)):
#         my_list[i] += nun
#     return my_list
# list_1 = [1,2,3,4,5]
# print(adding_to_list(list_1,10))

# #Сортировка сразу по нескольким критериям, КРИТЕРИИ ДОЛЖНЫ БЫТЬ В СКОБКАХ ДЛЯ ОБОЗНАЧЕНИЯ КОРТЕЖА)
# new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
#
# new_list.sort(key=lambda word: (len(word), word))
# print(new_list)

##Поиск гепотинузы, обычная функция и лямбда
# hyp = lambda a,b : (a**2 + b**2) **(1/2)
# print(hyp(3,4))
# def hyp1(a,b):
#     c = (a**2 + b**2) ** (1/2)
#     return c
# print(hyp1(3,4))


# #Задача, с которой я не справлися. Причина: невнимательно читал содержание модуля, сразу забыл как
# #сортировать с помощью лямбды, не стал перечитывать модуль в поисках ответа)
## Задача на использование лямбды в больших функциях
# def sort_sides(l_in):
#     l_in.sort(key = lambda x: (x[0] ** 2 + x[1] ** 2) ** (1/2))
#     return l_in
#









