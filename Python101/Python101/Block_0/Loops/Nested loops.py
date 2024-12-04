# temperature = [
#     [13, 15, 10],
#     [14, 13, 9],
#     [8, 9, 6]
# ]
# print(temperature[0][2])
# print(temperature[1][1])
# print(temperature[2][0])


# matrix = [
#     [1, 2 , 4],
#     [3, 4],
#     [5, 6]
# ]
# for r in matrix:
#     print("Current row ", r)
#     for elem in r:
#         print("elem ", elem)


# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
#
#
# # Вычисляем длину внешнего списка
# N = len(matrix)
# # Вычисляем длину вложенного списка
# M = len(matrix[0])
# # Создаём цикл по последовательности чисел от 0 до N (не включая N)
# # i — текущий элемент последовательности (индекс строки)
# for i in range(N):
#     # Выводим текущее значение i
#     print('Current i', i)
#     # Выводим i-е значение внешнего списка
#     print('Current row', matrix[i])
#     # Создаём цикл по последовательности чисел от 0 до M (не включая M)
#     # j — текущий элемент последовательности (индекс столбца)
#     for j in range(M):
#         # Выводим текущее значение j
#         print('Current j', j)
#         # Выводим элемент под индексами i и j
#         print('Current elem', matrix[i][j])
#     # Отделяем вывод на экран пустой строкой
#     print()


# hours = list(range(9, 24, 2))
# minutes = list(range(0,60,15))
#
# for hour in hours:
#     for minute in minutes:
#         if minute == 0:
#             print('Alarm is set on {}:{}0'.format(hour,minute))
#         else:
#             print('Alarm is set on {}:{}'.format(hour,minute))

# letters = ''
# count = 0
# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# for word in str_list:
#     letters += word
#     for let in word:
#         if let == 'e':
#             count+= 1
# print(count)


# letters = ''
# count = 0
# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# for word in str_list:
#     count += word.count('e')
# print(count)


# text_list = [
#     'afbaad2',
#     'faaf',
#     'afaga',
#     'agag'
# ]
# i = 1
# for text in text_list:
#     count = 0
#     for symbol in text:
#         if symbol == 'a':
#             count += 1
#     print("В {} строке {} букв(ы) 'а'".format(i, count))
#     i+=1


# min_value_rows = []
# random_matrix = [[9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
#                  ]
#
# for row in random_matrix:
#     min_value = row[0]
#     for num in row:
#         if num < min_value:
#             min_value = num
#     min_value_rows.append(min_value)
# print(min_value_rows)


# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
# max_value_rows = []
#
#
# for row in random_matrix:
#     max_value = row[0]
#     for number in row:
#         if number > max_value:
#             max_value = number
#     max_value_rows.append(max_value)
# print(max_value_rows)



# student_scores = [
#     [56, 90, 80],
#     [80, 86, 92],
#     [91, 76, 89],
#     [91, 42, 60],
#     [65, 30, 90]
# ]
# amount_exams = len(student_scores[0])
# amount_students = len(student_scores)
# i = 0
# avg = 0
# sum = 0
# for student in student_scores:
#     sum_exam = 0
#     i+=1
#     for exam in student:
#         sum_exam += exam
#         avg_student = sum_exam / amount_exams
#         sum += exam
#     print('Средний балл студента под номером {}: {}'.format(i, avg_student))
# print(sum,amount_students,amount_exams)
# avg = sum / (amount_students * amount_exams)
# print("Cредний балл по всем экзаменам:", avg)



# student_scores = [
#     [56, 90, 80],
#     [80, 86, 92],
#     [91, 76, 89],
#     [91, 42, 60],
#     [65, 30, 90]
# ]
# N = len(student_scores) # Задаём число студентов
# M = len(student_scores[0]) # Задаём число экзаменов
# summa = 0 # Задаём начальное значение общего балла
# math_sum = 0 # Задаём начальное значение общего балла по математике
# info_sum = 0 # Задаём начальное значение общего балла по информатике
# rus_sum = 0 # Задаём начальное значение общего балла по русскому языку
# # Создаём цикл по последовательности от 0 до N (не включая N)
# for i in range(N): # i — индекс строки
#     # Добавляем баллы по математике i-го студента
#     math_sum += student_scores[i][0]
#     # Добавляем баллы по информатике i-го студента
#     info_sum += student_scores[i][1]
#     # Добавляем баллы по русскому языку i-го студента
#     rus_sum += student_scores[i][2]
#     # Создаём цикл по последовательности от 0 до M (не включая M)
#     for j in range(M): # j — индекс столбца
#         # Добавляем баллы i-го студента по j-му экзамену
#         summa += student_scores[i][j]
# # Выводим средний балл по математике
# print('Average math score', math_sum / N)
# # Выводим средний балл по информатике
# print('Average info score', info_sum / N)
# # Выводим средний балл по русскому языку
# print('Average rus score', rus_sum / N)
# # Выводим общий средний балл
# print('Average score', summa /(N*M))


# test_matrix = [
#     [1, 2, 3,  4],
#     [7, -1, 2, 5],
#     [123, 2, -1, 3],
#     [123, 5, 1]
# ]
# max_len = 0
# min_len = 9999999999999999999
#
# for leng in test_matrix:
#     if max_len < len(leng):
#         max_len = len(leng)
#     if min_len > len(leng):
#         min_len = len(leng)
# if len(test_matrix) == min_len == max_len:
#     is_square = True
# else:
#     is_square = False
# print(is_square)
#
#
# # Вычисляем число строк в матрице
# num_lines = len(test_matrix)
# # Задаём начальное количество строк, длина которых совпадает с числом строк в матрице.
# count = 0
# # Создаём цикл по строкам матрицы
# for line in test_matrix: #line — текущая строка матрицы
#     # Проверяем, что длина текущей строки равна количеству строк.
#     if len(line) == num_lines:
#         # Если условие выполняется, увеличиваем количество строк,
#         # длина которых совпадает с числом строк в матрице.
#         count += 1
# # Cравниваем полученное число с числом строк в матрице
# is_square = num_lines == count


# temp = [[25, 27, 28, 26, 27, -26, -25, -2, 26], [21, 22, 28, 27, 28, 26, 25, 19, 26], [-19, 21, 25, -27, 28, 25, 21, 20, 26]]
#
# month = len(temp)
# day = len(temp[0])
#
# for i in range(month):
#     for j in range(day):
#         if temp[i][j] < 0:
#             temp[i][j] *= -1
# print(temp)

customer_satisfaction = [
    [0.87, 0.56, 0.77],
    [0.22, 0.46, 0.56, 0.89, 0.95],
    [0.45, 0.44, 0.68],
    [0.73, 0.88, 0.95, 0.49]
]

month_satisfaction = []

for month in customer_satisfaction:
    sum = 0
    count = 0
    for value in month:
        sum += value
        count +=1

    sr = round(sum / count,2)
    month_satisfaction.append(sr)
print(month_satisfaction)