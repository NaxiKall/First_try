
#

# def get_count_unique_symbols(s):
#     s = s.lower()
#     s = s.replace(" ","")
#     unsymb = []
#     for symbol in s:
#         if symbol not in unsymb:
#             unsymb.append(symbol)
#     return len(unsymb)
# print(get_count_unique_symbols('Это простая строка'))
# def get_min_string(s1,s2):
#     def get_count_unique_symbols(s):
#         s = s.lower()
#         s = s.replace(' ', '')
#         # Возвращаем количество уникальных символов
#         # Это будет длина множества, составленного из строки
#         return len(set(s))
#     if len(set(s1)) < len(set(s2)):
#         return s1
#     elif len(set(s1)) > len(set(s2)):
#          return s2
#     else:
#         return (s1,s2)
#
# print(get_min_string(s1 = 'школа', s2 = 'school'))
#
# pi = 3.1416
# def calculate_area_circle(r):
#     area = pi * r ** 2
#     return round(area,3)
#
# def calculate_area_ellipse(a,b):
#     area = pi * a * b
#     return round(area,3)
#
# print(calculate_area_circle(r=5))


# money = 200000
# def cash(less_money):
#     global money
#     money -= less_money
#     return money
#
#
# cash(1000)
# print(money)


# # Словарь с курсами валют (по отношению к рублю)
# currencies = {'USD': 74, 'EUR': 88, 'GBP': 98 , 'CHF': 82}
# # Общее количество денег на счету, которое нужно конвертировать
# money = 100000
# # Функция для конвертации валюты, аргумент - наименование валюты
# def convert(currencies,money,currency):
#     # Объявляем, что money - глобальная переменная
#     # Производим конвертацию - делим количество денег на счету на соответствующий курс
#     money = money / currencies[currency]
#     return money
#
# convert_money = convert(currencies, money, 'EUR')
# print(convert_money)

#
# def calculate_cost(cost, sale):
#     def prikol():
#         nonlocal sale
#
#         # Внутренняя функция для предобработки аргумента sale
#         def preprocessing_sale():
#             # Объявляем, что используем нелокальную переменную sale
#             nonlocal sale
#             # Если sale — строка
#             if type(sale) is str:
#                 # Удаляем из строки '%', приводим к float и делим на 100
#                 sale = float(sale.replace('%', '')) / 100
#             # Если sale — целое число
#             elif type(sale) is int:
#                 # Делим его на 100
#                 sale = sale / 100
#         # Запускаем предобработку, прежде чем вычислить стоимость
#         preprocessing_sale()
#         # Считаем итоговую стоимость и возвращаем её
#         # (стоимость — стоимость * скидка)
#         return cost - cost * sale
#     return prikol()
#
# print(calculate_cost(1330, '15%'))



# # Функция для вычисления количества символов (symbol) в строке s
# def count_occurrences(s, symbol):
#     # Внутренняя функция для предобработки строки s
#     def preprocessing_s():
#         nonlocal s
#         s = s.replace(' ', '')
#         # Приводим строку к нижнему регистру
#         s = s.lower()
#     # Вызываем функцию для предобработки аргумента s
#     preprocessing_s()
#     # Считаем количество символов symbol в строке s и возвращаем результат
#     return s.count(symbol)
#
# print(count_occurrences('This is simple string', symbol='t'))
#
# advertising_campaigns = {'ютуб': [212, 248], 'вк': [514, 342], 'радио': [339, 125]}

# # Создаём новый пустой словарь
# advertising_campaigns_max = {}
# # Создаём цикл по ключам исходного словаря
# for key in advertising_campaigns:
#     # Вычисляем максимум в списке, лежащем по ключу key
#     maksimum = max(advertising_campaigns[key])
#     # Добавляем максимум в новый словарь
#     advertising_campaigns_max[key] = maksimum

