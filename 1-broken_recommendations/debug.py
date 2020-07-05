# Python3 код для демонстрации
# Поиск в матрице
# используя any () + понимание списка


# инициализирующий список

test_list = [[4, 5, 6],

             [10, 2, 13],

             [1, 11, 18]]

# печать оригинального списка

print("The original list : " + str(test_list))

# используя any () + понимание списка
# искать в матрице

res = any(13 in sub for sub in test_list)

# результат печати

print("Is 13 present in Matrix ? : " + str(res))