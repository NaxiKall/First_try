# import numpy as np
# number = np.random.randint(1,101)
# count = 0

# while True:
#     count += 1
#     predict_number = int(input("Угадай число от 1 до 100  "))
#     if predict_number < number:
#         print("Число должно быть больше")
#     elif predict_number > number:
#         print("Число должно быть меньше ")
#     else:
#         print(f"Вы угадали число! Это число - {number}. Вы потратили {count} попыток")
#         break

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(11) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == "__main__":
    score_game(random_predict)

