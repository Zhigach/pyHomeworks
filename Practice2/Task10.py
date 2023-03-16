# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


map = ['орел', 'решка']


def printCoinOrientations(coinsArray):
    for orientation in coinsArray:
        print(map[orientation], end=' ')

n = int(input("Enter number of coins on the table (orientation will be generated randomly): "))
lst = []

for i in range(n):
    lst.append(random.randint(0, 1))

count = 0
for val in lst:
    if val == 1:
        count += 1

printCoinOrientations(lst)

print(f"\nМинимальное число монет, которые нужно перевернуть - {min(len(lst)//2, count)}")
