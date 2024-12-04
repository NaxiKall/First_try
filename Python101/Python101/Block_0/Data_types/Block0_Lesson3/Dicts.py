# empty_dict1 = {}
# empty_dict2 = {}
# print(empty_dict1, empty_dict2)


# alphabetic_dift = {"a":1, "b":2, "c":3, "d":4, "e": 5}
# print(alphabetic_dift["d"])

# place_and_money = {1 : 100, 2 : 50, 3 : 10}
# print(place_and_money[2])
# place_and_money[4] = 5
# print(place_and_money)


# place_and_money = {1 : 100, 2 : 50, 3 : 10}
# place_and_money[3] = 25
# print(place_and_money)


# place_and_money = {1: 100, 2: 50, 3: 25}                      ОБНУДЕНИЕ СЛОВАРЯ
# place_and_money.clear() ## == place_and_money = {}
# print(place_and_money)


# friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
# print(friends.keys()) ##Выводит только ключи


# place_and_money = {1: 100, 2: 50, 3: 25}
# print(place_and_money.keys())


# name_to_age = {'Anne': 22, 'Anton' : 27, 'Phillip': 30}       ПОИСК ЗНАЧЕНИЯ В СЛОВАРЕ
# print(name_to_age.keys())
# print(name_to_age.values())


# place_and_money = {1: 100, 2: 50, 3: 10 }
# print(place_and_money.get(20,"Такого нет."))                  ВЫВОД ЗНАЧЕНИЯ КОТОРОГО НЕТ


# name_to_age = {'Anne': 22, 'Anton' : 27, 'Phillip': 30}
# print(name_to_age.get("Danny",-1))


# place_and_money = {1:100, 2:50, 3:10}                        ОБНОВЛЕНИЕ СЛОВАРЯ
# place_and_money.update({4:5,5:1})
# print(place_and_money)


# name_to_age = {'Anne' : 22, "Anton" :  27, "Phillip" : 30}
# name_to_age.update({"Anne": 23, "Phillip" : 29})
# print(name_to_age)


# place_and_money = {1:100, 2:50, 3: 10}                 ##МЕТОД .pop
# result = place_and_money.pop(3)
# print(result)


# name_to_age = {"Anne" : 22, "Anton" : 27, "Phillip" : 30}
# result = name_to_age.pop("Anne")
# print(result)


# place_and_money = {1:100, 2:50, 3: 10}              #МЕТОД savedefault
# place_and_money.setdefault(10,1)
# print(place_and_money)



# name_to_age = {"Anne" : 22, "Anton" : 27, "Phillip" : 30}
# name_to_age.setdefault("Anne", 132)
# print(name_to_age)



# test_dict = {}                              #В КАЧЕСТВЕ КЛЮЧЕЙ МОГУТ БЫТЬ НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ, А В КАЧЕСТВЕ ЗНАЧЕНИЙ ЛЮБАЯ СТРУКТУРА ДАННЫХ
# test_dict.setdefault(5, [3,4,5])
# test_dict.setdefault((3,4,5), "strong man")
# print(test_dict)


