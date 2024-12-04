# # Напишите функцию get_less(list_in, num), которая принимает на вход список list_in, состоящий из чисел, и ещё одно число num.
# #
# # Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. Если такого числа нет, необходимо вернуть None.
#
# def get_less(list_in, num):
#     for cock in list_in:
#         if num > cock:
#             return cock
#     return None
#
# print(get_less([1, 5, 8,  10], 8))


## Напишите функцию split_date(date), которая принимает на вход строку, задающую дату, в формате ддммгггг без разделителей. Функция должна вернуть кортеж из чисел (int): день, месяц, год.
# def split_date(date):
#     datespl1 = date[0:2]
#     datespl2 = date[2:4]
#     datespl3 = date[4:]
#     tpl1 = (int(datespl1),int(datespl2),int(datespl3))
#     return tpl1
# print(split_date("31012019"))
#
# def split_date(date):
#    day, month, year = date[:2], date[2:4], date[4:]
#    return int(day), int(month), int(year)


# def is_prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num):
#         ost = num % i
#         if ost == 0:
#             return False
#     return True

#
# def between_min_max(*args) :
#    max1 = max(*args)
#    min1 = min(*args)
#    mean = (max1 + min1) /2
#    return mean


# def best_student(**students):
#     studentsdicts = {}
#     studentsdicts.update(students)
#     rating = studentsdicts.values()
#     top_stud = max(rating)
#     for key,val in studentsdicts.items():
#         if val == top_stud:
#             return key
# print(best_student(Tom=12, Jerry=1, Jane=2))
#

#
# def is_palindrom(str1):
#     for i in range(0,int(len(str1)/2)):
#         if str1[i] != str1[len(str1) - i - 1]:
#             return "no"
#     return "yes"
# print(is_palindrom("123321"))
#
# is_palindrom = lambda s: "yes" if s == s[::-1] else "no"


# area = lambda a,b : a*b

#
# between_min_max = lambda *nums: max(nums) + min(nums) / 2

# def sort_ignore_case(ls):
#     return sorted(ls,key= lambda word: word.lower())
# print(sort_ignore_case(['Acc', 'abc']))

# def exchange(rate = None,rub = None,usd = None):
#     args = 0
#     if rate is not None:
#         args +=1
#     if rub is not None:
#         args +=1
#     if usd is not None:
#         args +=1
#     if args == 1:
#         raise ValueError('Not enough arguments')
#     if args == 3:
#         raise ValueError('Too many arguments')
#     if rate is not None and rub is not None:
#         return rub / rate
#     if rate is not None and usd is not None:
#         return usd * rate
#     if usd is not None and rub is not None:
#         return rub / usd
#
# print(exchange(usd = 12))
