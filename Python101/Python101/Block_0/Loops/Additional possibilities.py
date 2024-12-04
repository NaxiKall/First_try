# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
#
# for day, dynamic in enumerate(user_dynamics):
#     if dynamic < 0:
#         print("В {} день ушло {} клиентов".format(day + 1,dynamic))


# str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
# cut_str_list = []
#
# for i,word in enumerate(str_list):
#     cut_str_list.append([i,word[:3]])
# print(cut_str_list)


# # Список вещей, которые нужно положить в инвентарь.
# to_inventory = ['Blood Moon Sword', 'Sunset-colored sword', 'Bow of Stars', 'Gain Stone']
# # Задаём пустой инвентарь
# inventory = []
# # Создаём цикл по элементам списка to_inventory
# # item — текущий элемент списка
# for item in to_inventory:
#     # Проверяем условие, что инвентарь уже заполнен.
#     if len(inventory) == 3:
#         # Если условие выполняется,выводим предупреждение об ошибке.
#         print('Inventory is full!')
#         # Завершаем работу цикла
#         break
#     # Если цикл не завершился добавляем предмет в инвентарь
#     inventory.append(item)
# # Выводим результирующий инвентарь
# print(inventory)


# Задаём число
# n = 812
# # Создаём бесконечный цикл
# while True:
#     # Проверяем условие, что остаток от деления на 3 равен 0.
#     if n % 3 == 0:
#         # Если условие выполняется, новое число — результат целочисленного деления на 3.
#         n = n // 3
#         # Проверяем условие, что в результате деления получили 1.
#         if n == 1:
#             # Выводим утвердительное сообщение
#             print('n - is the power of the number 3!')
#             # Выходим из цикла
#             break
#     else:
#         # В противном случае выводим сообщение-опровержение
#         print('n - is not the power of the number 3!')
#         # Выходим из цикла
#         break

# n = 19
# origin = n
# # Создаём бесконечный цикл
# while True:
#     if n % 2 == 0:
#         n /= 2
#     else:
#         n = (n * 3 + 1) // 2
#     if n == 1:
#         # Если условие выполняется, выводим утвердительное сообщение.
#         print(f'Syracuse hypothesis holds for number {origin}')
#         break
#
#         # Ваш код здесь


# client_status = {
#     103303: 'yes',
#     103044: 'no',
#     100423: 'yes',
#     103032: 'no',
#     103902: 'no'
# }
#
# for i, user_id in enumerate(client_status):
#     print(user_id, client_status[user_id])


# mixture_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
# count_numbers = 0
# for stroka in mixture_dict:
#     if type(mixture_dict[stroka]) is str:
#         continue
#     else:
#         count_numbers += 1
# print(count_numbers)


# text = """
# The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.
#
# Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.
#
# `Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
# """
# symbols_dict = {}
# text = text.lower()
# text = text.replace(' ', "")
# text = text.replace("\n","")
#
# for symbol in text:
#     if symbol  not in symbols_dict:
#         symbols_dict[symbol] = 1
#     else:
#         symbols_dict[symbol] += 1
# print(symbols_dict)

# text = """
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I am sure.
# So if she sells sea shells on the sea shore,
# I am sure that the shells are sea shore shells.
# """
#
# count_punctuation = {',': 0, '.': 0, '?': 0, '!': 0, ';': 0, '—': 0}
#
# for symbol in text:
#     if symbol in count_punctuation:
#         count_punctuation[symbol] += 1
#
# print( count_punctuation)


# sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm.'
#
# sentence = sentence.lower()
# sentence = sentence.replace('.','')
# sentence = sentence.replace(",",'')
# sentence =sentence.split()
# word_dict = {}
#
# for word in sentence:
#     if word not in word_dict:
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
#
# print(word_dict)


# str_list = ["text", "morning", "notepad", "television", "ornament"]
# symbol_to_check = 't'
# word_dict = {}
#
# for  word in str_list:
#     count = 0
#     for letter in word:
#         if letter == symbol_to_check:
#             count += 1
#     word_dict.update({word:count})
# print(word_dict)