#Один из клиентов сыроварни — магазин здорового питания. Им важно, чтобы сыры, которые им поставляет сыроварня, имели жирность менее n %

def filter_by_fat(data,n):
    fat_values = {key: values[2] for key,values in data.items()}
    updated_data = {key: fat for key, fat in fat_values.items() if fat < n}
    return updated_data

cheese_data = {
    'чеддер': [370, 5000, 33, 'твердый'],
    'пармезан': [510, 4000, 29, 'твердый'],
    'гауда': [250, 3700, 27, 'полутвердый'],
    'эдам': [220, 10000, 30, 'полутвердый'],
    'горгонзола': [320, 3000, 32, 'полумягкий'],
    'рокфор': [340, 15000, 31, 'полумягкий'],
    'стилтон': [360, 7000, 35, 'полумягкий'],
    'камамбер': [250, 8000, 24, 'мягкий'],
    'бри': [310, 6500, 28, 'мягкий'],
}
# print(filter_by_fat(cheese_data,27) )

def count_money(data):
    cheese_money = {key: values[0] * 10 *  values[1] for key,values in data.items()}
    return sum(cheese_money.values())

# print(count_money(cheese_data))

def find_cheese_type(data,cheese_type):
    updated_data = {key: cheese[3] for key, cheese in data.items() if cheese[3] == cheese_type}
    return list(updated_data.keys())

# print(find_cheese_type(cheese_data, cheese_type='мягкий'))


def sort_cheese(data):
    updated_data = dict(sorted(data.items(), key= lambda items:items[1]))
    return list(updated_data.keys())
# print(sort_cheese(cheese_data))


def purchase(items):
    items_dict = dict()
    for item in items:
        if item not in items_dict:
            items_dict[item] = 1
        else:
            items_dict[item] += 1
    updated_data = {key : value for key,value in items_dict.items() if value > 1}
    if not updated_data:
        print("Ваш заказ оформлен верно")
    else:
        for key,value in updated_data.items():
            if value > 1:
                print("Вы продублировали ингредиент {} в заказе {} раз(а)".format(key,value))




ingredients = ['кислота уксусная', 'кислота лимонная', 'закваска', 'кислота молочная', 'пряность', 'бактерии', 'аннато', 'кальций', 'калий', 'специя', 'молоко коровье', 'молоко овечье', 'фермент', 'соль', 'сливки', 'грибки', 'ароматизатор', 'молоко козье', 'дрожжи', 'каротин']

purchase(ingredients)
# Ваш заказ оформлен верно

ingredients = ['молоко коровье', 'молоко овечье', 'бактерии', 'молоко козье', 'сливки', 'фермент', 'закваска', 'молоко коровье', 'соль', 'молоко коровье', 'бактерии', 'молоко овечье', 'кислота лимонная', 'грибки', 'соль', 'дрожжи', 'кислота уксусная', 'кальций', 'калий', 'каротин', 'аннато', 'специя', 'пряность', 'ароматизатор', 'соль', 'кислота молочная']

purchase(ingredients)
# Вы продублировали ингредиент бактерии в заказе 2 раз(а)
# Вы продублировали ингредиент молоко коровье в заказе 3 раз(а)
# Вы продублировали ингредиент молоко овечье в заказе 2 раз(а)
# Вы продублировали ингредиент соль в заказе 3 раз(а)


