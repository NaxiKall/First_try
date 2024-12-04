# prices = [34562, 66572, 25683, 17683, 56389, 28973]
# ## filtered_prices = [25683, 17683, 28973]
#
#
# filtered_prices = list(filter(lambda x: x < 30000, prices))
#
# print(filtered_prices)




# def filter_family(services):
#     family_list = ['certificate of a large family','social card',
#                    'maternity capital','parking permit','tax benefit',
#                    'reimbursement of expenses',
#                    "compensation for the purchase of children's goods"]
#     # Фильтруем список services с помощью filter()
#     # Первый аргумент — lambda-функция, которая возвращает True,
#     # если её аргумент есть в списке family_list,
#     # в противном случае она возвращает False
#     result = list(filter(lambda x: x in family_list, services))
#     return result


# reg = [('Ivanov', 'Sergej', 24, 9, 1995),
#       ('Smith', 'John', 13, 2, 2003),
#       ('Petrova', 'Maria', 13, 3, 2003)]
#
#
#
# # Объявляем функцию-преобразование для кортежа
# def update_tuple(arg):
#     # Выделяем фамилию из кортежа
#     surname = arg[0]
#     # Выделяем имя из кортежа
#     name = arg[1]
#     # Создаём новую запись: фамилия + пробел + первая буква имени + точка
#     new_surname = surname + ' ' + name[0] + '.'
#     # Возвращаем обновлённый кортеж
#     return (new_surname, arg[2], arg[3], arg[4])
#
# # Фильтруем записи по условию, что последний элемент кортежа > 2000
# filter_reg = filter(lambda x: x[-1] > 2000, reg)
# # Применяем функцию-преобразование к каждому кортежу из списка и создаём новый список
# new_reg = list(map(update_tuple, filter_reg))
#

# data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
#  (0.02731, 6.421, 78.9, 242.0, 9.14),
#  (0.02729, 7.185, 61.1, 242.0, 4.03),
#  (0.03237, 6.998, 45.8, 222.0, 2.94),
#  (0.06905, 7.147, 54.2, 222.0, 5.33),
#  (0.02985, 6.43, 58.7, 222.0, 5.21),
#  (0.08829, 6.012, 66.6, 311.0, 12.43)]
#
#
# map_func = lambda x:(*x,round(x[0] + x[3] + x[4],2))
# updated_data = tuple(map(map_func,data))
# filtered_data = tuple(filter(lambda x: x[5] > 60,updated_data))
#
# print(filtered_data)
#

