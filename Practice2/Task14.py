# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter number N, this program will print all powers of 2 that are not higher than N: "))

power = 1
counter = 0
while power < n:
    print(f"2 power {counter} is {power}")
    power *= 2
    counter += 1
