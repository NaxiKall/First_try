# python_string = 'Hello! My name is Python. I will help you to analyze some data.'
# print(python_string[18:24])
#
# print(len(python_string) **3)


# absolute_error = predicted_time - real_time
# if absolute_error < 0:
#     absolute_error *= -1
# round(absolute_error)

# input_string = 'Hello! My name is Python. I will help you to analyze some data.'
# ## count_words = 13
#
# input_string.replace(".","")
# input_string.replace(",","")
# input_string.replace("!","")
# input_string.replace("?","")
# input_string = input_string.split()
# count_words = 0
# for word in input_string:
#     count_words += 1
# print(count_words)
#
# file_path = 'data/images/train/10394.jpg'
# ## file_name = '10394'
# ## file_extension = 'jpg'
#
# file_path = file_path.split("/")
#
# image_name_ext = file_path[-1]
# image_name_ext = image_name_ext.split(".")
# file_name = image_name_ext[0]
# file_extension = image_name_ext[1]


# generated_text = "глаза нее на поднял он и она попросила что-нибудь скажи"
# ## updated_text = "скажи что-нибудь попросила она и он поднял на нее глаза"
#
# updated_text = " ".join(generated_text.split()[::-1])
#
# print(updated_text)

# def change_password(user_name, new_password):
#     return "Пользователь {} сменил пароль на {}".format(user_name,new_password)


# car_dict = {
#     'car_ID': [123, 117, 111, 82, 101, 96, 156, 2, 58, 49],
#     'fueltype': ['gas', 'diesel', 'diesel', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas'],
#     'horsepower': [68, 95, 95, 88, 97, 69, 62, 111, 101, 176],
#     'price': [7609.0, 17950.0, 13860.0, 8499.0, 9549.0, 7799.0, 8778.0, 16500.0, 13645.0, 35550.0]
# }
#
# mean_price = round(sum(car_dict['price']) / len(car_dict['price']),1)
# dis_c = len(list(filter(lambda x: x == "diesel",car_dict['fueltype'])))
# min_horsepower = min(car_dict['horsepower'])


# def check_duplicates(lst):
#     set_ln = len(set(lst))
#     list_ln = len(lst)
#     if set_ln == list_ln:
#         return False
#     return True


# def swap_places(lst):
#     first = lst[0]
#     last = lst[-1]
#     lst[0] = last
#     lst[-1] = first
#     return lst
# print(swap_places([1, 2, 3]))
# ## [3, 2, 1]
# print(swap_places([1, 2, 3, 4, 5]))
# ## [5, 2, 3, 4, 1]
# print(swap_places(['н', 'л', 'о', 'с']))
# ## ['с', 'л', 'о', 'н']


# def equalize_lengths(lst):
#     lst = sorted(lst,key= lambda x:len(x), reverse= True)
#     max_ln = len(lst[0])
#     for i in range(len(lst)):
#         n = max_ln - len(lst[i])
#         lst[i] = lst[i] + "_" * n
#     return lst
# print(equalize_lengths(['крот', 'белка', 'выхухоль']))
# # ['выхухоль', 'белка___', 'крот____']
#
# print(equalize_lengths(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# # ['aaaaa', 'aaaa_', 'aaa__', 'aa___', 'a____']
#
# print(equalize_lengths(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
#
# # ['qweasdqweas', 'ewqqqqq____', 'rteww______', 'q__________']
#
#
#
# def check_number_sign(number):
#     if number > 1:
#         return 1
#     elif number == 0:
#         return 0
#     else:
#         return -1


# def find_min_number(a,b,c):
#     if a < b:
#         min = a
#     else: min = b
#     if min < c:
#         return min
#     else: return c

# def sum_min_numbers(a,b,c):
#     nums = [a,b,c]
#     nums.sort()
#     return nums[0] + nums[1]
# print(sum_min_numbers(3,2,1))


# def division(a,b):
#     if b == 0:
#         print("Zero division error!")
#         return None
#     return a / b

# def get_prediction(x1,x2):
#     if x1 < 20:
#         if x2 < 200:
#             return 300.5
#         else:
#             return 65.7
#     else:
#         if x2 > 170:
#             return 1023
#         else:
#             if x2 > 40:
#                 return -64.1
#             else:
#                 return 0.7
#

# def more_than_n(lst,n):
#     return list(filter(lambda x: abs(x) > n,lst ))

# def lucky_ticket(ticket_num):
#     str_t_n = str(ticket_num)
#     num_lst = []
#     for num in str_t_n:
#         num_lst.append(num)
#     sum_last = 0
#     sum_first = 0
#     for ord_num in range(3):
#         sum_first += int(num_lst[ord_num])
#         sum_last += int(num_lst[-ord_num -1])
#     print(sum_first,sum_last)
#     if sum_last == sum_first:
#         return True
#     return False
#
# print(lucky_ticket(515740))


# def holes_count(number):
#     holes = 0
#     num_lst = []
#     s_n = str(number)
#     for digit in s_n:
#         if int(digit) in [0,4,6,9]:
#             holes += 1
#         if int(digit) == 8:
#             holes += 2
#     return holes

