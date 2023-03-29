# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random


def createRandomIntArray(length):
    return [random.randint(0, 10) for i in range(length)]


low = int(input("Specify the lower limit: "))
high = int(input("Specify the upper limit: "))
arr = createRandomIntArray(30)

print(arr)
print([low <= item <= high for item in arr].count(True))
