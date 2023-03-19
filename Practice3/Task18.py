# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Enter natural number N: "))
arr = []

print("Enter array values separated by newline: ")
for i in range(n):
    arr.append(int(input()))

x = int(input("Enter number X, program will find the number in array closest to X: "))

minDelta = abs(arr[0] - x)
minDeltaIndex = 0

for i in range(1, len(arr)):
    if abs(arr[i] - x) < minDelta:
        minDelta = abs(arr[i] - x)
        minDeltaIndex = i

print(f"{arr[minDeltaIndex]} is the closest to {x} value in {arr} array")