# def even_numbers_in_matrix(matrix):
#     count = 0
#     for row in matrix:
#         for digit in row:
#             if digit % 2 == 0:
#                 count += 1
#     return count


# def matrix_sum(matrix1,matrix2):
#     sum_matrix = []
#     def matrix_check(matrix):
#         row_count = 0
#         line_count = 0
#         for row in matrix:
#             row_count += 1
#             for line in row:
#                 line_count += 1
#         return row_count,line_count
#
#     if  matrix_check(matrix1) != matrix_check(matrix2):
#         print("Error! Matrices dimensions are different!")
#         return None
#     i = 0
#     j = 0
#     sum_matrix = np.array(matrix1) + np.array(matrix2)
#     return list(sum_matrix)
# matrix1_example = [
#           [1, 5, 4],
#           [4, 2 ,2],
#           [5, 2, 1]
# ]
#
# matrix2_example = [
#           [10, 15, 43],
#           [41, 2, -2],
#           [7, 5, 7]
# ]
# print(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))




# def print_personal_data(**data):
#     data_dict = dict(sorted(data.items()))
#     for item in data_dict:
#         print(item + ":", data_dict.get(item))
#
# print_personal_data(first_name='John', last_name='Doe', age=28, position='Python developer')


# def get_word_list(text):
#     punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#     text = text.lower()
#     for symbol in text:
#         if symbol in punctuation_list:
#             text = text.replace(symbol," ")
#     word_list = text.split()
#     return word_list
#
# print(get_word_list("Gfjdlkfj f.    m,fsfm. fafa: fsadfsa...sds sfs"))


# def get_unique_words(word_list = None):
#     count_dict = dict()
#     for word in word_list:
#         if word not in count_dict:
#             count_dict[word] = 1
#         else:
#             count_dict[word] += 1
#     return dict(sorted(count_dict.items()))
#
# words_list_example = ['and', 'take', 'the', 'most', 'special', 'care', 'that', 'you', 'locate', "muad'dib", 'in', 'his', 'place', 'the', 'planet', 'arrakis', 'do', 'not', 'be', 'deceived', 'by', 'the', 'fact', 'that', 'he', 'was', 'born', 'on', 'caladan', 'and', 'lived', 'his', 'first', 'fifteen', 'years', 'there', 'arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
#
# print(get_unique_words(word_list = words_list_example))
# ## ['and', 'arrakis', 'as', 'be', 'born', 'by', 'caladan', 'care', 'deceived', 'do', 'dune', 'fact', 'fifteen', 'first', 'forever', 'he', 'his', 'in', 'is', 'known', 'lived', 'locate', 'most', "muad'dib", 'not', 'on', 'place', 'planet', 'special', 'take', 'that', 'the', 'there', 'was', 'years', 'you']


# def get_most_frequent_word(unchanged_text):
#     final_text = dict()
#     def get_word_list(text):
#         punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#         text = text.lower()
#         for symbol in text:
#             if symbol in punctuation_list:
#                 text = text.replace(symbol," ")
#         word_list = text.split()
#         return word_list
#     changed_text = get_word_list(unchanged_text)
#
#     def get_words_count(word_list=None):
#         count_dict = dict()
#         for word in word_list:
#             if word not in count_dict:
#                 count_dict[word] = 1
#             else:
#                 count_dict[word] += 1
#         return dict(sorted(count_dict.items(),key= lambda item: item[1], reverse= True))
#     final_text = get_words_count(changed_text)
#     return next(iter(final_text))
#
# text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
# print(get_most_frequent_word(text_example))
# # the
#
# text_example = "Есть урок, который идет не сорок пять минут, а всю жизнь. Этот урок проходит и в классе, и в поле, и дома, и в лесу. Я назвал этот урок седьмым потому, что в школе обычно бывает не больше шести уроков. Не удивляйтесь, если я скажу, что учителем на этом уроке может быть и береза возле вашего дома, и бабушка, и вы сами (В. Песков)"
# print(get_most_frequent_word(text_example))
# # и

# def get_total_score(dataa):
#     updated_data_def = lambda x:(*x, x[1] + x[2] + x[3])
#     updated_data = list(map(updated_data_def,dataa))
#     return sorted(updated_data, key= lambda x: x[4])
#
#
#
# data = [
#     ('Amanda', 37, 78, 67),
#     ('Patricia', 78, 93, 68),
#     ('Marcos', 79, 67, 89),
#     ('Dmitry', 67, 68, 100),
#     ('Andrey', 100, 78, 76),
#     ('Victoria', 93, 69, 96),
# ]
#
# print(get_total_score(data))
# # [('Amanda', 37, 78, 67, 182), ('Marcos', 79, 67, 89, 235), ('Dmitry', 67, 68, 100, 235), ('Patricia', 78, 93, 68, 239), ('Andrey', 100, 78, 76, 254), ('Victoria', 93, 69, 96, 258)]
