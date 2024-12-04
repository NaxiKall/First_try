# # Задаём вес входящего в лифт человека
# # Задаём грузоподъёмность
# max_weight = 400
# weight = 0
# # Задаём суммарный вес людей в лифте
# S = 0
# # Создаём цикл, который будет работать, пока S не превысит max_weight.
# while S < max_weight: # делай, пока…
#     print('введите вес входящего человека  ')
#     weight = int(input())
#     # Увеличиваем суммарный вес
#     # Равносильно S = S + weight
#     S += weight
#     # Выводим значение суммарного веса после обновления
#     print('Current sum weight', S)
#
#
# # Отделяем промежуточный вывод от результата пустой строкой
# print()
# # Выводим итоговое значение перевеса
# print('Overweight {} kg'.format(S - max_weight))


# volume = 10
# sum = 0
# while sum <= volume:
#     sum += 3.3
# cost = -volume + sum
# print(cost)


# # Создаём накопительную переменную, в которой будем считать сумму.
# S = 0
# # Задаём текущее натуральное число
# n = 1
# i = 0
#
# # Создаём цикл, который будет работать, пока сумма не превысит 500.
# while S < 500:  # делай, пока …
#     # Увеличиваем сумму, равносильно S = S + n
#     S += n
#     # Увеличиваем значение натурального числа
#     n += n
#     i+= 1
#     # Выводим строку ожидания
#     print(n)
# # Отделяем промежуточный вывод от результата пустой строкой
# print()
# # Выводим результирующую сумму
# print("Sum is: ", S)
# # Выводим результирующее количество чисел
# print("Numbers total: ", i)


# number = 1
# value = 10
#
# while value > number*number:
#     number+=1
# print(number)

# База позывных и паролей
secret_passwords = {
    'Enot': '1234',
    'Agent12': '12345',
    'MouseLulu': '2341'
}
# Создаём бесконечный цикл
# while True:
#     # Запрашиваем у пользователя позывной
#     name = input('Enter your name: ')
#     # Проверяем, что позывной есть среди ключей словаря.
#     if name in secret_passwords:
#         # Если позывной верный, запрашиваем у пользователя пароль.
#         password = input('Enter your password: ')
#         # Проверяем, что введённый пароль совпадает со значением по ключу позывного.
#         if password == secret_passwords[name]:
#             # Если пароль верный, выводим приветственное сообщение.
#             print('Welcome')
#             # Завершаем цикл
#             break
#         else:
#             # Если пароль неверный, выводим сообщение об ошибке.
#             print('Wrong password')
#     else:
#         # Если позывной неверный, выводим сообщение об ошибке.
#         print('Wrong name')

# value = 10
# number = 1
# while True:
#     if number * number > value:
#         print(number)
#         break
#     else:
#         number +=1

# i = 0
# n = int(input())
# while i < n:
#     print("Hello")
#     i+=1



# x = 1
# n = 10
#
# while x < n:
#     if x ** 2 % n == 0:
#         break
#     else:
#         x+=1



# value = 1000
# p = 1
# i = 1
# while p < value:
#     p*= i
#     i+=1
# print(p)


# money = 1000
# target_money = 3000
# year_count = 0
# while money < target_money:
#     money*= 1.08
#     year_count += 1
# print(year_count)


# hp = 500
# dmg = 80
# sec = 0
#
# while hp > 0:
#     hp -= dmg
#     sec +=1
# print(sec)


# n = 17
# fibonacci_list = [1]
# a = 1
# b = 1
# i = 1
# while i < n:
#     fibonacci_list.append(b)
#     c = b
#     b = b + a
#     a = c
#     i+=1
#
# print(fibonacci_list)



