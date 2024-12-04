from collections import Counter
from statistics import median

from Tools.scripts.pindent import start
from lib2to3.fixer_util import is_list


##Задача один
# def pure_intersection(string1,string2):
#     #Создаем строки для проверки условия
#     check_string1 = string1.replace(" ","").replace(",","")
#     check_string2 = string2.replace(" ", "").replace(",", "")
#     # Убираем пробелы и запятые, а также создаем множества
#     string1 = string1.replace(" ", "")
#     set1 = string1.split(",")
#     set1 = set(set1)
#     string2 = string2.replace(" ", "")
#     set2 = string2.split(",")
#     set2 = set(set2)
#     #Проверяем, являются ли все символы в строке цифрами
#     if not check_string1.isdigit() or not check_string2.isdigit():
#         #Выводим пользователю сообщение о том, что он ввел неправильные данные
#         print("Некорекктный ввод")
#         return
#     #Выводим результат
#     print(list(set1.intersection(set2)))
#
#
# input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
# input_string2 = input('Введите 2-ую последовательность идентификаторов: ')
#
# pure_intersection(input_string1,input_string2)
#

# #Задача два
# def find_min_max(line: str):
#     #Меняем запятые на точки
#     line = line.replace(",", ".")
#     #Разделяем строку по пробелам
#     line = line.split()
#     #Создаем новый список, в который программа будет записывать подходящие переменные
#     updated_line = list()
#     #Сортируем строку так, чтобы в ней были только float значения
#     for num in line:
#         try:
#             float(num)
#             updated_line.append(float(num))
#         except ValueError:
#             pass
#         #Выводим на экран ответ
#     print("Minimum: ", min(updated_line), "\nMaximum: ", max(updated_line))
#
#
# (find_min_max("-2,56 25,002 восемь 19,13 13 -37,5"))
#

# # Задача три
# def find_median(line:str):
#     #Меняем запятые на пробелы
#     line = line.replace(","," ")
#     #Делим строку по пробелам
#     line = line.split()
#     #Создаем новый список
#     updated_line = list()
#     #Проверяем является ли список пустым, если он пустой, то сообщаем пользователю о неккоректном вводе
#     if not line:
#         raise ValueError("Неккоректный ввод")
#     #Проверяем являются ли все значения в списке числами, если да то добавляем их в новый список, если нет, то сообщаем пользователю о неккоректном вводе
#     for num in line:
#         if float(num.isdigit()):
#             updated_line.append(float(num))
#         else:
#             raise ValueError("Неккоректный ввод")
#     #Cортируем список
#     updated_line = sorted(updated_line)
#     #Находим медиану и выводим ее
#     if len(updated_line) %2 == 0:
#         print("Median: ",   ((updated_line[len(updated_line) // 2 - 1]) + updated_line[len(updated_line) // 2]) / 2)
#     else:
#         print("Median: ",updated_line[len(updated_line) // 2])
#
#
# (find_median("100, 5, 2, 4, 3, 6"))

# #Задача чотыре
#
# def transform_string_to_integer(digit:str):
#     #Создаем переменную, в которую будем записывать число
#     final_num = 0
#     temp_num = 0
#     #Словарь с суффиксами и числами
#     number_word_dict = {
#         "ты": 1000, "м": 1000000,
#         "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800,
#         "девятьс": 900,
#         "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18,
#         "девятн": 19,
#         "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
#         "дес": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }
#     #Превращаем строку в список с делением по пробелу
#     digit = digit.split()
#     #Проверяем каждое слово в строке
#     for num in digit:
#         #Проверяем каждый ключ на соответствие начала строки
#         for key in number_word_dict.keys():
#             #Если число начинается с символов, которые являются ключами списка, то проверяем есть ли в числе тысячные или миллионные разряды
#             if num.startswith(key):
#                 if key == "ты" or key == "м":
#                     #Если это тысяча или миллион, то умножаем на тысячу или миллион
#                     temp_num*= number_word_dict[key]
#                     final_num += temp_num
#                     temp_num = 0
#                     #Прерываем выполнение кода, чтобы не возникало проблем с повторами
#                     break
#                 else:
#                     temp_num += number_word_dict[key]
#                     break
#     final_num += temp_num
#
#     #Выводим число
#     print(final_num)
# (transform_string_to_integer("один миллион двести тридцать четыре тысячи пятьсот шестьдесят семь "))

#Задача пять
#Импортируем функцию factorial из библиотеки math
from math import factorial
def decompose_factorial(n):
    if n <= 0:
        raise ValueError("Некорректный ввод")
    result_line = str
    #Создаем факториал n
    m = factorial(n)
    #Функция разложения числа на множители
    def factor(n):
        ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            ans.append(n)
        return ans
    #Раскладываем число на множители
    lst = factor(m)
    #Создаем список, в который будем добавлять множитель числа и его количество с правильным выводом
    string_lst = list()
    #Создаем словарь, в котором находятся множители числа и их количество
    counted_dict = dict(Counter(lst))
    #Делаем часть вывода
    print(n,"! = ",sep="",end="")
    #Цикл, который добавляет в список множители числа и их количество с правильным выводом
    for key, value in counted_dict.items():
        #Если количество = 1, то количество выводить не надо
        if value == 1:
            string_lst.append(str(key))
        else:
            string_lst.append(str(key) +  "^" + str(value))
    #Соединяем элементы списка в строку
    result_line = " * ".join(string_lst)
    #Выводим результат
    print(result_line)


decompose_factorial(-1)