#
# def register(surname, name, date, middle_name=None, registry=None):
#     # Вспомогательная функция для предобработки даты
#     def preprocessing_date(date):
#         # Разделяем строку по символу точки
#         day, month, year = date.split('.')
#         # Преобразуем все данные к типу данных int
#         day, month, year = int(day), int(month), int(year)
#         return day, month, year
#     # Если список не был передан — создаём пустой список
#     if registry is None:
#         registry = list()
#     # Разделяем дату на составляющие
#     day, month, year = preprocessing_date(date)
#     # Добавляем данные в список
#     registry.append((surname, name, middle_name, day, month, year))
#     def check_date():
#         nonlocal day, month, year
#         if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
#             return False
#             # Проверяем год на заданный диапазон
#         if (year <= 1900) or (year >= 2024):
#             return False
#             # Проверяем месяц на заданный диапазон
#         if (month < 1) or (month > 12):
#             return False
#             # Проверяем день на заданный диапазон
#         if (day < 1) or (day > 31):
#             return False
#             # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
#         if (month in [4, 6, 9, 11]) and (day > 30):
#             return False
#             # Проверяем количество дней в феврале
#         def is_leap():
#             nonlocal year
#             return year % 400 == 0 or year % 4 == 0 and year % 100 !=0
#         if month == 2 and day > 28:
#             return is_leap()
#         return True
#     check_date()
#     if check_date() is False:
#         raise ValueError("Invalid Date!")
#     return registry
#
#
#
# reg = register('Petrova', 'Maria', '13.03.2003', 'Ivanovna')
# reg = register('Ivanov', 'Sergej', '24.09.1995', registry=reg)
# reg = register('Smith', 'John', '13.02.2003', registry=reg)
# print(reg)
# ## [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]
#
# reg = register('Ivanov', 'Sergej', '24.13.1995')
# ## ValueError: Invalid Date!
#



# def triangle(p1, p2, p3):
#
#     # Функция для вычисления сторон треугольника
#     # По умолчанию параметры функции берутся из объемлющей области видимости
#     def sides(p1, p2, p3):
#         # Распаковываем кортежи для удобства, “;” означает новую строку кода
#         x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
#         # Вычисляем стороны по теореме Пифагора
#         a = ((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5
#         b = ((x3 - x1) ** 2 + (y3 - y1)** 2) ** 0.5
#         c = ((x3 - x2) ** 2 + (y3 - y2)** 2) ** 0.5
#         return a, b, c
#
#     def check_exist_triangle(a, b, c):
#         if a + b > c and a + c > b and b + c > a:
#             return True
#         raise ValueError("Треугольник не существует")
#
#
#     # Функция для вычисления периметра треугольника
#     def calculate_perimeter_triangle(a, b, c):
#         # Периметр — сумма всех сторон треугольника
#         perimeter = a + b + c
#         return perimeter
#
#     # Функция для вычисления площади треугольника
#     def calculate_area_triangle(a, b, c):
#         # Вычисляем полупериметр
#         # Значение perimeter берётся из объемлющей области видимости
#         p = perimeter / 2
#         # Вычисляем площадь по формуле Герона
#         area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#         return area
#     a, b, c = sides(p1, p2, p3)
#     check_exist_triangle(a,b,c)
#     perimeter = calculate_perimeter_triangle(a, b, c)
#     area = calculate_area_triangle(a, b, c)
#     result = {'a': a, 'b': b, 'c': c, 'perimeter': perimeter, 'area': area}
#     return result
#
# print(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
# ## {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
# print(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
# ## {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}
# print(triangle(p1=(2.5, 2), p2=(4, 1), p3=(1, 3)))
# ## ValueError: Треугольник не существует

# pi = 3.1416
# def circle(p1,p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     def radius():
#         r = (((x2 - x1) ** 2) + ((y2 - y1)**2)) ** 0.5
#         return r
#     rad = radius()
#     def calculate_circumference():
#         l = 2 * pi * rad
#         return round(l,3)
#     def calculate_area_circle():
#         s = pi * rad ** 2
#         return round(s,3)
#     return {"radius":round(rad,3), "circumference": calculate_circumference(), "area": calculate_area_circle()}
#
# print(circle(p1=(3, 2.5), p2=(4, 4.5)))

