# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def powRecursion(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    return base*powRecursion(base, power-1)


a = int(input("Введите целое число - основание степени: "))
b = int(input("Введите целое число - показатель степени: "))

print(f"{a} в степени {b} равно {powRecursion(a,b)}")

