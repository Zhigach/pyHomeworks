# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1


n = int(input("Enter natural number N: "))
arr = []

print("Enter values separated by newline: ")
for i in range(n):
    arr.append(int(input()))

x = int(input("Enter number X, program will count number of X occurrences in array: "))

count = 0
for item in arr:
    if item == x:
        count += 1

print(f"{x} is met in an array {arr} {count} time(s)")
